---
title: "افزایش سرعت مایکروسافت اج در ویندوز ۱۱ با معماری اجرای شتاب‌یافته (Accelerated App Launches)"
titleEn: "Microsoft Edge is Faster on Windows with Accelerated App Launches"
summaryFa: "مایکروسافت با پیاده‌سازی معماری جدید اجرای شتاب‌یافته در ویندوز ۱۱، سرعت باز شدن مرورگر اج را تا ۳۳٪ در شرایط تسک‌های سنگین افزایش داد و این قابلیت را به کرومیوم اهدا کرد."
summaryEn: "Microsoft Edge becomes the first browser to support Windows Accelerated App Launches, boosting launch speeds up to 33% under heavy multitasking and upstreaming the tech to Chromium."
dateShamsi: "۰۸ آبان ۱۴۰۵"
dateGregorian: "29 Oct 2026"
category: "news"
tags:
  - مایکروسافت
  - اج
  - ویندوز_۱۱
  - عملکرد
  - کرومیوم
  - معماری_سیستم
tagsEn:
  - "Microsoft Edge"
  - "Windows 11"
  - "Performance"
  - "Chromium"
  - "Architecture"
  - "Browser"
published: true
source: "https://blogs.windows.com/msedgedev/2026/10/29/edge-is-faster-on-windows-with-accelerated-app-launches/"
---

تیم توسعه‌دهنده مایکروسافت اج (Microsoft Edge) و ویندوز ۱۱ به تازگی اعلام کردند که مرورگر اج نخستین مرورگری در دنیاست که از قابلیت معماری جدید **«اجرای شتاب‌یافته اپلیکیشن‌ها» (Accelerated App Launches)** در ویندوز پشتیبانی می‌کند. این بهینه‌سازی سیستمی، سرعت باز شدن مرورگر را به طور میانگین **۱۵ درصد** و در سناریوهای مالتی‌تسکینگ سنگین تا **۳۳ درصد** افزایش می‌دهد.

این قابلیت از نسخه **Microsoft Edge 150 به بعد** و بر روی سیستم‌عامل‌های **ویندوز ۱۱ (نسخه‌های 25H2، 26H1 و 26H2)** همراه با به‌روزرسانی اکتبر ۲۰۲۶ (KB5127936) یا نسخه‌های جدیدتر فعال شده است.

![مرورگر مایکروسافت اج و عملکرد بهینه‌شده در ویندوز ۱۱](assets/msedge/edge-hero.webp)

## ۱. سازوکار سنتی اجرای مرورگر و مشکل پروسس‌های واسط

مرورگر اج مانند بسیاری از اپلیکیشن‌های مدرن ویندوز، در اغلب مواقع از پیش در سیستم در حال اجرا است؛ چه از طریق یک پنجره باز و چه در پس‌زمینه سیستم‌عامل به واسطه قابلیت‌هایی نظیر **Startup Boost**.

پیش از این، وقتی کاربر روی یک لینک کلیک می‌کرد یا آیکون اج را از روی تسک‌بار یا منوی استارت باز می‌کرد، ویندوز بلافاصله متوجه وضعیت مرورگر نمی‌شد. سیستم‌عامل ابتدا باید تشخیص می‌داد که آیا اج از قبل در حال اجرا است یا خیر. برای این کار:
1. ویندوز ابتدا یک **پروسس واسط کمکی (Intermediary Process)** ایجاد می‌کرد.
2. این پروسس در میان پروسس‌های در حال اجرای سیستم جستجو می‌کرد تا نمونه فعال مرورگر را پیدا کند.
3. در صورت یافتن پروسس فعال، درخواست باز شدن تب یا صفحه را به آن پروسس تحویل می‌داد.

![شکل ۱: ساختار سنتی اجرای مرورگر؛ ویندوز یک پروسس واسط برای جستجوی پروسس فعال باز می‌کرد](assets/msedge/diagram-extra-process.webp)

روی سیستمی که به تازگی روشن شده و تسک سنگینی ندارد، این تاخیر شاید نامحسوس باشد؛ اما در شرایط کاری واقعی، زمانی که سیستم زیر بار پردازش‌های متعدد، تب‌های سنگین یا نرم‌افزارهای مختلف است، ساخت همین پروسس واسط اضافی باعث مکث، کندی و احساس کند بودن باز شدن مرورگر می‌شد.

## ۲. معماری جدید: اجرای شتاب‌یافته (Accelerated App Launches)

در معماری جدید پیاده‌سازی‌شده با همکاری تیم هسته ویندوز:
- به محض اینکه نخستین پروسس اج در سیستم شروع به کار می‌کند، یک **درخواست ثبت‌نام (Registration Request)** به ویندوز ارسال می‌کند.
- ویندوز این درخواست را تایید و در جدول پروسس‌های شتاب‌یافته ثبت می‌کند.
- از این لحظه به بعد، هر بار که کاربر روی لینکی کلیک کند، از منوی استارت یا از تسک‌بار اج را باز کند، ویندوز بدون نیاز به ساخت هیچ پروسس واسطی، **مستقیماً پروسس اصلی در حال اجرای اج را مطلع می‌سازد**.

