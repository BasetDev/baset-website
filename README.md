# Baset | Personal Portfolio & Tech Directory

A minimalist, high-performance personal portfolio and tech directory for **Baset**, inspired by **yazdan.me** and **Pytopia**.

100% database-free, statically compiled, and deployed on [Vercel](https://vercel.com).

---

## ✍️ Content Authoring (Obsidian Workflow)

Content is authored inside an **Obsidian vault** at `D:\obsidian\obsidiainbrain\me\website` and synced into the repository's `content/` directory via an automated synchronization script.

### Obsidian Directory Structure:
```text
D:\obsidian\obsidiainbrain\me\website\
├── news/                  # اخبار هوش مصنوعی، فناوری و تلگرام
├── articles/              # مقالات تحلیلی، معماری و سیستم‌ها
├── tutorials/             # آموزش‌های گام‌به‌گام برنامه‌نویسی
├── drafts/                # پیش‌نویس‌ها و ایده‌ها (در سایت منتشر نمی‌شوند)
└── templates/             # قالب آماده نوت جدید (post-template.md)
```

### Frontmatter Standard:
```yaml
---
title: "عنوان یادداشت یا خبر"
titleEn: "Note Title in English"
dateShamsi: "۱۵ مهر ۱۴۰۴"
dateGregorian: "07 Oct 2025"
category: "news" # news | articles | tutorials
tags: ["AI", "Tech"]
published: true # Only notes with published: true appear on the live site
---
```

---

## 🔄 Automated Synchronization

Run the sync script to pull changes from the Obsidian vault, mirror Markdown files into `content/`, and compile the website:

```bash
python3 scripts/sync-obsidian.py
```

---

## 🚀 Deployment

The repository is pre-configured for instant zero-configuration deployment to **Vercel**:
- Root directory: `./`
- Output: `index.html` (Zero-DB Static Jamstack)
- Security: Configured via `vercel.json`
