from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.data_validation import load_csv, require_columns, require_no_missing, require_numeric_columns


def load_financials(path: Path | None = None) -> pd.DataFrame:
    columns = ["year", "revenue", "ebitda", "operating_income", "net_income", "free_cash_flow", "shares_outstanding", "net_debt", "current_share_price"]
    df = load_csv(path or PROJECT_DIR / "data" / "tesla_sample_financials.csv")
    require_columns(df, columns)
    require_no_missing(df, columns)
    require_numeric_columns(df, columns)
    return df.sort_values("year").reset_index(drop=True)


def load_assumptions(path: Path | None = None) -> pd.DataFrame:
    columns = ["scenario", "revenue_growth", "operating_margin", "tax_rate", "reinvestment_rate", "discount_rate", "terminal_growth", "shares_outstanding", "net_debt", "current_share_price"]
    df = load_csv(path or PROJECT_DIR / "data" / "dcf_assumptions.csv")
    require_columns(df, columns)
    require_no_missing(df, columns)
    require_numeric_columns(df, [column for column in columns if column != "scenario"])
    return df


def get_assumption(assumptions: pd.DataFrame, scenario: str = "Base") -> pd.Series:
    match = assumptions[assumptions["scenario"].str.lower() == scenario.lower()]
    if match.empty:
        raise ValueError(f"Missing scenario: {scenario}")
    return match.iloc[0]


def build_dcf(financials: pd.DataFrame, assumption: pd.Series, forecast_years: int = 5) -> tuple[pd.DataFrame, dict[str, float]]:
    discount_rate = float(assumption["discount_rate"])
    terminal_growth = float(assumption["terminal_growth"])
    if discount_rate <= terminal_growth:
        raise ValueError("Discount rate must be greater than terminal growth.")
    latest = financials.iloc[-1]
    revenue = float(latest["revenue"])
    rows = []
    for year_number in range(1, forecast_years + 1):
        revenue *= 1 + float(assumption["revenue_growth"])
        operating_income = revenue * float(assumption["operating_margin"])
        nopat = operating_income * (1 - float(assumption["tax_rate"]))
        reinvestment = revenue * float(assumption["reinvestment_rate"])
        free_cash_flow = nopat - reinvestment
        rows.append(
            {
                "year": int(latest["year"] + year_number),
                "revenue": revenue,
                "operating_income": operating_income,
                "nopat": nopat,
                "reinvestment": reinvestment,
                "free_cash_flow": free_cash_flow,
                "pv_free_cash_flow": free_cash_flow / ((1 + discount_rate) ** year_number),
            }
        )
    forecast = pd.DataFrame(rows)
    terminal_cash_flow = forecast.iloc[-1]["free_cash_flow"] * (1 + terminal_growth)
    terminal_value = terminal_cash_flow / (discount_rate - terminal_growth)
    pv_terminal_value = terminal_value / ((1 + discount_rate) ** forecast_years)
    enterprise_value = forecast["pv_free_cash_flow"].sum() + pv_terminal_value
    equity_value = enterprise_value - float(assumption["net_debt"])
    implied_share_price = equity_value / float(assumption["shares_outstanding"])
    summary = {
        "enterprise_value": float(enterprise_value),
        "equity_value": float(equity_value),
        "implied_share_price": float(implied_share_price),
        "terminal_value": float(terminal_value),
        "pv_terminal_value": float(pv_terminal_value),
        "current_share_price": float(assumption["current_share_price"]),
        "upside_downside": float(implied_share_price / float(assumption["current_share_price"]) - 1),
    }
    return forecast, summary

