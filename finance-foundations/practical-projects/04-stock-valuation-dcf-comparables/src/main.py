from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from comparables_analysis import calculate_multiples, comparable_implied_values, load_comparables
from dcf_model import build_dcf, get_assumption, load_assumptions, load_financials
from sensitivity_analysis import build_sensitivity_table
from utils.report_helpers import format_currency, format_number, format_percent, markdown_table
from valuation_charts import create_valuation_charts


def recommendation_label(upside_downside: float) -> str:
    if upside_downside > 0.15:
        return "Undervalued"
    if upside_downside < -0.15:
        return "Overvalued"
    return "Fairly valued"


def build_scenario_values(financials: pd.DataFrame, assumptions: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, assumption in assumptions.iterrows():
        _, summary = build_dcf(financials, assumption)
        rows.append({"scenario": assumption["scenario"], "implied_share_price": summary["implied_share_price"], "current_share_price": summary["current_share_price"], "upside_downside": summary["upside_downside"]})
    return pd.DataFrame(rows)


def build_report(base_assumption: pd.Series, dcf_summary: dict[str, float], multiples: pd.DataFrame, comparable_values: pd.DataFrame, sensitivity: pd.DataFrame, scenario_values: pd.DataFrame, charts: dict[str, Path]) -> str:
    recommendation = recommendation_label(dcf_summary["upside_downside"])
    multiples_table = multiples[["company", "ev_revenue", "ev_ebitda", "pe_ratio"]]
    comparable_table = comparable_values[["method", "multiple", "implied_share_price"]]
    scenario_table = scenario_values[["scenario", "implied_share_price", "upside_downside"]]
    sensitivity_summary = sensitivity.groupby("discount_rate", as_index=False)["implied_share_price"].mean()
    return f"""# Stock Valuation Report

## Company Analyzed

Tesla-style fake sample company.

## Executive Summary

The base-case DCF implies a share price of {format_currency(dcf_summary['implied_share_price'], digits=0, suffix='')} versus a current sample price of {format_currency(dcf_summary['current_share_price'], digits=0, suffix='')}. That represents {format_percent(dcf_summary['upside_downside'])} upside/downside and supports a preliminary **{recommendation}** conclusion.

## Data Used

- `data/tesla_sample_financials.csv`
- `data/sample_comparables.csv`
- `data/dcf_assumptions.csv`

The dataset is fake and built for valuation practice.

## Key Metrics

- Enterprise value: {format_currency(dcf_summary['enterprise_value'])}
- Equity value: {format_currency(dcf_summary['equity_value'])}
- Implied share price: {format_currency(dcf_summary['implied_share_price'], digits=0, suffix='')}
- Current sample share price: {format_currency(dcf_summary['current_share_price'], digits=0, suffix='')}
- Upside/downside: {format_percent(dcf_summary['upside_downside'])}
- Recommendation: {recommendation}

## Business Overview

The company is modeled as a high-growth electric vehicle and energy platform with meaningful reinvestment needs.

## DCF Assumptions

| Assumption | Base Case |
|---|---|
| Revenue growth | {format_percent(base_assumption['revenue_growth'])} |
| Operating margin | {format_percent(base_assumption['operating_margin'])} |
| Tax rate | {format_percent(base_assumption['tax_rate'])} |
| Reinvestment rate | {format_percent(base_assumption['reinvestment_rate'])} |
| Discount rate | {format_percent(base_assumption['discount_rate'])} |
| Terminal growth | {format_percent(base_assumption['terminal_growth'])} |

## DCF Valuation

Enterprise value is estimated at {format_currency(dcf_summary['enterprise_value'])}, equity value at {format_currency(dcf_summary['equity_value'])}, and present value of terminal value at {format_currency(dcf_summary['pv_terminal_value'])}.

Chart: `../charts/{charts['revenue_forecast'].name}`

Chart: `../charts/{charts['free_cash_flow_forecast'].name}`

## Comparable Company Analysis

{markdown_table(multiples_table, {'ev_revenue': lambda value: format_number(value, 2), 'ev_ebitda': lambda value: format_number(value, 2), 'pe_ratio': lambda value: format_number(value, 2)})}

{markdown_table(comparable_table, {'multiple': lambda value: format_number(value, 2), 'implied_share_price': lambda value: format_currency(value, digits=0, suffix='')})}

Chart: `../charts/{charts['comparable_valuation'].name}`

## Sensitivity Analysis

{markdown_table(sensitivity_summary, {'discount_rate': format_percent, 'implied_share_price': lambda value: format_currency(value, digits=0, suffix='')})}

Chart: `../charts/{charts['dcf_sensitivity'].name}`

## Valuation Range

{markdown_table(scenario_table, {'implied_share_price': lambda value: format_currency(value, digits=0, suffix=''), 'upside_downside': format_percent})}

Chart: `../charts/{charts['valuation_range'].name}`

## Key Risks

- Terminal value sensitivity.
- Margin and growth uncertainty.
- Peer selection risk.
- No dilution or detailed capital structure schedule.

## Charts Generated

- `../charts/{charts['revenue_forecast'].name}`
- `../charts/{charts['free_cash_flow_forecast'].name}`
- `../charts/{charts['comparable_valuation'].name}`
- `../charts/{charts['dcf_sensitivity'].name}`
- `../charts/{charts['valuation_range'].name}`

## Article Insights

No project-specific articles have been processed yet. Add company or sector articles to `research/articles/` and use the shared article reader to create valuation assumption notes.

## Limitations

The model uses fake data, simple assumptions, and a simplified capital structure. Real valuation should include segment detail, dilution, working capital, capex schedules, WACC support, and peer selection review.

## Final Recommendation

The base-case output indicates the stock is {recommendation.lower()} in this fake dataset. This is a learning model, not investment advice.
"""


def main() -> None:
    financials = load_financials()
    assumptions = load_assumptions()
    base = get_assumption(assumptions, "Base")
    forecast, dcf_summary = build_dcf(financials, base)
    multiples = calculate_multiples(load_comparables())
    comparable_values = comparable_implied_values(financials, multiples, float(base["net_debt"]), float(base["shares_outstanding"]))
    sensitivity = build_sensitivity_table(financials, base)
    scenario_values = build_scenario_values(financials, assumptions)
    charts = create_valuation_charts(financials, forecast, sensitivity, comparable_values, scenario_values, PROJECT_DIR / "outputs" / "charts")
    report = build_report(base, dcf_summary, multiples, comparable_values, sensitivity, scenario_values, charts)
    report_path = PROJECT_DIR / "outputs" / "reports" / "stock_valuation_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    print(f"Wrote report: {report_path}")
    for chart in charts.values():
        print(f"Wrote chart: {chart}")


if __name__ == "__main__":
    main()
