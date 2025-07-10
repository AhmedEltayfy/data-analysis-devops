from fpdf import FPDF
import re
import time

start = time.time()

# معالجة نتائج التنسيق
with open("black_output.txt", "r", encoding="utf-8") as f:
    black_lines = f.readlines()

# استخراج عدد الملفات المعاد تنسيقها
formatted_files = 0
for line in black_lines:
    if re.search(r"reformatted", line):
        formatted_files += 1

# تحديد الحالة العامة للتنسيق
black_status = "✅ ناجح" if "All done!" in "".join(black_lines) else "⚠️ مطلوب"

# معالجة نتائج pytest
with open("test_results.txt", "r", encoding="utf-8") as f:
    test_lines = f.readlines()

# توليد تقرير PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_text_color(0, 0, 128)
pdf.cell(200, 10, txt="📊 Budget Analyzer CI Report", ln=True, align='C')
pdf.set_text_color(0, 0, 0)

pdf.ln(5)
pdf.cell(200, 10, txt=f"📁 حالة التنسيق: {black_status}", ln=True)
pdf.cell(200, 10, txt=f"📝 عدد ملفات معاد تنسيقها: {formatted_files}", ln=True)

duration = round(time.time() - start, 2)
pdf.cell(200, 10, txt=f"⏱️ مدة تنفيذ التقرير: {duration} ثانية", ln=True)

pdf.ln(5)
pdf.cell(200, 10, txt="🧪 نتائج اختبارات pytest:", ln=True)

for line in test_lines[:20]:
    pdf.cell(200, 8, txt=line.strip(), ln=True)

pdf.output("ci_report.pdf")
