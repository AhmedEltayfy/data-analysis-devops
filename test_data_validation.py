import pandas as pd
import pytest

# تحميل البيانات
@pytest.fixture
def load_data():
    return pd.read_csv("balance_sheet_mar.csv")

# اختبار خلوّ البيانات من القيم الفارغة
def test_no_missing_values(load_data):
    assert load_data.isnull().sum().sum() == 0, "⚠️ البيانات تحتوي على قيم فارغة!"

# اختبار أن جميع القيم رقمية
def test_data_types(load_data):
    numeric_types = ['int64', 'float64']
    assert all(load_data.dtypes.isin(numeric_types)), "⚠️ هناك أعمدة غير رقمية!"