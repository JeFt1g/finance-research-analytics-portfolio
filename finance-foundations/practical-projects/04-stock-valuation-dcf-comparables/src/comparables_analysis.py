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


def load_comparables(path: Path | None = None) -> pd.DataFrame:
    columns = ["company", "revenue", "ebitda", "net_income", "market_cap", "enterprise_value", "shares_outstanding"]
    df = load_csv(path or PROJECT_DIR / "data" / "sample_comparables.csv")
    require_columns(df, columns)
    require_no_missing(df, columns)
    require_numeric_columns(df, [column for column in columns if column != "company"])
    return df


def calculate_multiples(comparables: pd.DataFrame) -> pd.DataFrame:
    result = comparables.copy()
    result["ev_revenue"] = result["enterprise_value"] / result["revenue"]
    result["ev_ebitda"] = np.where(result["ebitda"] > 0, result["enterprise_value"] / result["ebitda"], np.nan)
    result["pe_ratio"] = np.where(result["net_income"] > 0, result["market_cap"] / result["net_income"], np.nan)
    return result


def comparable_implied_values(financials: pd.DataFrame, multiples: pd.DataFrame, net_debt: float, shares_outstanding: float) -> pd.DataFrame:
    latest = financials.iloc[-1]
    peers = multiples[multiples["company"].str.lower() != "tesla"]
    rows = [
        {
            "method": "EV/Revenue",
            "multiple": peers["ev_revenue"].median(),
            "implied_enterprise_value": latest["revenue"] * peers["ev_revenue"].median(),
            "implied_equity_value": latest["revenue"] * peers["ev_revenue"].median() - net_debt,
        },
        {
            "method": "EV/EBITDA",
            "multiple": peers["ev_ebitda"].median(),
            "implied_enterprise_value": latest["ebitda"] * peers["ev_ebitda"].median(),
            "implied_equity_value": latest["ebitda"] * peers["ev_ebitda"].median() - net_debt,
        },
        {
            "method": "P/E",
            "multiple": peers["pe_ratio"].median(),
            "implied_enterprise_value": np.nan,
            "implied_equity_value": latest["net_income"] * peers["pe_ratio"].median(),
        },
    ]
    result = pd.DataFrame(rows)
    result["implied_share_price"] = result["implied_equity_value"] / shares_outstanding
    return result

