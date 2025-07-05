<!-- 🌐 اللغة -->
🇬🇧 English version available [here](README.en.md)

<!-- 🖼️ شعار المشروع -->
![Joseph Empire Preview](assets/joseph-empire-preview.png)

<!-- 🎯 الشارات -->
<p align="center">
  <a href="https://github.com/AhmedEltayfy/data-analysis-devops/actions">
    <img alt="CI" src="https://github.com/AhmedEltayfy/data-analysis-devops/actions/workflows/devops-ci.yml/badge.svg">
  </a>
  <a href="assets/BudgetAnalyzer_Documentation_AhmedELTayfy.pdf">
    <img alt="Docs" src="https://img.shields.io/badge/docs-PDF-blue">
  </a>
  <a href="https://data-analysis-devops-ajjiwigrbjayb86vtzed6e.streamlit.app">
    <img alt="Streamlit" src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg">
  </a>
</p>

📚 [عرض التوثيق على GitHub Wiki](../../wiki)
📦 [نشر التطبيق على Render](https://github.com/AhmedEltayfy/data-analysis-devops/wiki/🔧-نشر-التطبيق-على-Render)

# 💰 Budget Analyzer | تحليل الميزانية 📊

تطبيق تفاعلي باستخدام Streamlit يساعدك على تحليل ميزانيتك بطريقة احترافية وسريعة.

---

## 🚀 رابط مباشر للتجربة

[🔗 تشغيل التطبيق الآن](https://data-analysis-devops-ajjiwigrbjayb86vtzed6e.streamlit.app)

📎 لعرض تقديمي سريع:  
[🎥 عرض تقديمي (Demo Mode)](https://data-analysis-devops-ajjiwigrbjayb86vtzed6e.streamlit.app/?mode=demo)

---

## 🧩 الميزات

- 📂 تحميل ملفات CSV وتحليلها فورًا  
- 🧪 بيانات تجريبية افتراضية عند غياب الملف  
- 🖼️ صفحة ترحيب أنيقة بشعار وشروحات  
- 🔁 زر تجربة البيانات التجريبية بسهولة  
- 🧹 زر لإعادة ضبط الجلسة دون إعادة تحميل الصفحة  
- 📈 رسوم بيانية مخصصة باستخدام Plotly  
- 💾 تصدير البيانات كـ CSV / Excel  
- 🧾 توليد تقرير PDF تلقائي من التحليل  
- 🎥 عرض تقديمي يُخفي الشريط الجانبي لعرض النتائج فقط  
- 🎨 تخصيص ألوان الرسوم البيانية لواجهة جذابة  

---

## 🖼️ لقطة من التطبيق

![واجهة التطبيق](assets/screenshot.png)

---

## 🛠️ طريقة التشغيل المحلي

```bash
git clone https://github.com/AhmedEltayfy/data-analysis-devops.git
cd data-analysis-devops
pip install -r requirements.txt
streamlit run streamlit_app.py