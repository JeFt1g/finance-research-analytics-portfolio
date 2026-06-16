# Stock Valuation: DCF + Comparables

## Goal

Value a Tesla-style company using DCF, comparable company multiples, sensitivity analysis, and bull/base/bear cases.

## What This Project Teaches

Revenue forecasting, free cash flow, terminal value, discount rates, peer multiples, valuation ranges, and investment recommendations.

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
cd finance-foundations\practical-projects\04-stock-valuation-dcf-comparables
..\.venv\Scripts\python src\main.py
```

## Inputs

- `data/tesla_sample_financials.csv`
- `data/sample_comparables.csv`
- `data/dcf_assumptions.csv`

## Outputs

- `outputs/charts/*.png`
- `outputs/reports/stock_valuation_report.md`

## Finance Concepts Used

DCF, revenue forecast, free cash flow, terminal value, enterprise value, equity value, implied share price, EV/Revenue, EV/EBITDA, and P/E.

## Python Concepts Used

pandas modeling, scenario analysis, sensitivity tables, and matplotlib charts.

## Example Results

The model compares DCF-implied value to current sample price and peer-implied values.

## Limitations

Fake data, simplified assumptions, no dilution schedule, no capex detail, and no real peer diligence.

## Next Improvements

Add real filings, explicit operating model schedules, and Monte Carlo sensitivity.

## Portfolio Submission Notes

This is one of the strongest portfolio projects in the repo. Review the generated report at `outputs/reports/stock_valuation_report.md` and the chart PNGs under `outputs/charts/`.

## One-Sentence Summary

Value a Tesla-style sample company with DCF, comparables, sensitivity analysis, scenarios, and a recommendation.

## Why This Project Matters

Stock valuation is a core finance portfolio skill because it connects business assumptions, cash flow forecasting, market multiples, and investment judgment.

## Features

- Revenue and free cash flow forecast
- Discount rate and terminal growth assumptions
- Enterprise value, equity value, and implied share price
- Comparable company analysis
- Bull, base, and bear scenarios
- Sensitivity chart and valuation report

## Demo

Run the CLI, then open `outputs/reports/stock_valuation_report.md` and the chart PNGs in `outputs/charts/`.

## Installation

```bash
pip install -r requirements.txt
```

## How To Run CLI

```bash
python main.py --company "Tesla Sample"
```

## How To Run Dashboard

```bash
streamlit run app.py
```

## Article Reader

Company articles can be processed by the shared article reader, then linked to this project's `research/` folder as risk notes, valuation assumptions, or comparable company context.

## Technical Concepts Used

DCF modeling, pandas scenario tables, sensitivity analysis, peer multiples, matplotlib charts, and smoke tests.

## Future Improvements

Add real filings, analyst estimate imports, WACC schedule detail, dilution, and more robust peer selection.
