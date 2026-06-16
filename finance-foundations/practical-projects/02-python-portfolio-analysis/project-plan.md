# Project Plan

## Objective

Calculate portfolio returns, risk metrics, charts, and a markdown report from sample stock prices and weights.

## Inputs

Daily prices and portfolio weights.

## Calculations

Daily returns, cumulative returns, weighted portfolio return, annualized return, annualized volatility, Sharpe ratio, max drawdown, and correlation matrix.

## Outputs

Five charts and a portfolio report.

## Step-by-Step Build Plan

1. Load prices and weights.
2. Validate matching tickers.
3. Calculate returns and risk.
4. Generate charts.
5. Export report.

## Subagents Responsible

Project Architect, Finance Analyst, Quant Developer, Data Visualization, Report Writer, and QA Agent.

## Acceptance Criteria

`src/main.py` runs, generates five charts, and writes the required report.

## Future Improvements

Add benchmark, rolling metrics, and optimization.

