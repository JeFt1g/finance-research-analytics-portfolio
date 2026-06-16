from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.data_validation import load_csv, require_columns, require_no_missing, require_numeric_columns

REQUIRED_COLUMNS = [
    "year",
    "revenue",
    "gross_profit",
    "operating_income",
    "net_income",
    "current_assets",
    "current_liabilities",
    "total_assets",
    "shareholders_equity",
    "total_debt",
]


def load_financials(path: Path | None = None) -> pd.DataFrame:
    df = load_csv(path or PROJECT_DIR / "data" / "apple_sample_financials.csv")
    require_columns(df, REQUIRED_COLUMNS)
    require_no_missing(df, REQUIRED_COLUMNS)
    require_numeric_columns(df, REQUIRED_COLUMNS)
    return df.sort_values("year").reset_index(drop=True)


def calculate_ratios(df: pd.DataFrame) -> pd.DataFrame:
    ratios = df.copy()
    ratios["gross_margin"] = ratios["gross_profit"] / ratios["revenue"]
    ratios["operating_margin"] = ratios["operating_income"] / ratios["revenue"]
    ratios["net_profit_margin"] = ratios["net_income"] / ratios["revenue"]
    ratios["roe"] = ratios["net_income"] / ratios["shareholders_equity"]
    ratios["current_ratio"] = ratios["current_assets"] / ratios["current_liabilities"]
    ratios["debt_to_equity"] = ratios["total_debt"] / ratios["shareholders_equity"]
    ratios["asset_turnover"] = ratios["revenue"] / ratios["total_assets"]
    return ratios


def ratio_summary(df: pd.DataFrame) -> pd.DataFrame:
    return calculate_ratios(df)[
        [
            "year",
            "gross_margin",
            "operating_margin",
            "net_profit_margin",
            "roe",
            "current_ratio",
            "debt_to_equity",
            "asset_turnover",
        ]
    ]

