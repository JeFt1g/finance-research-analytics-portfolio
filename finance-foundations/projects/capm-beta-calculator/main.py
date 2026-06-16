"""CAPM beta calculator."""
def mean(x): return sum(x)/len(x)
def beta(stock, market):
    sm, mm = mean(stock), mean(market)
    return sum((s-sm)*(m-mm) for s,m in zip(stock,market)) / sum((m-mm)**2 for m in market)
def capm(rf, b, market): return rf + b * (market - rf)
if __name__ == "__main__":
    b = beta([.04,-.02,.03,.01,.05], [.03,-.01,.02,.005,.035])
    print({"beta": round(b, 4), "expected_return": round(capm(.04, b, .09), 4)})
