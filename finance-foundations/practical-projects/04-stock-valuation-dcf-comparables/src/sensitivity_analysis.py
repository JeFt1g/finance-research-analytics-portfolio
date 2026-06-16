from __future__ import annotations

import pandas as pd

from dcf_model import build_dcf


def build_sensitivity_table(financials: pd.DataFrame, base_assumption: pd.Series) -> pd.DataFrame:
    rows = []
    for discount_rate in [0.08, 0.09, 0.10, 0.11, 0.12]:
        for terminal_growth in [0.02, 0.025, 0.03, 0.035, 0.04]:
            assumption = base_assumption.copy()
            assumption["discount_rate"] = discount_rate
            assumption["terminal_growth"] = terminal_growth
            _, summary = build_dcf(financials, assumption)
            rows.append({"discount_rate": discount_rate, "terminal_growth": terminal_growth, "implied_share_price": summary["implied_share_price"]})
    return pd.DataFrame(rows)

