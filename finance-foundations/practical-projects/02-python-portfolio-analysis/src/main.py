from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parents[1]
ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from portfolio_charts import create_portfolio_charts
from portfolio_returns import calculate_cumulative_returns, calculate_daily_returns, calculate_portfolio_returns, calculate_portfolio_value, load_prices, load_weights
from risk_metrics import asset_risk_return, correlation_matrix, portfolio_risk_summary
from utils.report_helpers import format_currency, format_number, format_percent, markdown_table


def build_report(weights: pd.Series, risk_summary: dict[str, float], asset_risk: pd.DataFrame, correlations: pd.DataFrame, charts: dict[str, Path]) -> str:
    allocation = weights.reset_index()
    allocation.columns = ["ticker", "weight"]
    off_diagonal = ~np.eye(len(correlations), dtype=bool)
    average_correlation = correlations.where(off_diagonal).stack().mean() if len(correlations) > 1 else 0
    diversification = "moderate diversification" if average_correlation < 0.85 else "limited diversification"
    return f"""# Python Portfolio Analysis Report

## Portfolio Overview

Fake four-asset portfolio with Apple, Microsoft, NVIDIA, and JPMorgan-style sample prices.

## Executive Summary

The portfolio ended with a total return of {format_percent(risk_summary['total_return'])}, annualized volatility of {format_percent(risk_summary['annualized_volatility'])}, Sharpe ratio of {format_number(risk_summary['sharpe_ratio'], 2)}, and max drawdown of {format_percent(risk_summary['max_drawdown'])}.

## Data Used

- `data/sample_portfolio_prices.csv`
- `data/sample_portfolio_weights.csv`

The dataset contains fake prices and static weights for a short sample portfolio.

## Key Metrics

- Total return: {format_percent(risk_summary['total_return'])}
- Annualized return: {format_percent(risk_summary['annualized_return'])}
- Annualized volatility: {format_percent(risk_summary['annualized_volatility'])}
- Sharpe ratio: {format_number(risk_summary['sharpe_ratio'], 2)}
- Max drawdown: {format_percent(risk_summary['max_drawdown'])}

## Asset Allocation

{markdown_table(allocation, {'weight': format_percent})}

Chart: `../charts/{charts['asset_allocation'].name}`

## Return Analysis

Chart: `../charts/{charts['portfolio_value'].name}`

## Risk Analysis

{markdown_table(asset_risk, {'annualized_return': format_percent, 'annualized_volatility': format_percent})}

Chart: `../charts/{charts['risk_return'].name}`

## Sharpe Ratio

The estimated Sharpe ratio is {format_number(risk_summary['sharpe_ratio'], 2)} using a 2.0% risk-free rate assumption.

## Drawdown Analysis

Max drawdown was {format_percent(risk_summary['max_drawdown'])}.

## Key Insights

- The portfolio generated positive cumulative return in the fake sample period.
- The highest-growth asset contributes higher volatility.
- Average pairwise correlation suggests {diversification}.
- Technology exposure is a major concentration risk.

## Charts Generated

- `../charts/{charts['portfolio_value'].name}`
- `../charts/{charts['cumulative_returns'].name}`
- `../charts/{charts['asset_allocation'].name}`
- `../charts/{charts['risk_return'].name}`
- `../charts/{charts['correlation_heatmap'].name}`

## Article Insights

No project-specific articles have been processed yet. Add market or allocation articles to `research/articles/` and use the shared article reader to create stress scenarios or concentration notes.

## Key Risks

- Short sample history makes annualized metrics unstable.
- Static weights ignore rebalancing.
- No benchmark, fees, taxes, dividends, or factor attribution are included.

## Limitations

The dataset is fake and too short for investment decisions. Treat results as portfolio analytics practice only.

## Final Conclusion

The sample portfolio performed well, but the short period makes annualized metrics unstable. Add a benchmark and longer history next.
"""


def main() -> None:
    prices = load_prices()
    weights = load_weights()
    asset_returns = calculate_daily_returns(prices)
    portfolio_returns = calculate_portfolio_returns(asset_returns, weights)
    cumulative_returns = calculate_cumulative_returns(asset_returns)
    portfolio_value = calculate_portfolio_value(portfolio_returns)
    risk_summary = portfolio_risk_summary(portfolio_returns)
    asset_risk = asset_risk_return(asset_returns)
    correlations = correlation_matrix(asset_returns)
    charts = create_portfolio_charts(portfolio_value, cumulative_returns, weights, asset_risk, correlations, PROJECT_DIR / "outputs" / "charts")
    report = build_report(weights, risk_summary, asset_risk, correlations, charts)
    report_path = PROJECT_DIR / "outputs" / "reports" / "portfolio_analysis_report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report, encoding="utf-8")
    print(f"Wrote report: {report_path}")
    for chart in charts.values():
        print(f"Wrote chart: {chart}")


if __name__ == "__main__":
    main()
