# Financial Statement Analysis

## Goal

Analyze fake Apple-style financial statements to understand revenue growth, profitability, liquidity, leverage, and efficiency.

## What This Project Teaches

Ratio analysis, trend analysis, financial interpretation, charting, and markdown report generation.

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
cd finance-foundations\practical-projects\01-financial-statement-analysis
..\.venv\Scripts\python src\analyze_financials.py
```

## Inputs

- `data/apple_sample_financials.csv`

## Outputs

- `outputs/charts/*.png`
- `outputs/reports/financial_statement_analysis_report.md`

## Finance Concepts Used

Revenue growth, margins, ROE, current ratio, debt-to-equity, and asset turnover.

## Python Concepts Used

pandas, reusable functions, matplotlib, and markdown export.

## Example Results

The sample company shows renewed revenue growth, high profitability, improving margins, and declining leverage.

## Limitations

Fake annual data; no cash flow statement, segment data, interest expense, or industry benchmark.

## Next Improvements

Add cash flow analysis, peer comparison, and common-size statements.

## Portfolio Submission Notes

This is one of the strongest portfolio projects in the repo. Review the generated report at `outputs/reports/financial_statement_analysis_report.md` and the chart PNGs under `outputs/charts/`.

## One-Sentence Summary

Analyze Apple-style financial statements into ratios, trend charts, risks, and a markdown analyst report.

## Why This Project Matters

Financial statement analysis is a core finance analyst skill because it turns accounting data into business performance, liquidity, leverage, and valuation inputs.

## Features

- Revenue and profit trends
- Gross, operating, and net margin
- ROE, current ratio, debt-to-equity, and asset turnover
- Portfolio-ready charts and report
- Research folder for article-driven notes

## Demo

Run the CLI, then open `outputs/reports/financial_statement_analysis_report.md` and the chart PNGs in `outputs/charts/`.

## Installation

```bash
pip install -r requirements.txt
```

## How To Run CLI

```bash
python main.py --company "Apple Sample"
```

## How To Run Dashboard

```bash
streamlit run app.py
```

## Article Reader

Add company articles to `research/articles/` and process global sources with `shared/article_reader/article_reader.py`; useful insights can be copied into this project's `research/processed/` folder.

## Technical Concepts Used

Python path-safe scripts, pandas transforms, matplotlib charts, markdown report generation, and lightweight smoke tests.

## Future Improvements

Add quarterly data, cash flow statement analysis, peer benchmarking, and SEC filing ingestion.
