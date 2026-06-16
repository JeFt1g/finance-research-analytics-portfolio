# How To Run The Finance Research + Analytics OS

## 1. Create Virtual Environment

```bash
python -m venv .venv
```

## 2. Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Article Reader

```bash
python shared/article_reader/article_reader.py --input research/articles/sample_company_article.txt
```

## 5. Run Research App

```bash
streamlit run apps/finance_research_app/app.py
```

## 6. Run Project Launcher

```bash
streamlit run apps/project_dashboard_launcher/app.py
```

## 7. Run Practical Projects

```bash
cd practical-projects/01-financial-statement-analysis
python main.py
```

```bash
cd ../02-python-portfolio-analysis
python main.py
```

```bash
cd ../03-credit-risk-analysis
python main.py
```

```bash
cd ../04-stock-valuation-dcf-comparables
python main.py
```

## 8. Run Simple Smoke Tests

From each practical project folder:

```bash
python tests/test_basic_run.py
```

## 9. Run Portfolio Check

From the repo root:

```bash
python scripts/check_portfolio.py
```
