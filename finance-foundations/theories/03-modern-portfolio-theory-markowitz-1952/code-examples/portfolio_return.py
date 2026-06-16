"""Portfolio expected return."""
def portfolio_return(weights, returns):
    if abs(sum(weights) - 1) > 1e-8:
        raise ValueError("weights must sum to 1")
    return sum(w * r for w, r in zip(weights, returns))

if __name__ == "__main__":
    print(portfolio_return([0.6, 0.4], [0.08, 0.03]))
