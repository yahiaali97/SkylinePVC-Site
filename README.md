# موقع Skyline

## التشغيل
- دبل كليك على `start-server.bat` → هيفتح http://localhost:8080
  (محتاج Python أو Node.js متسطب على الجهاز).
- أو افتح `index.html` مباشرة في المتصفح.

## الملفات
- `index.html`, `about.html`, `projects.html`, `faq.html`, `contact.html` — صفحات الموقع
- `assets/js/projects-data.js` — بيانات الفيديوهات (المكان، العنوان، المواصفات). لإضافة فيديو جديد: ضيف عنصر هنا وحط صورته في `assets/projects/<id>.jpg`.
- `assets/projects/` — صور الفيديوهات (من صفحة فيسبوك الرسمية)
- `assets/logo.png` — اللوجو بخلفية شفافة (ونسخة `logo-dark.png` للوضع الداكن)، و`assets/logo-original.png` — الأصلي
- `tools/build.py` — بيعيد بناء الصفحات (الهيدر والفوتر المشتركين): `python tools/build.py`
