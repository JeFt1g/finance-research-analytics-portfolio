from __future__ import annotations


THEORY_RULES = {
    "Black-Scholes": ["option", "call", "put", "strike", "volatility", "implied volatility", "greeks", "derivative"],
    "Market Efficiency": ["efficient market", "market efficiency", "abnormal return", "event study", "index", "passive"],
    "Modern Portfolio Theory": ["portfolio", "diversification", "correlation", "efficient frontier", "risk-return", "allocation"],
    "CAPM": ["capm", "beta", "risk-free", "market return", "alpha", "cost of equity"],
    "Arbitrage Pricing Theory": ["factor", "macro", "risk premium", "multi-factor", "apt", "arbitrage pricing"],
    "Agency Theory": ["governance", "management", "shareholder", "incentive", "compensation", "agency"],
    "Limits to Arbitrage": ["mispricing", "short selling", "liquidity", "funding", "bubble", "crash", "arbitrage"],
}

PROJECT_RULES = {
    "Financial Statement Analysis": ["revenue", "margin", "income statement", "balance sheet", "roe", "ratio"],
    "Portfolio Analysis": ["portfolio", "returns", "volatility", "sharpe", "allocation", "correlation"],
    "Credit Risk Analysis": ["credit", "default", "borrower", "loan", "debt-to-income", "delinquency"],
    "Stock Valuation": ["valuation", "dcf", "free cash flow", "multiple", "enterprise value", "share price"],
    "Option Pricing": ["option", "strike", "implied volatility", "call", "put", "greeks"],
    "Market Efficiency Testing": ["event", "abnormal return", "announcement", "market reaction", "efficiency"],
    "Corporate Governance Analysis": ["governance", "board", "executive", "compensation", "shareholder"],
}


def classify(text: str, rules: dict[str, list[str]]) -> list[dict[str, object]]:
    lower = text.lower()
    results = []
    for label, keywords in rules.items():
        matches = [keyword for keyword in keywords if keyword in lower]
        if matches:
            results.append({"label": label, "score": len(matches), "matches": matches})
    return sorted(results, key=lambda item: (-int(item["score"]), str(item["label"])))


def classify_theories(text: str) -> list[dict[str, object]]:
    return classify(text, THEORY_RULES)


def classify_projects(text: str) -> list[dict[str, object]]:
    return classify(text, PROJECT_RULES)
