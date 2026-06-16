"""Event-study abnormal return template."""
def abnormal_returns(stock, market):
    if len(stock) != len(market):
        raise ValueError("series must match")
    return [s - m for s, m in zip(stock, market)]

if __name__ == "__main__":
    ar = abnormal_returns([0.002, -0.004, 0.05], [0.001, -0.002, 0.006])
    print(ar, sum(ar))
