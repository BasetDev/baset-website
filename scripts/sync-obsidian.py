#!/usr/bin/env python3
"""
Sync script inspired by yazdan.me/scripts/sync-vault.ts
Syncs Markdown articles from Obsidian vault (D:\\obsidian\\obsidiainbrain\\me\\website)
into repository's content/ directory, compiles them into index.html,
and stages changes for git/Vercel.
"""

import os
import re
import json
import shutil
import subprocess
from pathlib import Path

# Paths
REPO_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = REPO_DIR / "content"
HTML_FILE = REPO_DIR / "index.html"
ROOT_WORKSPACE_HTML = Path("/home/bac/workspace/baset-pytopia.html")
DESKTOP_HTML = Path("/mnt/c/Users/Base/Desktop/baset-pytopia.html")

VAULT_DIR = Path(os.environ.get("VAULT_DIR", "/mnt/d/obsidian/obsidiainbrain/me/website"))

CATEGORY_THEMES = {
    "news": "card-theme-amber",
    "articles": "card-theme-violet",
    "tutorials": "card-theme-emerald",
    "telegram-bots": "card-theme-sky",
    "accounting": "card-theme-emerald",
    "web-apps": "card-theme-violet",
    "ai-workflows": "card-theme-amber",
    "tech-insights": "card-theme-rose"
}

CATEGORY_ICONS = {
    "news": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>',
    "articles": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>',
    "tutorials": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>'
}

def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    
    yaml_text = parts[1].strip()
    body = parts[2].strip()
    
    meta = {}
    current_key = None
    for line in yaml_text.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line and not line.startswith("-"):
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.split("#")[0].strip().strip('"').strip("'")
            if val.lower() == "true":
                meta[key] = True
            elif val.lower() == "false":
                meta[key] = False
            elif val == "":
                meta[key] = []
                current_key = key
            else:
                meta[key] = val
                current_key = None
        elif line.startswith("-") and current_key:
            item = line.lstrip("-").strip().strip('"').strip("'")
            if isinstance(meta.get(current_key), list):
                meta[current_key].append(item)
    return meta, body

def markdown_to_html(md_text):
    lines = md_text.split("\n")
    html_parts = []
    in_code_block = False
    code_lang = ""
    code_lines = []
    in_list = False
    list_type = None

    for line in lines:
        if line.startswith("```"):
            if in_code_block:
                in_code_block = False
                code_content = "\n".join(code_lines)
                html_parts.append(f"""
          <div class="code-syntax-block">
            <div class="code-syntax-header">
              <span>{code_lang or 'code'}</span>
              <button class="copy-snippet-btn" onclick="copySnippet(this)">کپی کد</button>
            </div>
            <pre class="code-syntax-body"><code>{code_content}</code></pre>
          </div>""")
                code_lines = []
            else:
                in_code_block = True
                code_lang = line[3:].strip()
            continue

        if in_code_block:
            code_lines.append(line.replace("<", "&lt;").replace(">", "&gt;"))
            continue

        stripped = line.strip()
        if not stripped:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            continue

        if stripped.startswith("### "):
            html_parts.append(f"<h3>{stripped[4:]}</h3>")
        elif stripped.startswith("## "):
            html_parts.append(f"<h2>{stripped[3:]}</h2>")
        elif stripped.startswith("# "):
            html_parts.append(f"<h1>{stripped[2:]}</h1>")
        elif stripped.startswith("> "):
            quote_text = stripped[2:].replace("**", "<strong>").replace("__", "<strong>")
            html_parts.append(f'<div class="callout-quote-box">{quote_text}</div>')
        elif re.match(r"^\d+\.\s", stripped):
            if not in_list or list_type != "ol":
                if in_list:
                    html_parts.append(f"</{list_type}>")
                html_parts.append("<ol>")
                in_list = True
                list_type = "ol"
            item_text = re.sub(r"^\d+\.\s*", "", stripped)
            html_parts.append(f"<li>{item_text}</li>")
        elif stripped.startswith("- ") or stripped.startswith("* "):
            if not in_list or list_type != "ul":
                if in_list:
                    html_parts.append(f"</{list_type}>")
                html_parts.append("<ul>")
                in_list = True
                list_type = "ul"
            item_text = stripped[2:]
            html_parts.append(f"<li>{item_text}</li>")
        else:
            if in_list:
                html_parts.append(f"</{list_type}>")
                in_list = False
            p_text = stripped.replace("**", "<strong>")
            html_parts.append(f"<p>{p_text}</p>")

    if in_list:
        html_parts.append(f"</{list_type}>")

    return "\n".join(html_parts)

