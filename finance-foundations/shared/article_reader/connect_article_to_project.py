from __future__ import annotations

from classify_article import classify_projects


def project_connections(text: str) -> list[str]:
    matches = classify_projects(text)
    if not matches:
        return ["No strong practical project connection detected. Review manually for possible ideas."]
    return [f"{match['label']} - matched: {', '.join(match['matches'])}" for match in matches]