![شکل ۲: ساختار جدید اجرای شتاب‌یافته؛ ویندوز با اطلاع‌رسانی مستقیم به پروسس فعال، تاخیر را حذف می‌کند](assets/msedge/diagram-accelerated-launch.webp)

این ارتباط مستقیم، گلوگاه‌های ساخت پروسس در تسک‌بار و منوی استارت را به طور کامل از بین می‌برد و عملکرد روان مرورگر را حتی در بالاترین فشارهای پردازشی تضمین می‌کند.

## ۳. اهدای این معماری به پروژه متن‌باز کرومیوم (Chromium)

نکته تحسین‌برانگیز در این به‌روزرسانی این است که مایکروسافت این دستاورد مهندسی را تنها برای اج انحصاری نگه نداشته است. مایکروسافت کدهای مربوط به این قابلیت را به پروژه متن‌باز **کرومیوم (Chromium)** اهدا کرده است تا در آینده سایر مرورگرهای مبتنی بر کرومیوم (نظیر گوگل کروم، بریو، ویوالدی و اوپرا) نیز بتوانند در ویندوز ۱۱ از قابلیت اجرای شتاب‌یافته بهره‌مند شوند.

علاوه بر این، مایکروسافت اعلام کرده است که در حال گسترش این سازوکار به سناریوهای دیگر نظیر باز کردن فایل‌های PDF و اپلیکیشن‌های مستقل ویندوز است. توسعه‌دهندگان نرم‌افزارهای تحت ویندوز نیز می‌توانند با استفاده از API مربوطه، قابلیت اجرای شتاب‌یافته را در برنامه‌های شخصی خود فعال کنند.

---
📎 **منبع رسمی خبر در وبلاگ توسعه‌دهندگان مایکروسافت ویندوز:**  
[https://blogs.windows.com/msedgedev/2026/10/29/edge-is-faster-on-windows-with-accelerated-app-launches/](https://blogs.windows.com/msedgedev/2026/10/29/edge-is-faster-on-windows-with-accelerated-app-launches/)

<!-- english -->

Microsoft has announced that Microsoft Edge is the first browser in the world to support **Accelerated App Launches** on Windows, delivering a significantly faster and more consistent launch experience.

With accelerated app launches enabled, Windows users experience a **15% average launch speed improvement**, with performance gains scaling up to **33% under heavy multitasking scenarios**.

This enhancement is rolled out starting with **Microsoft Edge version 150+** and is supported on **Windows 11 (versions 25H2, 26H1, and 26H2)** with the October 2026 non-security update (KB5127936) or later.

![Microsoft Edge browser on Windows 11](assets/msedge/edge-hero.webp)

## 1. The Bottleneck: Intermediary Process Spawning

Edge, like many modern Windows applications, is frequently already running on a machine—either through a visible open window or dormant in the background via mechanisms like **Startup Boost**.

Previously, when launching Edge from the Taskbar, the Start menu, or by clicking a web hyperlink:
1. Windows could not instantly determine if a live Edge process was already resident in memory.
2. To resolve this, Windows was forced to spawn an **intermediary process**.
3. This helper process searched through the active process table, located the running browser instance, and forwarded the request before terminating.

![Figure 1: Legacy launch workflow spawning an extra intermediary process](assets/msedge/diagram-extra-process.webp)

While virtually imperceptible on an idle machine, under heavy real-world multitasking—where CPU and I/O scheduler queues are saturated—creating this extra intermediary process introduced tangible input lag and perceived stutter.

## 2. The Architectural Solution: Direct Notification

Through close co-engineering between the Edge and Windows kernel teams, the new Accelerated App Launch framework streamlines the launch path:
- When an Edge process initializes, it registers an **accelerated-launch notification token** with Windows.
- Windows verifies and records this registration.
- For all subsequent invocations, Windows bypasses intermediary process creation entirely and **directly signals the existing Edge instance**.

![Figure 2: Modern accelerated launch workflow directly notifying the running Edge process](assets/msedge/diagram-accelerated-launch.webp)

This eliminates redundant process creation overhead, dramatically reducing latency across the Taskbar, Start Menu, and default URL protocol handlers.

## 3. Contributing Upstream to Chromium

Crucially, Microsoft is not keeping this optimization proprietary. The engineering team is contributing this implementation upstream to the open-source **Chromium project**, enabling other Chromium-based browsers (including Google Chrome, Brave, and Opera) to take advantage of Windows accelerated launches in future releases.

Furthermore, Microsoft is actively expanding this capability across Windows workflows, including default PDF handler invocations, and has published developer APIs allowing third-party Windows desktop software to register for accelerated launches.

---
📎 **Official Article on Windows Experience Blog:**  
[https://blogs.windows.com/msedgedev/2026/10/29/edge-is-faster-on-windows-with-accelerated-app-launches/](https://blogs.windows.com/msedgedev/2026/10/29/edge-is-faster-on-windows-with-accelerated-app-launches/)
