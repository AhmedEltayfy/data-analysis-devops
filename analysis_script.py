import pandas as pd
from pathlib import Path
import os

# تحديد مجلد البيانات
data_dir = Path("dat/")

# الحصول على جميع ملفات CSV داخل المجلد
file_paths = list(data_dir.glob("*.csv"))

# وظيفة 1: تحميل البيانات والتحقق من صحتها
def load_and_validate(path):
    try:
        df = pd.read_csv(path)
        assert "Revenue" in df.columns, "❌ خطأ: العمود 'Revenue' غير موجود!"
        print(f"✅ تم تحميل الملف بنجاح: {path}")
        return df
    except Exception as e:
        print(f"❌ خطأ في الملف {path}: {e}")
        return None

# وظيفة 2: تحليل الإيرادات
def analyze(df):
    revenue_mean = df["Revenue"].mean()
    print(f"📊 متوسط الإيرادات: {revenue_mean:.2f}")
    return revenue_mean

# وظيفة 3: إرسال النتيجة (محاكاة للنشر)
def ship_output(result, file_id):
    print(f"📦 رفع نتيجة الملف '{file_id}' إلى النظام... ✅ [تم بنجاح]")

# تشغيل التحليل لكل ملف في القائمة
for path in file_paths:
    print(f"\n🚧 معالجة الملف: {path}")

    df = load_and_validate(path)
    if df is None:
        continue

    result = analyze(df)
    ship_output(result, os.path.basename(path))