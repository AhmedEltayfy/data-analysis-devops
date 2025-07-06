import pandas as pd
import os

# محاكاة ملفات مالية بصيغة CSV
file_paths = [
    r"D:/IBM DevOps and Software/..."
    r"02 Second Phase/03 Working in Small Batches/dat/balance_sheet_jan.csv",
    r"D:/IBM DevOps and Software/..."
    r"02 Second Phase/03 Working in Small Batches/dat/balance_sheet_feb.csv",
    r"D:/IBM DevOps and Software/..."
    r"02 Second Phase/03 Working in Small Batches/dat/balance_sheet_mar.csv",
]



# خطوة 1: التحقق من تنسيق الملف وتحميله
def load_and_validate(path):
    try:
        df = pd.read_csv(path)
        assert "Revenue" in df.columns, "Missing 'Revenue' column"
        return df
    except Exception as e:
        print(f"[خطأ] {path}: {e}")
        return None



# خطوة 2: إجراء تحليل بسيط على العمود المستهدف
def analyze(df):
    revenue_mean = df["Revenue"].mean()
    print(f"✅ متوسط الإيرادات: {revenue_mean:.2f}")
    return revenue_mean

# خطوة 3: محاكاة إرسال النتيجة (مثلاً إلى API أو حفظها)
def ship_output(result, file_id):
    print(f"📦 رفع نتيجة الملف '{file_id}' إلى النظام... [تم بنجاح]")


# الخط الرئيسي: تنفيذ كل مرحلة على كل ملف على حدة
for path in file_paths:
    print(f"\n🚧 معالجة الملف: {path}")

    df = load_and_validate(path)
    if df is None:
        continue

    result = analyze(df)
    ship_output(result, os.path.basename(path))
    