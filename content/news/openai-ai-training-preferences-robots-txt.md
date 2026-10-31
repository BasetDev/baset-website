---
title: "توافق OpenAI، گوگل و مایکروسافت برای یکپارچه‌سازی ترجیحات آموزش هوش مصنوعی در robots.txt"
titleEn: "Making it Easier for Websites to Express AI Training Preferences (OpenAI, Google & Microsoft)"
summaryFa: "OpenAI با همراهی گوگل و مایکروسافت از پشتیبانی یک سیگنال واحد در فایل robots.txt برای اعلام عدم تمایل به آموزش مدل‌های هوش مصنوعی خبر داد."
summaryEn: "OpenAI, Google, and Microsoft announce voluntary support for a unified robots.txt signal allowing publishers to set AI training preferences across providers."
dateShamsi: "۰۹ آبان ۱۴۰۵"
dateGregorian: "30 Oct 2026"
category: "news"
tags:
  - هوش_مصنوعی
  - اوپن_ای_آی
  - ربات_تکست
  - گوگل
  - مایکروسافت
  - حریم_خصوصی
tagsEn:
  - "OpenAI"
  - "Robots.txt"
  - "AI Training"
  - "Google"
  - "Microsoft"
  - "Web Standards"
published: true
source: "https://openai.com/index/helping-websites-express-ai-training-preferences/"
---

شرکت **OpenAI** به همراه **مایکروسافت** و **گوگل** از ابتکار مشترکی برای ساده‌سازی فرآیند اعلام ترجیحات وب‌سایت‌ها در زمینه آموزش مدل‌های هوش مصنوعی رونمایی کردند. بر اساس این توافق داوطلبانه، شرکت‌های ارائه‌دهنده هوش مصنوعی یک **سیگنال واحد و مشترک در فایل `robots.txt`** را به رسمیت خواهند شناخت.

تا پیش از این، مدیران وب‌سایت‌ها و ناشران محتوا مجبور بودند برای تک‌تک خزنده‌ها و ربات‌های هوش مصنوعی (نظیر GPTBot، Google-Extended، CCBot و غول‌های دیگر) قوانین و خطوط جداگانه‌ای در فایل robots.txt بنویسند و مرتباً این لیست طولانی را به‌روزرسانی کنند.

![توافق OpenAI، مایکروسافت و گوگل بر سر سیگنال واحد robots.txt برای ترجیحات آموزش هوش مصنوعی](assets/openaipref/hero.webp)

## ۱. چرا صنعت هوش مصنوعی به یک سیگنال مشترک نیاز داشت؟

با رشد انفجاری مدل‌های زبانی بزرگ، تعداد خزنده‌های جمع‌آوری داده به ده‌ها مورد رسید. برای یک ناشر یا وبمستر، پایش اینکه کدام ربات متعلق به کدام شرکت است و نوشتن دستورات عدم دسترسی (Disallow) برای هر یک از آن‌ها به یک سردرد فنی و مدیریتی تبدیل شده بود.

سیگنال مشترک جدید این فرآیند را یکپارچه می‌کند:
- **یکبار تنظیم برای همه:** وب‌سایت‌ها با تنظیم یک دستور مشترک در فایل `robots.txt`، ترجیح خود را به صورت همزمان به تمام شرکت‌های ارائه‌دهنده هوش مصنوعی مشارکت‌کننده اعلام می‌کنند.
- **کاهش اصطکاک وبمسترها:** حذف نیاز به شناسایی دستی خزنده‌های جدید و پیگیری تغییر نام بات‌ها.
- **توافق میان غول‌های فناوری:** همکاری OpenAI، گوگل و مایکروسافت نشان‌دهنده شکل‌گیری یک استاندارد صنعتی پذیرفته‌شده است.

## ۲. همگام با استاندارد گروه کاری IETF

این اقدام داوطلبانه برگرفته از تلاش‌های در حال انجام در **کارگروه ترجیحات هوش مصنوعی (AIPREF)** در سازمان بین‌المللی مهندسی اینترنت (**IETF**) است. 

OpenAI اعلام کرده است که با پیوستن به این ابتکار مشترک، تعهد خود را به مشارکت در تدوین استانداردهای جهانی وب برای تعامل سایت‌ها و مدل‌های مولد تقویت می‌کند و سایر توسعه‌دهندگان و شرکت‌های حوزه AI را نیز به احترام به این سیگنال مشترک فراخوانده است.

## ۳. تکلیف ابزارهای کنترلی فعلی چیست؟

نکته کلیدی در این اعلامیه این است که **سیگنال مشترک جایگزین کنترل‌های قبلی نخواهد شد، بلکه مکمل آن‌هاست:**
- اگر سایتی بخواهد قوانین تفکیک‌شده‌تری داشته باشد (مثلاً اجازه جستجو به ربات بدهد اما آموزش مدل فونداسیون را مسدود کند)، خزنده‌های تفکیک‌شده مثل `GPTBot` و `OAI-SearchBot` همچنان به کار خود ادامه می‌دهند و به دستورات اختصاصی احترام می‌گذارند.
- پیاده‌سازی این سیگنال مشترک در ماه‌های آینده توسط OpenAI عملیاتی خواهد شد و گوگل نیز اعلام کرده است که در سال ۲۰۲۷ به طور کامل از این کنترل مشترک پشتیبانی خواهد کرد.

---
📎 **منبع رسمی خبر در وب‌سایت رسمی OpenAI:**  
[https://openai.com/index/helping-websites-express-ai-training-preferences/](https://openai.com/index/helping-websites-express-ai-training-preferences/)

<!-- english -->

OpenAI, in collaboration with Google and Microsoft, has announced support for a **common, unified signal in `robots.txt`**, allowing websites and publishers to easily express their preferences regarding the use of their content for foundational generative AI training.

Historically, web operators were forced to research dozens of separate crawler user-agents (such as GPTBot, Google-Extended, and others) and maintain sprawling, fragmented disallow rules across their configurations.

![OpenAI, Microsoft and Google standardizing AI training preferences in robots.txt](assets/openaipref/hero.webp)

## 1. Why a Unified AI Preferences Signal Matters

The rapid proliferation of generative AI crawlers created unsustainable operational friction for web publishers. Website operators had to independently track emerging scrapers and update disallow lists perpetually.

The shared signal streamlines this dynamic:
- **Configure Once for Multiple Providers:** Publishers communicate a uniform preference to all participating AI model providers simultaneously.
- **Reduced Maintenance Overhead:** Eliminates the burden of tracking individual bot user-agents and protocol variations.
- **Industry Coalition:** Endorsement by OpenAI, Microsoft, and Google establishes a robust consensus foundation.

## 2. Anchored in IETF Standards Work

This voluntary initiative builds directly upon the ongoing efforts of the **Internet Engineering Task Force (IETF) AI Preferences (AIPREF) working group**. 

OpenAI emphasized that participating in this shared signal advances its long-term commitment to open web standards, urging other AI providers and crawling organizations to adopt and respect the common signal.

## 3. Coexistence with Existing Crawler Controls

The introduction of a common signal does not deprecate existing granular crawler controls:
- Established bot-specific directives (e.g., granular disallow rules for `GPTBot` vs. `OAI-SearchBot`) remain fully operational and respected.
- Publishers retain complete flexibility to permit real-time search indexing while restricting foundational pre-training.
- OpenAI plans to roll out implementation of the signal in the coming months, while Google has committed to full operational integration by 2027.

---
📎 **Official Announcement on OpenAI Index:**  
[https://openai.com/index/helping-websites-express-ai-training-preferences/](https://openai.com/index/helping-websites-express-ai-training-preferences/)
