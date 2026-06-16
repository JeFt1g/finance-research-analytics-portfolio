from __future__ import annotations

import pandas as pd


def calculate_trends(df: pd.DataFrame) -> pd.DataFrame:
    trends = df.sort_values("year").copy()
    for column in ["revenue", "gross_profit", "operating_income", "net_income"]:
        trends[f"{column}_growth"] = trends[column].pct_change()
    return trends

