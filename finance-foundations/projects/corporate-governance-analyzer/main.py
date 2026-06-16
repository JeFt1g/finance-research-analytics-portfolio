"""Governance text analyzer."""
RULES = {"compensation": ["guaranteed bonus", "repriced options"], "alignment": ["dual class", "related party"], "monitoring": ["staggered board", "limited independence"]}
def analyze(notes):
    text = notes.lower()
    flags = {k: [p for p in phrases if p in text] for k, phrases in RULES.items()}
    flags = {k: v for k, v in flags.items() if v}
    return {"risk_score": min(100, 20 * sum(len(v) for v in flags.values())), "flags": flags}
if __name__ == "__main__":
    print(analyze("Dual class shares, staggered board, and guaranteed bonus."))
