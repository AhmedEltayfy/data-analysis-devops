import streamlit as st
import pandas as pd
import plotly.express as px
import io
from fpdf import FPDF
from pandas.api.types import CategoricalDtype

# إعداد الصفحة
st.set_page_config(
    page_title="📊 تحليل الميزانية - Budget Analyzer",
    page_icon="assets/favicon.ico",
    layout="wide"
)

st.title("💰 Budget Analyzer App")

# تعريف مبكر لتفادي الأخطاء لاحقًا
uploaded_file = None
df = None

# ========== عرض تقديمي أم لا ==========
is_demo_mode = st.query_params.get("mode") == "demo"

# ========== الشريط الجانبي ==========
if not is_demo_mode:
    st.sidebar.title("🔧 إعدادات التطبيق")
    uploaded_file = st.sidebar.file_uploader("⬆️ حمّل ملف الميزانية (CSV)", type="csv")
    page = st.sidebar.radio("📂 اختر الصفحة", [
        "🏠 الصفحة الرئيسية",
        "📁 تحليل البيانات",
        "📈 الرسوم البيانية",
        "📤 التصدير"
    ])
    st.sidebar.markdown("---")
    if st.sidebar.button("🧹 مسح البيانات الحالية وإعادة التشغيل"):
        st.session_state.clear()
        st.rerun()
else:
    page = "📈 الرسوم البيانية"

# ========== الصفحة الترحيبية ==========
if page == "🏠 الصفحة الرئيسية":
    st.markdown("""
        <div style='text-align: center;'>
            <img src="assets/logo.png" width="120" />
            <h1>👋 أهلاً بك في تطبيق <span style='color:#4CAF50;'>Budget Analyzer</span></h1>
            <p style='font-size:18px;'>حلّل ميزانيتك، استخرج الرسوم، وصدّر النتائج — في أقل من دقيقة!</p>
            <a href="?page=📁+تحليل+البيانات"><button style='padding:10px 20px;'>ابدأ الآن 🚀</button></a>
            <br><br>
            <a href="?mode=demo"><button style='padding:8px 16px;background-color:#555;color:#fff;'>عرض تقديمي (Demo Mode) 🎥</button></a>
        </div>
    """, unsafe_allow_html=True)
    st.stop()

# ========== تحميل البيانات ==========
if "use_demo_data" not in st.session_state:
    st.session_state.use_demo_data = True

if not is_demo_mode:
    if uploaded_file is None and st.button("🔁 جرّب البيانات التجريبية من جديد"):
        st.session_state.use_demo_data = True

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state["last_df"] = df
    st.success("📂 تم رفع الملف بنجاح!")
    st.session_state.use_demo_data = False
elif "last_df" in st.session_state:
    df = st.session_state["last_df"]
    st.info("📦 جاري استخدام الملف المرفوع سابقًا")
elif st.session_state.use_demo_data:
    df = pd.DataFrame({
        "Month": ["يناير", "فبراير", "مارس", "أبريل"],
        "Revenue": [12000, 14500, 16000, 13800],
        "Expenses": [7000, 8500, 9000, 7800]
    })
    st.info("✅ تعمل الآن على بيانات تجريبية — يمكنك رفع ملفك الخاص في أي وقت.")
else:
    st.warning("⚠️ لم يتم تحميل أو إنشاء بيانات بعد.")
    st.stop()

# ========== تحليل البيانات ==========
if page == "📁 تحليل البيانات":
    st.subheader("📄 عرض البيانات:")
    st.dataframe(df)

    st.subheader("📊 ملخص إحصائي:")
    st.write(df.describe())

# ========== الرسوم البيانية ==========
elif page == "📈 الرسوم البيانية":
    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) >= 2:
        st.subheader("📈 رسم بياني تفاعلي")
        x_axis = st.selectbox("اختر المحور X", numeric_cols)
        y_axis = st.selectbox("اختر المحور Y", numeric_cols, index=1)
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} حسب {x_axis}")
        fig.update_traces(marker_color='#4CAF50')
        st.plotly_chart(fig)
    else:
        st.warning("⚠️ لا توجد أعمدة رقمية كافية.")

    # ترتيب الأشهر في حالة وجود تحليل شهري
    if "Month" in df.columns and "Revenue" in df.columns:
        month_order = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو",
                       "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"]
        df["Month"] = df["Month"].astype(CategoricalDtype(categories=month_order, ordered=True))
        df_sorted = df.sort_values("Month")
        df_sorted["نمو الإيرادات (%)"] = df_sorted["Revenue"].pct_change().fillna(0) * 100

        st.subheader("📉 تحليل النمو الشهري")
        st.line_chart(df_sorted.set_index("Month")[["Revenue", "نمو الإيرادات (%)"]])
        st.dataframe(df_sorted[["Month", "Revenue", "نمو الإيرادات (%)"]])
    else:
        st.info("📌 أضف عمودي 'Month' و 'Revenue' لتحليل النمو.")

# ========== التصدير ==========
elif page == "📤 التصدير":
    st.subheader("📥 تنزيل البيانات")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("💾 تحميل كـ CSV", csv, "analysis.csv", "text/csv")

    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Analysis")
    st.download_button("📊 تحميل كـ Excel", excel_buffer.getvalue(), "analysis.xlsx")

    st.subheader("🧾 تقرير PDF")
    
    def dataframe_to_pdf(df):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        col_width = 190 / len(df.columns)
        for col in df.columns:
            pdf.cell(col_width, 10, str(col), border=1)
        pdf.ln()
        for _, row in df.iterrows():
            for val in row:
                pdf.cell(col_width, 10, str(val), border=1)
            pdf.ln()
        return pdf.output(dest="S").encode("latin1")

    pdf_bytes = dataframe_to_pdf(df)
    st.download_button("📄 تحميل كـ PDF", pdf_bytes, "budget_report.pdf", "application/pdf")
