"""Governance risk keyword template."""
RULES = {"pay": ["guaranteed bonus", "repricing"], "rights": ["dual class", "poison pill"], "board": ["staggered board", "limited independence"]}

def governance_flags(notes):
    text = notes.lower()
    return [(kind, word) for kind, words in RULES.items() for word in words if word in text]

if __name__ == "__main__":
    print(governance_flags("Dual class shares and a staggered board."))
