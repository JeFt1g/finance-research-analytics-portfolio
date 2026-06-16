"""Event-study framework."""
def abnormal(stock, market): return [s - m for s, m in zip(stock, market)]
def event_study(stock, market, event_index, window=2):
    start, end = max(0, event_index-window), min(len(stock), event_index+window+1)
    ar = abnormal(stock[start:end], market[start:end])
    return {"window": (start, end-1), "abnormal_returns": ar, "cumulative_abnormal_return": sum(ar)}
if __name__ == "__main__":
    print(event_study([.001,-.002,.004,.052,.008,-.003,.002], [.001,-.001,.002,.006,.003,-.002,.001], 3))
