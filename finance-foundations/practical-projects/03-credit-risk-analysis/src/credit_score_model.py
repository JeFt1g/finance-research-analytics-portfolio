from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.data_validation import load_csv, require_columns, require_no_missing, require_numeric_columns

REQUIRED_COLUMNS = [
    "borrower_id",
    "income",
    "debt_to_income",
    "credit_history_years",
    "missed_payments_12m",
    "existing_debt",
    "employment_status",
    "loan_amount",
    "defaulted",
]


def load_credit_data(path: Path | None = None) -> pd.DataFrame:
    df = load_csv(path or PROJECT_DIR / "data" / "sample_credit_data.csv")
    require_columns(df, REQUIRED_COLUMNS)
    require_no_missing(df, REQUIRED_COLUMNS)
    require_numeric_columns(df, ["income", "debt_to_income", "credit_history_years", "missed_payments_12m", "existing_debt", "loan_amount", "defaulted"])
    return df.copy()


def employment_adjustment(status: str) -> float:
    return {"employed": 60, "contractor": 20, "self_employed": 15, "unemployed": -90}.get(str(status).lower(), 0)


def calculate_credit_score(row: pd.Series) -> float:
    debt_burden = row["existing_debt"] / max(row["income"], 1)
    loan_to_income = row["loan_amount"] / max(row["income"], 1)
    score = (
        600
        + min(row["income"] / 100000 * 110, 130)
        + min(row["credit_history_years"] * 10, 120)
        + employment_adjustment(row["employment_status"])
        - row["debt_to_income"] * 190
        - row["missed_payments_12m"] * 45
        - debt_burden * 80
        - loan_to_income * 45
    )
    return float(np.clip(score, 300, 850))


def score_borrowers(df: pd.DataFrame) -> pd.DataFrame:
    scored = df.copy()
    scored["credit_score"] = scored.apply(calculate_credit_score, axis=1)
    return scored

