# QA Checklist

## Architecture

- [x] `shared/` contains datasets, templates, utils, charts, and reports folders.
- [x] Each project is isolated in its own numbered folder.
- [x] Each project includes `README.md`, `project-plan.md`, `data/`, `src/`, `outputs/`, and `notes/`.

## Data

- [x] Sample data exists for every project.
- [x] Required columns are documented in each README.
- [x] No project depends on paid APIs or live data.

## Code

- [x] Scripts run from each project folder.
- [x] Imports resolve without hidden dependencies.
- [x] Outputs are written under each project's `outputs/` folder.
- [x] Charts are saved as PNG files.

## Finance Logic

- [x] Ratio formulas are documented and checked.
- [x] Portfolio return and risk formulas are documented and checked.
- [x] Credit scoring assumptions are documented and checked.
- [x] DCF and comparable valuation assumptions are documented and checked.

## Reports

- [x] Every project generates a markdown report.
- [x] Reports include executive summaries, assumptions, risks, and final conclusions.
- [x] Reports include tables or chart references useful for GitHub, school, or portfolio review.

## Verification Run

```powershell
cd "C:\Users\User\Documents\Projects (Finance)\finance-foundations\practical-projects"
.\.venv\Scripts\python -m compileall shared 01-financial-statement-analysis 02-python-portfolio-analysis 03-credit-risk-analysis 04-stock-valuation-dcf-comparables

cd 01-financial-statement-analysis
..\.venv\Scripts\python src\analyze_financials.py

cd ..\02-python-portfolio-analysis
..\.venv\Scripts\python src\main.py

cd ..\03-credit-risk-analysis
..\.venv\Scripts\python src\main.py

cd ..\04-stock-valuation-dcf-comparables
..\.venv\Scripts\python src\main.py
```

Result:

- 23 Python files.
- 31 markdown files.
- 11 CSV files.
- 19 PNG charts.
- 4 project scripts ran successfully.
