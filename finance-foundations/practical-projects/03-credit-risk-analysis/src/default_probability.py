from __future__ import annotations

import math

import numpy as np
import pandas as pd


def estimate_default_probability(row: pd.Series) -> float:
    base = 1 / (1 + math.exp((row["credit_score"] - 620) / 55))
    missed_payment_penalty = min(row["missed_payments_12m"] * 0.045, 0.22)
    dti_penalty = max(row["debt_to_income"] - 0.40, 0) * 0.55
    unemployment_penalty = 0.10 if str(row["employment_status"]).lower() == "unemployed" else 0.0
    loan_pressure = max(row["loan_amount"] / max(row["income"], 1) - 0.35, 0) * 0.20
    return float(np.clip(base + missed_payment_penalty + dti_penalty + unemployment_penalty + loan_pressure, 0.01, 0.95))


def add_default_probability(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["default_probability"] = result.apply(estimate_default_probability, axis=1)
    return result

