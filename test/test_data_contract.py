import pandas as pd

# Definimos las variables críticas que el modelo exige para funcionar
TARGET = "Personal Loan"
REQUIRED = {TARGET, "Income", "CCAvg", "Age"}

def load_data():
    return pd.read_csv("notebooks/data/raw/dataset.csv")

def test_dataset_is_not_empty():
    assert not load_data().empty

def test_required_columns_exist():
    assert REQUIRED <= set(load_data().columns)

def test_target_has_no_missing_and_two_classes():
    y = load_data()[TARGET]
    assert y.notna().all()
    assert y.nunique() >= 2