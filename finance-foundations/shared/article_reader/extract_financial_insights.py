from __future__ import annotations

import re


RISK_WORDS = [
    "risk",
    "uncertainty",
    "decline",
    "default",
    "liquidity",
    "leverage",
    "volatility",
    "inflation",
    "rates",
    "recession",
    "competition",
    "regulation",
    "impairment",
    "downgrade",
]

FINANCE_KEYWORDS = [
    "revenue",
    "earnings",
    "ebitda",
    "margin",
    "cash flow",
    "free cash flow",
    "debt",
    "equity",
    "valuation",
    "multiple",
    "portfolio",
    "return",
    "volatility",
    "beta",
    "credit",
    "default",
    "dividend",
    "buyback",
    "guidance",
    "interest rate",
]

KNOWN_COMPANIES = [
    "Apple",
    "Microsoft",
    "Nvidia",
    "Tesla",
    "Amazon",
    "Alphabet",
    "Meta",
    "JPMorgan",
    "Berkshire",
    "Netflix",
    "Exxon",
    "Walmart",
]


def extract_numbers(text: str, limit: int = 20) -> list[str]:
    pattern = r"(?<!\w)(?:\$?\d+(?:,\d{3})*(?:\.\d+)?%?|\d+(?:\.\d+)?x)(?!\w)"
    seen: list[str] = []
    for match in re.findall(pattern, text):
        if match not in seen:
            seen.append(match)
        if len(seen) >= limit:
            break
    return seen


def extract_companies(text: str, limit: int = 12) -> list[str]:
    found = []
    lower = text.lower()
    for company in KNOWN_COMPANIES:
        if company.lower() in lower:
            found.append(company)
    capitalized = re.findall(r"\b[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+){0,2}\b", text)
    stopwords = {"The", "This", "That", "For", "With", "From", "Article", "Source", "Market"}
    for name in capitalized:
        if name not in stopwords and name not in found:
            found.append(name)
        if len(found) >= limit:
            break
    return found[:limit]


def extract_matching_terms(text: str, terms: list[str], limit: int = 20) -> list[str]:
    lower = text.lower()
    matches = [term for term in terms if term.lower() in lower]
    return matches[:limit]


def extract_key_financial_points(text: str, limit: int = 8) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    points = []
    for sentence in sentences:
        lower = sentence.lower()
        if any(keyword in lower for keyword in FINANCE_KEYWORDS) or re.search(r"\d", sentence):
            points.append(sentence.strip())
        if len(points) >= limit:
            break
    return points or ["No clear financial points were detected with the rule-based extractor."]
