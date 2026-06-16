from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from charts import create_charts
from ratio_analysis import calculate_ratios, load_financials
from trend_analysis import calculate_trends
from utils.report_helpers import format_currency, format_number, format_percent, markdown_table


def build_report(df: pd.DataFrame, charts: dict[str, Path]) -> str:
    latest = df.iloc[-1]
    previous = df.iloc[-2]
    ratio_table = df[
        ["year", "gross_margin", "operating_margin", "net_profit_margin", "roe", "current_ratio", "debt_to_equity", "asset_turnover"]
    ].tail(4)
    formatters = {
        "gross_margin": format_percent,
        "operating_margin": format_percent,
        "net_profit_margin": format_percent,
        "roe": format_percent,
        "current_ratio": lambda value: format_number(value, 2),
        "debt_to_equity": lambda value: format_number(value, 2),
        "asset_turnover": lambda value: format_number(value, 2),
    }
    revenue_view = "Revenue growth is healthy in the latest year." if latest["revenue_growth"] > 0.05 else "Revenue growth is modest and should be monitored."
    margin_view = "Net margin improved." if latest["net_profit_margin"] > previous["net_profit_margin"] else "Net margin compressed."
    leverage_view = "Debt-to-equity declined, reducing balance sheet risk." if latest["debt_to_equity"] < previous["debt_to_equity"] else "Debt-to-equity increased and should be monitored."
    return f"""# Financial Statement Analysis Report

## Company Analyzed

Apple-style fake sample company from 2020 through 2025.

## Executive Summary

The company generated {format_currency(latest['revenue'])} of revenue and {format_currency(latest['net_income'])} of net income in {int(latest['year'])}. Latest revenue growth was {format_percent(latest['revenue_growth'])}, net margin was {format_percent(latest['net_profit_margin'])}, and ROE was {format_percent(latest['roe'])}.

## Data Used

Input file: `data/apple_sample_financials.csv`

The dataset contains fake annual financial statement data for revenue, gross profit, operating income, net income, current assets, current liabilities, total assets, shareholders' equity, and total debt.

## Key Metrics

- Latest revenue growth: {format_percent(latest['revenue_growth'])}
- Gross margin: {format_percent(latest['gross_margin'])}
- Operating margin: {format_percent(latest['operating_margin'])}
- Net margin: {format_percent(latest['net_profit_margin'])}
- ROE: {format_percent(latest['roe'])}
- Current ratio: {format_number(latest['current_ratio'], 2)}
- Debt-to-equity: {format_number(latest['debt_to_equity'], 2)}

## Revenue Trend

{revenue_view}

Chart: `../charts/{charts['revenue_trend'].name}`

## Profitability Trend

{margin_view}

Chart: `../charts/{charts['net_income_trend'].name}`

## Ratio Analysis

{markdown_table(ratio_table, formatters)}

Chart: `../charts/{charts['margin_comparison'].name}`

## Key Insights

- Revenue reached the highest level in the sample period.
- Operating income and net income grew in the latest year.
- ROE remains high.
- Current ratio is close to 1.0, so liquidity is adequate but not excessive.
- {leverage_view}

## Charts Generated

- `../charts/{charts['revenue_trend'].name}`
- `../charts/{charts['net_income_trend'].name}`
- `../charts/{charts['margin_comparison'].name}`
- `../charts/{charts['roe_trend'].name}`
- `../charts/{charts['liquidity_trend'].name}`

## Article Insights

No project-specific articles have been processed yet. Add company articles to `research/articles/` and use the shared article reader to link margin, governance, and valuation risks into this report.

## Key Risks

- Annual data hides quarterly volatility.
- High ROE can be flattered by leverage or buybacks.
- Liquidity needs cash flow timing, not just current ratio.

## Limitations

The dataset is fake, annual, and simplified. Real analysis should use filings, segment data, cash flow details, footnotes, and peer benchmarks.

## Final Conclusion

The sample company appears financially strong, with renewed growth, improving margins, and lower leverage. The main watch item is liquidity close to 1.0.
"""


def main() -> None:
    financials = load_financials()
    ratios = calculate_ratios(financials)
    analysis = calculate_trends(ratios)
    charts = create_charts(analysis, PROJECT_DIR / "outputs" / "charts")
    report = build_report(analysis, charts)
    report_path = PROJECT_DIR / "outputs" / "reports" / "financial_statement_analysis_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    print(f"Wrote report: {report_path}")
    for chart in charts.values():
        print(f"Wrote chart: {chart}")


if __name__ == "__main__":
    main()
