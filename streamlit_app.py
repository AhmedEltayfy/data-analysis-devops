import streamlit as st
import pandas as pd
import plotly.express as px
import io
import xlsxwriter

st.set_page_config(page_title="📊 لوحة تحكم الميزانية", layout="wide")
st.title("📁 تطبيق تحليل الميزانية")

# تبويب متعدد الصفحات
page = st.sidebar.radio("📂 اختر الصفحة", ["📁 تحليل البيانات", "📈 الرسوم البيانية", "📤 التصدير"])

# تحميل الملف
uploaded_file = st.sidebar.file_uploader("⬆️ حمّل ملف الميزانية (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("📂 تم رفع الملف بنجاح!")
else:
    st.warning("⚠️ لم يتم رفع ملف بعد — سيتم استخدام بيانات تجريبية.")
    df = pd.DataFrame({
        "Month": ["يناير", "فبراير", "مارس", "أبريل"],
        "Revenue": [12000, 14500, 16000, 13800],
        "Expenses": [7000, 8500, 9000, 7800]
    })
    st.info("✅ تعمل الآن على بيانات تجريبية — يمكنك رفع ملفك الخاص في أي وقت.")
