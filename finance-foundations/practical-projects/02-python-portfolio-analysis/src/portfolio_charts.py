from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.chart_helpers import apply_finance_style, ensure_output_dir, plt, save_figure


def create_portfolio_charts(
    portfolio_value: pd.Series,
    cumulative_returns: pd.DataFrame,
    weights: pd.Series,
    risk_return: pd.DataFrame,
    correlations: pd.DataFrame,
    output_dir: Path,
) -> dict[str, Path]:
    output_dir = ensure_output_dir(output_dir)
    apply_finance_style()

    fig, ax = plt.subplots()
    ax.plot(portfolio_value.index, portfolio_value.values, linewidth=2)
    ax.set_title("Portfolio Value Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Portfolio value")
    fig.autofmt_xdate()
    portfolio_value_path = save_figure(fig, output_dir / "portfolio_value.png")

    fig, ax = plt.subplots()
    cumulative_returns.plot(ax=ax, linewidth=1.8)
    ax.set_title("Asset Cumulative Returns")
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative return")
    fig.autofmt_xdate()
    cumulative_returns_path = save_figure(fig, output_dir / "cumulative_returns.png")

    fig, ax = plt.subplots()
    ax.pie(weights.values, labels=weights.index, autopct="%1.0f%%", startangle=90)
    ax.set_title("Asset Allocation")
    asset_allocation_path = save_figure(fig, output_dir / "asset_allocation.png")

    fig, ax = plt.subplots()
    ax.scatter(risk_return["annualized_volatility"], risk_return["annualized_return"], s=80)
    for _, row in risk_return.iterrows():
        ax.annotate(row["ticker"], (row["annualized_volatility"], row["annualized_return"]), xytext=(5, 5), textcoords="offset points")
    ax.set_title("Risk-Return By Asset")
    ax.set_xlabel("Annualized volatility")
    ax.set_ylabel("Annualized return")
    risk_return_path = save_figure(fig, output_dir / "risk_return.png")

    fig, ax = plt.subplots()
    image = ax.imshow(correlations.values, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(range(len(correlations.columns)), labels=correlations.columns)
    ax.set_yticks(range(len(correlations.index)), labels=correlations.index)
    ax.set_title("Return Correlation Heatmap")
    for row_idx in range(len(correlations.index)):
        for col_idx in range(len(correlations.columns)):
            ax.text(col_idx, row_idx, f"{correlations.iloc[row_idx, col_idx]:.2f}", ha="center", va="center", color="black")
    fig.colorbar(image, ax=ax, fraction=0.046, pad=0.04)
    correlation_path = save_figure(fig, output_dir / "correlation_heatmap.png")

    return {
        "portfolio_value": portfolio_value_path,
        "cumulative_returns": cumulative_returns_path,
        "asset_allocation": asset_allocation_path,
        "risk_return": risk_return_path,
        "correlation_heatmap": correlation_path,
    }

