"""Arbitrage failure simulation."""
def simulate_arbitrage(capital, position, adverse_move, margin_requirement):
    loss = position * adverse_move
    remaining = capital - loss
    required = position * margin_requirement
    return {"loss": loss, "remaining_capital": remaining, "required_margin": required, "forced_exit": remaining < required}

if __name__ == "__main__":
    print(simulate_arbitrage(1_000_000, 3_000_000, 0.2, 0.25))