def sync():
    print(f"[*] Checking Obsidian vault at: {VAULT_DIR}")
    if not VAULT_DIR.exists():
        print(f"[!] Warning: Vault directory not found: {VAULT_DIR}")
        return

    CONTENT_DIR.mkdir(parents=True, exist_ok=True)
    published_items = []

    # 1. Sync files from Vault into repo's content/ directory
    for md_file in sorted(VAULT_DIR.rglob("*.md")):
        if "templates" in md_file.parts or "drafts" in md_file.parts or md_file.name.lower() == "readme.md":
            continue

        # Relative path inside vault/website (e.g., news/realcompanion.md)
        rel_path = md_file.relative_to(VAULT_DIR)
        dest_file = CONTENT_DIR / rel_path
        dest_file.parent.mkdir(parents=True, exist_ok=True)

        shutil.copy2(md_file, dest_file)

        # Parse frontmatter
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        meta, body = parse_frontmatter(content)

        if not meta.get("published", False):
            continue

        slug = md_file.stem
        category = meta.get("category", md_file.parent.name)
        if category not in CATEGORY_THEMES:
            category = "news"

        title_fa = meta.get("title", slug)
        title_en = meta.get("titleEn", slug)
        date_shamsi = meta.get("dateShamsi", "امروز")
        date_gregorian = meta.get("dateGregorian", "Today")
        tags = meta.get("tags", ["Tech"])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]

        paragraphs = [p for p in body.split("\n\n") if p.strip() and not p.strip().startswith("#")]
        summary_fa = paragraphs[0].strip() if paragraphs else title_fa
        if len(summary_fa) > 160:
            summary_fa = summary_fa[:157] + "..."

        html_body = markdown_to_html(body)

        published_items.append({
            "id": slug,
            "type": "article",
            "category": category,
            "categoryClass": CATEGORY_THEMES.get(category, "card-theme-amber"),
            "dateShamsi": date_shamsi,
            "dateGregorian": date_gregorian,
            "tags": tags,
            "iconSvg": CATEGORY_ICONS.get(category, CATEGORY_ICONS["news"]),
            "titleFa": title_fa,
            "titleEn": title_en,
            "summaryFa": summary_fa,
            "summaryEn": summary_fa,
            "contentFa": html_body,
            "contentEn": html_body
        })

    print(f"[✓] Synced Markdown files into {CONTENT_DIR}")
    print(f"[✓] Found {len(published_items)} published article(s) to compile.")

    if not published_items:
        return

    # 2. Build JavaScript block
    js_items = []
    for item in published_items:
        tags_json = json.dumps(item["tags"], ensure_ascii=False)
        js_items.append(f"""      {{
        id: "{item['id']}",
        type: "{item['type']}",
        category: "{item['category']}",
        categoryClass: "{item['categoryClass']}",
        dateShamsi: "{item['dateShamsi']}",
        dateGregorian: "{item['dateGregorian']}",
        tags: {tags_json},
        iconSvg: '{item['iconSvg']}',
        titleFa: "{item['titleFa']}",
        titleEn: "{item['titleEn']}",
        summaryFa: "{item['summaryFa']}",
        summaryEn: "{item['summaryEn']}",
        contentFa: `
{item['contentFa']}
        `,
        contentEn: `
{item['contentEn']}
        `
      }}""")

    items_block = "    const directoryItems = [\n" + ",\n".join(js_items) + "\n    ];"

    # 3. Compile into HTML files
    for path in [HTML_FILE, ROOT_WORKSPACE_HTML]:
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                html = f.read()

            pattern = r'const directoryItems = \[.*?\];'
            new_html, count = re.subn(pattern, items_block, html, flags=re.DOTALL)
            if count > 0:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_html)
                print(f"[✓] Updated {path}")

    # Copy to Desktop
    if DESKTOP_HTML.parent.exists() and HTML_FILE.exists():
        shutil.copy2(HTML_FILE, DESKTOP_HTML)
        print(f"[✓] Desktop copy updated at {DESKTOP_HTML}")

if __name__ == "__main__":
    sync()
