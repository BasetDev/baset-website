---
title: "چرا بنچمارک‌های حافظه در هوش مصنوعی ما را سر کار گذاشته‌اند؟ (تحلیل RealCompanion)"
titleEn: "Why AI Memory Benchmarks Mislead Us: Analysis of the RealCompanion Study"
summaryFa: "تحلیل ۲۷ هزار پیام واقعی نشان می‌دهد پنجره پیام‌های اخیر جواب ۹۵.۹٪ پیام‌ها را دارد، اما برای حافظه بلندمدت کارایی تا ۲.۲٪ سقوط می‌کند!"
summaryEn: "Analysis of 27k real-world chat messages reveals recency windows cover 95.9% of queries, but true long-term retrieval plunges to 2.2%."
dateShamsi: "۱۴ مهر ۱۴۰۵"
dateGregorian: "05 Oct 2026"
category: "news"
tags:
  - هوش_مصنوعی
  - ماشین_لرنینگ
  - بنچمارک
  - معماری_نرم_افزار
  - RAG
  - RealCompanion
tagsEn:
  - "AI Memory"
  - "Machine Learning"
  - "Benchmark"
  - "Software Architecture"
  - "RAG"
  - "RealCompanion"
published: true
source: "https://arxiv.org/abs/2610.01780"
---

خیلی از بنچمارک‌های حافظه در هوش مصنوعی ما را سر کار گذاشته‌اند، چون روی داده‌های مصنوعی و سوالات ساختگی تست می‌شوند نه مکالمات واقعی انسان‌ها.

به تازگی پژوهشگران در مقاله‌ای به نام **RealCompanion** دست به کار متفاوتی زدند: تحلیل **۲۷,۲۱۸ پیام واقعی** بین ده کاربر و ربات هوش مصنوعی در طول ۱۲۰ روز، همراه با استدلال مرحله‌به‌مرحله برای هر برچسب داده.

## سه نتیجه فنی جالب از تحلیل داده‌ها

1. **خطای پنجره پیام‌های اخیر (Recency Window):**
   پنجره پیام‌های اخیر جواب ۹۵.۹ درصد پیام‌ها را در خود دارد، اما برای پیام‌هایی که واقعاً به حافظه دور نیاز دارند، کارایی این پنجره تا ۲.۲ درصد سقوط می‌کند. در واقع ۹۶ درصد بهره‌ای که از بازیابی حافظه می‌بینیم، ناشی از پیام‌هایی است که اصلاً نیازی به حافظه دور نداشتند!

2. **عدم توانایی مدل‌ها در تشخیص زمان بازیابی:**
   هیچ مدلی نتوانست در مکالمه واقعی تشخیص دهد «چه زمانی» به سراغ حافظه گذشته برود. در بنچمارک‌های قبلی، خود سوالات مصنوعی سرنخ را لو می‌دادند.

3. **۳۱ برابر اختلاف هزینه با بازدهی یکسان:**
   سه سیستم معماری مختلف برای بازسازی پرسونا تست شدند و هر سه به امتیاز F1 دقیقاً یکسانی رسیدند؛ اما با ۳۱ برابر اختلاف هزینه در مصرف توکن!

> **سوال برای معماران سیستم:**  
> وقتی معیارهای تجمیعی این‌قدر گمراه‌کننده‌اند، شما در عمل چطور بازدهی سیستم‌های حافظه یا RAG را اندازه می‌گیرید؟

---
📎 **منبع مقاله در arXiv:** [https://arxiv.org/abs/2610.01780](https://arxiv.org/abs/2610.01780)

<!-- english -->

Many AI memory benchmarks are fundamentally misleading because they are tested against synthetic data and contrived queries rather than natural, longitudinal human conversations.

Recently, researchers behind the **RealCompanion** paper took a radically different approach: analyzing **27,218 real-world messages** exchanged between 10 users and AI companions over 120 days, backed by step-by-step reasoning annotations.

## Three Key Technical Takeaways

1. **The Recency Window Fallacy:**  
   Recent message windows resolve 95.9% of user inquiries. However, for queries genuinely requiring long-term memory, recency window accuracy plunges down to 2.2%. In essence, 96% of perceived memory retrieval success originates from interactions that never demanded historical context in the first place!

2. **Inability to Decide 'When' to Retrieve:**  
   No LLM was able to reliably deduce 'when' to trigger historical memory lookups in organic conversations. In prior benchmarks, the synthetic questions themselves inadvertently signaled memory needs.

3. **Identical F1 Score at 31x Token Cost:**  
   Three disparate architectural paradigms were evaluated for persona reconstruction. All three attained identical F1 performance metrics—despite a staggering 31-fold difference in token consumption expense!

> **Question for System Architects:**  
> With aggregate metrics proving so deceptive, how do you evaluate production memory systems or RAG pipelines in real deployments?

---
📎 **Paper on arXiv:** [https://arxiv.org/abs/2610.01780](https://arxiv.org/abs/2610.01780)
