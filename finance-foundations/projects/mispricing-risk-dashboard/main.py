"""Mispricing risk dashboard prototype."""
def risk_score(mispricing, short_interest, days_to_cover, borrow_cost, volatility, leverage):
    return min(100, abs(mispricing)*0.8 + short_interest*1.2 + days_to_cover*6 + borrow_cost + volatility*0.3 + leverage*5)
def explain(score):
    if score >= 70: return "High risk: constraints can force early exit."
    if score >= 40: return "Medium risk: check liquidity, borrow, and drawdown."
    return "Lower risk in this simple model."
if __name__ == "__main__":
    score = risk_score(35, 28, 5, 12, 70, 2.5)
    print({"score": round(score, 2), "explanation": explain(score)})
