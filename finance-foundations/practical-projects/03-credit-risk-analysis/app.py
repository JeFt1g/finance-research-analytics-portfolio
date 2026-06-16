from __future__ import annotations

import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
REPORT = PROJECT_DIR / "outputs" / "reports" / "credit_risk_analysis_report.md"
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

    st.set_page_config(page_title="Credit Risk Analysis", layout="wide")
    st.title("Credit Risk Analysis")
    st.write("Borrower scoring, default probability, risk segmentation, and risk-driver charts.")

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
    for chart in sorted(CHART_DIR.glob("*.png")):
        st.image(str(chart), caption=chart.name, use_container_width=True)


if __name__ == "__main__":
    main()
