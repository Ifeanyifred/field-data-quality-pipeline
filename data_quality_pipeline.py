import pandas as pd
import numpy as np

def load_data(path):
    return pd.read_csv(path)

def basic_quality_checks(df):
    report = {}
    report["rows"] = len(df)
    report["missing_values"] = df.isnull().sum().to_dict()
    report["duplicate_rows"] = df.duplicated().sum()
    return report

def detect_outliers(df, column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1
    outliers = df[(df[column] < q1 - 1.5 * iqr) | (df[column] > q3 + 1.5 * iqr)]
    return outliers

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

if __name__ == "__main__":
    data = load_data("sample_survey.csv")
    report = basic_quality_checks(data)
    print("DATA QUALITY REPORT:", report)

    if "load_kw" in data.columns:
        outliers = detect_outliers(data, "load_kw")
        print(f"Detected {len(outliers)} outliers")

    cleaned = clean_data(data)
    cleaned.to_csv("cleaned_data.csv", index=False)
