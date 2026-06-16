from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt


def ensure_output_dir(path: Path | str) -> Path:
    output_dir = Path(path)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def apply_finance_style() -> None:
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.rcParams.update(
        {
            "figure.figsize": (9, 5),
            "axes.titlesize": 13,
            "axes.labelsize": 10,
            "legend.frameon": False,
        }
    )


def save_figure(fig, path: Path | str) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=160, bbox_inches="tight")
    plt.close(fig)
    return path
