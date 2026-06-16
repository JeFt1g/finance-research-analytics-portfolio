"""Compare active and passive returns after fees."""
def compounded(returns):
    total = 1.0
    for item in returns:
        total *= 1 + item
    return total - 1

def compare(active, passive, active_fee=0.01, passive_fee=0.001):
    return {"active_net": compounded(active) - active_fee, "passive_net": compounded(passive) - passive_fee}

if __name__ == "__main__":
    print(compare([0.02, -0.01, 0.015], [0.015, -0.005, 0.012]))
