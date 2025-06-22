import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="تحليل الميزانية", page_icon="📊", layout="wide")

st.title("💰 Budget Analyzer App")

# ---------------------- الشريط الجانبي ----------------------

st.sidebar.title("🔧 إعدادات التطبيق")

uploaded_file = st.sidebar.file_uploader("⬆️ حمّل ملف الميزانية (CSV)", type="csv")

page = st.sidebar.radio("📂 اختر الصفحة", ["📁 تحليل البيانات", "📈 الرسوم البيانية", "📤 التصدير"])

st.sidebar.markdown("---")

if st.sidebar.button("🧹 مسح البيانات الحالية وإعادة التشغيل"):
    st.session_state.clear()
    st.rerun()

# --------------------- إدارة الحالة والبيانات ----------------------

# زر جرّب البيانات التجريبية
if "use_demo_data" not in st.session_state:
    st.session_state.use_demo_data = True

if uploaded_file is None and st.button("🔁 جرّب البيانات التجريبية من جديد"):
    st.session_state.use_demo_data = True

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("📂 تم رفع الملف بنجاح!")
    st.session_state.use_demo_data = False

elif st.session_state.use_demo_data:
    st.warning("⚠️ لم يتم رفع ملف — سيتم استخدام بيانات تجريبية.")
    df = pd.DataFrame({
        "Month": ["يناير", "فبراير", "مارس", "أبريل"],
        "Revenue": [12000, 14500, 16000, 13800],
        "Expenses": [7000, 8500, 9000, 7800]
    })
    st.info("✅ تعمل الآن على بيانات تجريبية — يمكنك رفع ملفك الخاص في أي وقت.")

else:
    st.info("⬅️ الرجاء رفع ملف CSV لبدء التحليل.")
    st.stop()

# --------------------- تبويب: تحليل البيانات ----------------------

if page == "📁 تحليل البيانات":
    st.subheader("📄 عرض البيانات:")
    st.dataframe(df)

    st.subheader("📊 ملخص إحصائي:")
    st.write(df.describe())

# --------------------- تبويب: الرسوم البيانية ----------------------

elif page == "📈 الرسوم البيانية":
    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) >= 2:
        st.subheader("📈 رسم بياني تفاعلي")
        x_axis = st.selectbox("اختر المحور X", numeric_cols)
        y_axis = st.selectbox("اختر المحور Y", numeric_cols, index=1)
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} حسب {x_axis}")
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ لا توجد أعمدة رقمية كافية للرسم البياني.")

    st.subheader("📉 تحليل النمو الشهري")

    if "Month" in df.columns and "Revenue" in df.columns:
        df_sorted = df.sort_values("Month")
        df_sorted["نمو الإيرادات (%)"] = df_sorted["Revenue"].pct_change().fillna(0) * 100
        st.line_chart(df_sorted.set_index("Month")[["Revenue", "نمو الإيرادات (%)"]])
        st.dataframe(df_sorted[["Month", "Revenue", "نمو الإيرادات (%)"]])
    else:
        st.info("📌 أضف عمودي 'Month' و 'Revenue' لتحليل النمو الشهري.")

# --------------------- تبويب: التصدير ----------------------

elif page == "📤 التصدير":
    st.subheader("📥 تنزيل البيانات")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("💾 تحميل كـ CSV", csv, "analysis.csv", "text/csv")

    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Analysis")

    excel_data = excel_buffer.getvalue()
    st.download_button("📊 تحميل كـ Excel", excel_data, "analysis.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
