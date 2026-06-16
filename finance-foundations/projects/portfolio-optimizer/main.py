"""Portfolio optimizer starter."""
def pret(w, r): return sum(a * b for a, b in zip(w, r))
def vol(w1, w2, v1, v2, corr): return (w1*w1*v1*v1 + w2*w2*v2*v2 + 2*w1*w2*corr*v1*v2) ** 0.5
def sharpe(ret, rf, risk): return (ret - rf) / risk
if __name__ == "__main__":
    for i in range(5):
        w = i / 4
        r = pret([w, 1-w], [0.08, 0.03])
        risk = vol(w, 1-w, 0.18, 0.07, 0.2)
        print({"stock_weight": w, "return": round(r, 4), "volatility": round(risk, 4), "sharpe": round(sharpe(r, 0.02, risk), 4)})
