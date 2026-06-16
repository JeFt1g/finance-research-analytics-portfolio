"""Estimate beta."""
def mean(values):
    return sum(values) / len(values)

def beta(stock, market):
    sm, mm = mean(stock), mean(market)
    cov = sum((s - sm) * (m - mm) for s, m in zip(stock, market))
    var = sum((m - mm) ** 2 for m in market)
    if var == 0:
        raise ValueError("market variance cannot be zero")
    return cov / var

if __name__ == "__main__":
    print(beta([0.04, -0.02, 0.03], [0.03, -0.01, 0.02]))
