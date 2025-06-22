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

# نتابع فقط إذا تم رفع الملف
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if page == "📁 تحليل البيانات":
        st.subheader("📄 عرض البيانات:")
        st.dataframe(df)

        st.subheader("📊 ملخص إحصائي:")
        st.write(df.describe())

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

    elif page == "📤 التصدير":
        st.subheader("📥 تنزيل البيانات")

        # تحميل كـ CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("💾 تحميل كـ CSV", csv, "analysis.csv", "text/csv")

        # تحميل كـ Excel
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Analysis")
           
        excel_data = excel_buffer.getvalue()
        st.download_button("📊 تحميل كـ Excel", excel_data, "analysis.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

else:
    st.info("⬅️ الرجاء رفع ملف CSV لبدء التحليل.")