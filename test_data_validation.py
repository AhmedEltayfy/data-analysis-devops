import pandas as pd


def load_data(file_path):
    return pd.read_csv(file_path)


def test_columns_exist():
    df = load_data("test_data/sample_budget.csv")
    expected_columns = ["Date", "Category", "Amount", "Description"]
    for col in expected_columns:
        assert col in df.columns


def test_amount_is_numeric():
    df = load_data("test_data/sample_budget.csv")
    assert pd.api.types.is_numeric_dtype(df["Amount"])


def test_no_missing_values():
    df = load_data("test_data/sample_budget.csv")
    assert not df.isnull().values.any()
