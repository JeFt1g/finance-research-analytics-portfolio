from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
REPORT = PROJECT_DIR / "outputs" / "reports" / "financial_statement_analysis_report.md"
CHART_DIR = PROJECT_DIR / "outputs" / "charts"


def run_project() -> tuple[bool, str]:
    result = subprocess.run([sys.executable, "main.py"], cwd=PROJECT_DIR, text=True, capture_output=True, check=False)
    return result.returncode == 0, result.stdout + result.stderr


def main() -> None:
    try:
        import streamlit as st
    except ImportError:
        print("Streamlit is not installed. Run `python main.py` for CLI mode.")
        return

    st.set_page_config(page_title="Financial Statement Analysis", layout="wide")
    st.title("Financial Statement Analysis")
    st.write("Apple-style sample company ratio, trend, margin, liquidity, and risk analysis.")

    if st.button("Run Analysis"):
        ok, output = run_project()
        st.code(output)
        if not ok:
            st.error("CLI run failed.")

    if REPORT.exists():
        st.subheader("Final Report")
        st.markdown(REPORT.read_text(encoding="utf-8"))
    else:
        st.warning("Run the analysis to generate the report.")

    st.subheader("Charts")
    charts = sorted(CHART_DIR.glob("*.png"))
    for chart in charts:
        st.image(str(chart), caption=chart.name, use_container_width=True)


if __name__ == "__main__":
    main()
