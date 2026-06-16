from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.chart_helpers import apply_finance_style, ensure_output_dir, plt, save_figure


def create_valuation_charts(
    financials: pd.DataFrame,
    forecast: pd.DataFrame,
    sensitivity: pd.DataFrame,
    comparable_values: pd.DataFrame,
    scenario_values: pd.DataFrame,
    output_dir: Path,
) -> dict[str, Path]:
    output_dir = ensure_output_dir(output_dir)
    apply_finance_style()

    fig, ax = plt.subplots()
    ax.plot(financials["year"], financials["revenue"], marker="o", label="Historical")
    ax.plot(forecast["year"], forecast["revenue"], marker="o", linestyle="--", label="Forecast")
    ax.set_title("Revenue Forecast")
    ax.set_xlabel("Year")
    ax.set_ylabel("USD millions")
    ax.legend()
    revenue_path = save_figure(fig, output_dir / "revenue_forecast.png")

    fig, ax = plt.subplots()
    ax.plot(financials["year"], financials["free_cash_flow"], marker="o", label="Historical")
    ax.plot(forecast["year"], forecast["free_cash_flow"], marker="o", linestyle="--", label="Forecast")
    ax.set_title("Free Cash Flow Forecast")
    ax.set_xlabel("Year")
    ax.set_ylabel("USD millions")
    ax.legend()
    fcf_path = save_figure(fig, output_dir / "free_cash_flow_forecast.png")

    pivot = sensitivity.pivot(index="discount_rate", columns="terminal_growth", values="implied_share_price")
    fig, ax = plt.subplots()
    image = ax.imshow(pivot.values, cmap="YlGnBu")
    ax.set_xticks(range(len(pivot.columns)), labels=[f"{value:.1%}" for value in pivot.columns])
    ax.set_yticks(range(len(pivot.index)), labels=[f"{value:.1%}" for value in pivot.index])
    ax.set_title("DCF Sensitivity: Implied Share Price")
    ax.set_xlabel("Terminal growth")
    ax.set_ylabel("Discount rate")
    for row_idx in range(len(pivot.index)):
        for col_idx in range(len(pivot.columns)):
            ax.text(col_idx, row_idx, f"${pivot.iloc[row_idx, col_idx]:.0f}", ha="center", va="center", color="black")
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    sensitivity_path = save_figure(fig, output_dir / "dcf_sensitivity.png")

    fig, ax = plt.subplots()
    ax.bar(comparable_values["method"], comparable_values["implied_share_price"], color="#6d7f3f")
    ax.set_title("Comparable Valuation Implied Share Price")
    ax.set_xlabel("Method")
    ax.set_ylabel("Implied share price")
    comparable_path = save_figure(fig, output_dir / "comparable_valuation.png")

    fig, ax = plt.subplots()
    ax.bar(scenario_values["scenario"], scenario_values["implied_share_price"], color=["#b45f4d", "#2f6f8f", "#476f52"])
    ax.axhline(scenario_values["current_share_price"].iloc[0], color="black", linestyle="--", linewidth=1.5, label="Current price")
    ax.set_title("Bull/Base/Bear Valuation Range")
    ax.set_xlabel("Scenario")
    ax.set_ylabel("Implied share price")
    ax.legend()
    range_path = save_figure(fig, output_dir / "valuation_range.png")

    return {
        "revenue_forecast": revenue_path,
        "free_cash_flow_forecast": fcf_path,
        "dcf_sensitivity": sensitivity_path,
        "comparable_valuation": comparable_path,
        "valuation_range": range_path,
    }

