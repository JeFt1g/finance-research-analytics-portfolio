from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]

PROJECTS = [
    {
        "name": "Financial Statement Analysis",
        "path": "practical-projects/01-financial-statement-analysis",
        "summary": "Analyzes Apple-style sample financials, ratios, trends, charts, risks, and a markdown report.",
        "report": "outputs/reports/financial_statement_analysis_report.md",
        "command": "cd practical-projects/01-financial-statement-analysis && python main.py",
    },
    {
        "name": "Python Portfolio Analysis",
        "path": "practical-projects/02-python-portfolio-analysis",
        "summary": "Calculates portfolio returns, volatility, Sharpe ratio, drawdown, allocation, and correlation.",
        "report": "outputs/reports/portfolio_analysis_report.md",
        "command": "cd practical-projects/02-python-portfolio-analysis && python main.py",
    },
    {
        "name": "Credit Risk Analysis",
        "path": "practical-projects/03-credit-risk-analysis",
        "summary": "Scores borrowers, estimates default probability, segments risk, and charts drivers.",
        "report": "outputs/reports/credit_risk_analysis_report.md",
        "command": "cd practical-projects/03-credit-risk-analysis && python main.py",
    },
    {
        "name": "Stock Valuation: DCF + Comparables",
        "path": "practical-projects/04-stock-valuation-dcf-comparables",
        "summary": "Builds DCF forecasts, comparables, sensitivity tables, scenarios, and a recommendation.",
        "report": "outputs/reports/stock_valuation_report.md",
        "command": "cd practical-projects/04-stock-valuation-dcf-comparables && python main.py",
    },
]


def main() -> None:
    try:
        import streamlit as st
    except ImportError:
        print("Streamlit is not installed. Install requirements.txt, then run: streamlit run apps/project_dashboard_launcher/app.py")
        return

    st.set_page_config(page_title="Finance Project Launcher", layout="wide")
    st.title("Finance Project Dashboard Launcher")
    st.write("Portfolio home page for the runnable finance analytics projects.")

    for project in PROJECTS:
        project_dir = REPO_ROOT / project["path"]
        report_path = project_dir / project["report"]
        with st.expander(project["name"], expanded=True):
            st.write(project["summary"])
            st.code(project["command"])
            st.write(f"Project folder: `{project['path']}`")
            if report_path.exists():
                st.write(f"Report: `{project['path']}/{project['report']}`")
                st.markdown(report_path.read_text(encoding="utf-8")[:1800])
            else:
                st.warning("Report has not been generated yet.")

    st.subheader("Best Demo Order")
    st.write("1. Stock Valuation App  2. Portfolio Analysis App  3. Finance Research App  4. Financial Statement Analysis App  5. Credit Risk App")


if __name__ == "__main__":
    main()
