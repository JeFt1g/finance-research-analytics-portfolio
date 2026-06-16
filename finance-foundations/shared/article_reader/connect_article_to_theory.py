from __future__ import annotations

from classify_article import classify_theories


def theory_connections(text: str) -> list[str]:
    matches = classify_theories(text)
    if not matches:
        return ["No strong theory connection detected. Review manually for possible links."]
    return [f"{match['label']} - matched: {', '.join(match['matches'])}" for match in matches]
