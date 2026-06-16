"""Short squeeze risk score."""
def short_squeeze_score(short_interest_percent, days_to_cover, borrow_cost_percent, volatility_percent):
    return min(100, short_interest_percent * 1.5 + days_to_cover * 8 + borrow_cost_percent * 1.2 + volatility_percent * 0.4)

if __name__ == "__main__":
    print(short_squeeze_score(25, 4, 12, 60))
