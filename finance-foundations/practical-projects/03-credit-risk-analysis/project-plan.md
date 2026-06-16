# Project Plan

## Objective

Score borrowers, estimate default probability, segment risk, generate charts, and export a credit risk report.

## Inputs

Income, debt-to-income, credit history, missed payments, debt, employment status, loan amount, and sample default flag.

## Calculations

Rule-based credit score, default probability, risk category, and segment summaries.

## Outputs

Scored borrowers, four charts, and a markdown report.

## Step-by-Step Build Plan

1. Load borrower data.
2. Calculate scores.
3. Estimate default probability.
4. Assign risk category.
5. Generate charts and report.

## Subagents Responsible

Project Architect, Finance Analyst, Quant Developer, Data Visualization, Report Writer, and QA Agent.

## Acceptance Criteria

`src/main.py` runs, generates four charts, and writes the required report.

## Future Improvements

Add validated logistic regression and fairness review.

