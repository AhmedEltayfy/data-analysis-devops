# 📓 Changelog — Budget Analyzer App

## [v1.2.0] - 2025-06-21
### Added
- تبويب متعدد الصفحات باستخدام `st.sidebar.radio`
- مخطط خطي متعدد الأعمدة باستخدام Plotly
- حساب نسبة نمو الإيرادات شهريًا
- زر تصدير النتائج إلى ملفات Excel وCSV

### Fixed
- خطأ `NameError: name 'df' is not defined` عن طريق تحريك المتغير داخل شرط `uploaded_file`
- مشكلة `xlsxwriter` بعدم وجود `.save()` داخل الـ context

---

## [v1.1.0] - 2025-06-20
### Added
- الواجهة التفاعلية بـ Streamlit
- تحميل ملفات CSV من خلال `st.file_uploader`
- عرض المخطط التفاعلي باستخدام `plotly.express.bar`

### Fixed
- خطأ تشغيل بسبب امتداد خاطئ `streamlit.app.py` → أعيدت تسميته إلى `streamlit_app.py`
- عدم وجود مكتبة matplotlib → تم تثبيتها يدويًا

---

## [v1.0.0] - 2025-06-20
### Created
- مستودع Git وتحضيره باستخدام Git Bash
- رفع ملفات البيانات والتحليل إلى GitHub
- إعداد GitHub Actions لتشغيل `analysis_script.py` تلقائيًا
