# Credit Risk Analysis

## Goal

Assess borrower risk using transparent credit scoring, default probability, and risk segmentation.

## What This Project Teaches

Credit drivers, rule-based scoring, probability of default, borrower classification, risk charts, and risk reporting.

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
cd finance-foundations\practical-projects\03-credit-risk-analysis
..\.venv\Scripts\python src\main.py
```

## Inputs

- `data/sample_credit_data.csv`

## Outputs

- `outputs/charts/*.png`
- `outputs/reports/credit_risk_analysis_report.md`

## Finance Concepts Used

Debt-to-income, missed payments, credit score, default probability, and risk categories.

## Python Concepts Used

pandas feature engineering, rule-based models, classification, and matplotlib charts.

## Example Results

Borrowers with high debt-to-income, missed payments, short credit histories, and unstable employment score as riskier.

## Limitations

Fake data and a hand-built learning model. Do not use for real lending.

## Next Improvements

Add logistic regression, calibration, ROC/AUC, and fairness checks.

## Portfolio Submission Notes

This is one of the strongest portfolio projects in the repo. Review the generated report at `outputs/reports/credit_risk_analysis_report.md` and the chart PNGs under `outputs/charts/`.

## One-Sentence Summary

Assess sample borrower risk with a transparent credit score, default probability, risk segment, charts, and report.

## Why This Project Matters

Credit risk analysis connects finance, data, regulation-aware modeling, and explainable risk communication.

## Features

- Credit score model
- Default probability estimate
- Low, medium, high, and very high risk segments
- Borrower insights and risk-driver charts
- Research folder for credit-cycle article notes

## Demo

Run the CLI, then open `outputs/reports/credit_risk_analysis_report.md` and the chart PNGs in `outputs/charts/`.

## Installation

```bash
pip install -r requirements.txt
```

## How To Run CLI

```bash
python main.py --data data/sample_credit_data.csv
```

## How To Run Dashboard

```bash
streamlit run app.py
```

## Article Reader

Credit cycle or borrower-risk articles can be processed by the shared article reader, then linked to this project's `research/` folder as model driver notes.

## Technical Concepts Used

Rule-based scoring, logistic-style probability mapping, pandas grouping, matplotlib charts, and smoke tests.

## Future Improvements

Add validation metrics, calibration plots, fairness checks, and scenario stress testing.
