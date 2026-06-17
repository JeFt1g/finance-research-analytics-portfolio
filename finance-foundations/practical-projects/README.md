# Practical Finance Projects

This folder turns finance theory into real projects.

## Portfolio Status

These four projects are the strongest submission pieces in the repository. Each one includes fake sample data, runnable Python code, generated charts, and a professional markdown report under `outputs/reports/`.

## Projects

| Project | Primary Skill | Reviewer Output |
|---|---|---|
| [Financial Statement Analysis](01-financial-statement-analysis/README.md) | Accounting ratios and business interpretation | `outputs/reports/financial_statement_analysis_report.md` |
| [Python Portfolio Analysis](02-python-portfolio-analysis/README.md) | Portfolio returns and risk | `outputs/reports/portfolio_analysis_report.md` |
| [Credit Risk Analysis](03-credit-risk-analysis/README.md) | Borrower scoring and default probability | `outputs/reports/credit_risk_analysis_report.md` |
| [Stock Valuation: DCF + Comparables](04-stock-valuation-dcf-comparables/README.md) | DCF, peer multiples, and recommendation logic | `outputs/reports/stock_valuation_report.md` |

## Recommended Build Order

1. Financial Statement Analysis
2. Python Portfolio Analysis
3. Stock Valuation
4. Credit Risk Analysis

## Why This Order

Financial statement analysis teaches the base language of companies.
Portfolio analysis teaches market returns and risk.
Stock valuation combines accounting, forecasting, and market pricing.
Credit risk analysis introduces risk modeling and probability.

## Setup

```powershell
cd "C:\Users\User\Documents\Projects (Finance)\finance-foundations\practical-projects"
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
```

## Run Each Project

```powershell
cd 01-financial-statement-analysis
..\.venv\Scripts\python src\analyze_financials.py

cd ..\02-python-portfolio-analysis
..\.venv\Scripts\python src\main.py

cd ..\03-credit-risk-analysis
..\.venv\Scripts\python src\main.py

cd ..\04-stock-valuation-dcf-comparables
..\.venv\Scripts\python src\main.py
```

## Verify Everything

From `finance-foundations/`:

```powershell
python scripts\check_portfolio.py
```

## Submission Notes

- All data is fake and educational.
- Outputs are already generated so reviewers can inspect reports and charts without running code first.
- No project uses paid APIs or live credentials.
