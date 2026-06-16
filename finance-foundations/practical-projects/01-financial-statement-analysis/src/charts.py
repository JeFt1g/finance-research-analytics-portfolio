from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.chart_helpers import apply_finance_style, ensure_output_dir, plt, save_figure


def _line_chart(df: pd.DataFrame, y_columns: list[str], title: str, ylabel: str, path: Path) -> Path:
    apply_finance_style()
    fig, ax = plt.subplots()
    for column in y_columns:
        ax.plot(df["year"], df[column], marker="o", linewidth=2, label=column.replace("_", " ").title())
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    ax.legend()
    return save_figure(fig, path)


def create_charts(df: pd.DataFrame, output_dir: Path) -> dict[str, Path]:
    output_dir = ensure_output_dir(output_dir)
    return {
        "revenue_trend": _line_chart(df, ["revenue"], "Revenue Trend", "USD millions", output_dir / "revenue_trend.png"),
        "net_income_trend": _line_chart(df, ["net_income"], "Net Income Trend", "USD millions", output_dir / "net_income_trend.png"),
        "margin_comparison": _line_chart(
            df,
            ["gross_margin", "operating_margin", "net_profit_margin"],
            "Margin Comparison",
            "Margin",
            output_dir / "margin_comparison.png",
        ),
        "roe_trend": _line_chart(df, ["roe"], "Return On Equity Trend", "ROE", output_dir / "roe_trend.png"),
        "liquidity_trend": _line_chart(df, ["current_ratio"], "Liquidity Trend", "Current ratio", output_dir / "liquidity_trend.png"),
    }

