"""Liquidity exit model."""
def days_to_exit(position_shares, average_daily_volume, max_volume_share=0.1):
    if position_shares <= 0 or average_daily_volume <= 0:
        raise ValueError("inputs must be positive")
    return position_shares / (average_daily_volume * max_volume_share)

if __name__ == "__main__":
    print(days_to_exit(500_000, 1_000_000))
