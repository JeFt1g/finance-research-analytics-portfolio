from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[2]
SHARED_DIR = ROOT_DIR / "shared"
sys.path.insert(0, str(SHARED_DIR))

from utils.chart_helpers import apply_finance_style, ensure_output_dir, plt, save_figure


def create_credit_charts(df: pd.DataFrame, output_dir: Path) -> dict[str, Path]:
    output_dir = ensure_output_dir(output_dir)
    apply_finance_style()

    fig, ax = plt.subplots()
    ax.hist(df["credit_score"], bins=8, color="#2f6f8f", edgecolor="white")
    ax.set_title("Credit Score Distribution")
    ax.set_xlabel("Credit score")
    ax.set_ylabel("Borrowers")
    score_path = save_figure(fig, output_dir / "credit_score_distribution.png")

    fig, ax = plt.subplots()
    ax.hist(df["default_probability"], bins=8, color="#b45f4d", edgecolor="white")
    ax.set_title("Default Probability Distribution")
    ax.set_xlabel("Default probability")
    ax.set_ylabel("Borrowers")
    probability_path = save_figure(fig, output_dir / "default_probability_distribution.png")

    fig, ax = plt.subplots()
    category_order = ["Low risk", "Medium risk", "High risk", "Very high risk"]
    counts = df["risk_category"].value_counts().reindex(category_order).fillna(0)
    ax.bar(counts.index, counts.values, color="#476f52")
    ax.set_title("Risk Category Counts")
    ax.set_xlabel("Risk category")
    ax.set_ylabel("Borrowers")
    ax.tick_params(axis="x", rotation=20)
    category_path = save_figure(fig, output_dir / "risk_category_counts.png")

    fig, ax = plt.subplots()
    colors = df["defaulted"].map({0: "#2f6f8f", 1: "#b45f4d"})
    ax.scatter(df["debt_to_income"], df["default_probability"], c=colors, s=70, alpha=0.85)
    ax.set_title("Debt-To-Income Vs Default Probability")
    ax.set_xlabel("Debt-to-income")
    ax.set_ylabel("Default probability")
    dti_path = save_figure(fig, output_dir / "dti_vs_default_probability.png")

    return {
        "credit_score_distribution": score_path,
        "default_probability_distribution": probability_path,
        "risk_category_counts": category_path,
        "dti_vs_default_probability": dti_path,
    }

