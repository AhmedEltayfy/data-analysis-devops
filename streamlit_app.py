import streamlit as st
import pandas as pd
import plotly.express as px
import io

# إعداد الواجهة
st.set_page_config(
    page_title="📊 تحليل الميزانية - Budget Analyzer",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Budget Analyzer App")

# الكشف عن وضع العرض التقديمي
is_demo_mode = st.query_params.get("mode") == "demo"

# ---------------------- الشريط الجانبي ----------------------

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

# ---------------------- الصفحة الترحيبية ----------------------

if page == "🏠 الصفحة الرئيسية":
    st.markdown("""
        <div style='text-align: center;'>
            <h1>👋 أهلاً بك في تطبيق <span style='color:#4CAF50;'>Budget Analyzer</span></h1>
            <p style='font-size:18px;'>حلّل ميزانيتك، استخرج الرسوم، وصدّر النتائج — في أقل من دقيقة!</p>
            <img src="https://media.giphy.com/media/3oEdv3Ul4nUtxmw5Qw/giphy.gif" width="400"/>
            <br><br>
            <a href="?page=📁+تحليل+البيانات"><button style='padding:10px 20px;font-size:16px;'>ابدأ الآن 🚀</button></a>
            <br><br>
            <a href="?mode=demo"><button style='padding:8px 16px;font-size:14px;background-color:#555;color:#fff;'>عرض تقديمي (Demo Mode) 🎥</button></a>
        </div>
    """, unsafe_allow_html=True)
    st.stop()

# ---------------------- إدارة البيانات ----------------------

if "use_demo_data" not in st.session_state:
    st.session_state.use_demo_data = True

uploaded_file = None if is_demo_mode else st.session_state.get("uploaded_file")

if not is_demo_mode:
    if "uploaded_file" not in st.session_state and 'file_uploader' in st.session_state:
        uploaded_file = st.session_state["file_uploader"]

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

# ---------------------- تحليل البيانات ----------------------

if page == "📁 تحليل البيانات":
    st.subheader("📄 عرض البيانات:")
    st.dataframe(df)

    st.subheader("📊 ملخص إحصائي:")
    st.write(df.describe())

# ---------------------- الرسوم البيانية ----------------------

elif page == "📈 الرسوم البيانية":
    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) >= 2:
        st.subheader("📈 رسم بياني تفاعلي")
        x_axis = st.selectbox("اختر المحور X", numeric_cols)
        y_axis = st.selectbox("اختر المحور Y", numeric_cols, index=1)
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} حسب {x_axis}")
        fig.update_traces(marker_color='#4CAF50')  # لون مخصص
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(255,255,255,0.95)')
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

# ---------------------- التصدير ----------------------

elif page == "📤 التصدير":
    st.subheader("📥 تنزيل البيانات")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("💾 تحميل كـ CSV", csv, "analysis.csv", "text/csv")

    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Analysis")

    excel_data = excel_buffer.getvalue()
    st.download_button("📊 تحميل كـ Excel", excel_data, "analysis.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
