from __future__ import annotations

import pandas as pd


def classify_risk(probability: float) -> str:
    if probability < 0.12:
        return "Low risk"
    if probability < 0.25:
        return "Medium risk"
    if probability < 0.45:
        return "High risk"
    return "Very high risk"


def add_risk_segments(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["risk_category"] = result["default_probability"].apply(classify_risk)
    return result


def segment_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("risk_category", as_index=False)
        .agg(
            borrowers=("borrower_id", "count"),
            avg_credit_score=("credit_score", "mean"),
            avg_default_probability=("default_probability", "mean"),
            avg_debt_to_income=("debt_to_income", "mean"),
            default_rate=("defaulted", "mean"),
        )
        .sort_values("avg_default_probability")
    )

