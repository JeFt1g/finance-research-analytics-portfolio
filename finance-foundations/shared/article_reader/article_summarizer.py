from __future__ import annotations

import re


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_sentences(text: str) -> list[str]:
    pieces = re.split(r"(?<=[.!?])\s+", clean_text(text))
    return [piece.strip() for piece in pieces if len(piece.strip()) > 20]


def summarize_text(text: str, max_sentences: int = 4) -> list[str]:
    sentences = split_sentences(text)
    if not sentences:
        return ["No summary available because the file contains too little readable text."]
    finance_terms = [
        "revenue",
        "margin",
        "cash flow",
        "risk",
        "valuation",
        "portfolio",
        "credit",
        "default",
        "volatility",
        "earnings",
        "debt",
        "equity",
        "growth",
        "market",
    ]
    scored = []
    for index, sentence in enumerate(sentences):
        lower = sentence.lower()
        score = sum(2 for term in finance_terms if term in lower)
        score += min(len(re.findall(r"\d", sentence)), 5)
        score += max(0, 3 - index) * 0.25
        scored.append((score, index, sentence))
    best = sorted(scored, key=lambda item: (-item[0], item[1]))[:max_sentences]
    return [sentence for _, _, sentence in sorted(best, key=lambda item: item[1])]
