# Python Portfolio Analysis

## Goal

Analyze a stock portfolio with Python returns, volatility, Sharpe ratio, drawdown, allocation, and correlations.

## What This Project Teaches

Daily returns, weighted portfolio return, annualized risk metrics, correlation, and portfolio visualization.

## Folder Structure

```text
data/
src/
outputs/charts/
outputs/reports/
notes/
```

## How To Run

```powershell
cd finance-foundations\practical-projects\02-python-portfolio-analysis
..\.venv\Scripts\python src\main.py
```

## Inputs

- `data/sample_portfolio_prices.csv`
- `data/sample_portfolio_weights.csv`

## Outputs

- `outputs/charts/*.png`
- `outputs/reports/portfolio_analysis_report.md`

## Finance Concepts Used

Returns, volatility, Sharpe ratio, max drawdown, asset allocation, and correlation.

## Python Concepts Used

pandas time series, vectorized portfolio math, and matplotlib charts.

## Example Results

The fake sample portfolio grows over the short period, with concentrated technology exposure.

## Limitations

Fake short-period prices, no dividends, no fees, no taxes, and no rebalancing.

## Next Improvements

Add benchmark comparison, rolling risk, and optimization.

## Portfolio Submission Notes

This is one of the strongest portfolio projects in the repo. Review the generated report at `outputs/reports/portfolio_analysis_report.md` and the chart PNGs under `outputs/charts/`.

## One-Sentence Summary

Analyze a sample portfolio's returns, volatility, Sharpe ratio, drawdown, allocation, and correlation.

## Why This Project Matters

Portfolio analytics shows how finance theory turns into risk management, asset allocation, and investor communication.

## Features

- Daily and cumulative returns
- Weighted portfolio return
- Annualized return and volatility
- Sharpe ratio and max drawdown
- Correlation matrix and allocation charts
- Research folder for article-driven notes

## Demo

Run the CLI, then open `outputs/reports/portfolio_analysis_report.md` and the chart PNGs in `outputs/charts/`.

## Installation

```bash
pip install -r requirements.txt
```

## How To Run CLI

```bash
python main.py --prices data/sample_portfolio_prices.csv --weights data/sample_portfolio_weights.csv
```

## How To Run Dashboard

```bash
streamlit run app.py
```

## Article Reader

Market and portfolio articles can be processed by the shared article reader, then linked to this project's `research/` folder as risk scenarios or allocation notes.

## Technical Concepts Used

pandas time series, vectorized math, matplotlib charting, correlation analysis, and smoke tests.

## Future Improvements

Add benchmark comparison, rolling metrics, factor attribution, and optimization.
