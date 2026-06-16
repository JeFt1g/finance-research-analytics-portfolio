"""Compensation alignment score."""
def compensation_alignment_score(ownership_percent, performance_pay_percent, guaranteed_pay_percent):
    score = 50 + min(ownership_percent * 2, 20) + min(performance_pay_percent * 0.4, 25) - min(guaranteed_pay_percent * 0.5, 30)
    return max(0, min(100, score))

if __name__ == "__main__":
    print(compensation_alignment_score(4, 60, 20))
