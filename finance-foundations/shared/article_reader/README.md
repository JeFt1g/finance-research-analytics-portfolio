# Shared Article Reader

Rule-based local article reader for finance research notes. It reads `.txt`, `.md`, and `.pdf` files when `pypdf` is installed.

## How To Run

```bash
python shared/article_reader/article_reader.py --input research/articles/sample_company_article.txt
```

Outputs are saved to `research/processed/`.

## What It Extracts

- Short summary
- Important numbers
- Company names when obvious
- Risk words
- Finance keywords
- Theory connections
- Practical project connections
- Possible app or case study ideas

## Limitations

This reader uses local rule-based extraction. It is useful for organizing research, but it does not replace professional financial analysis or full language-model reasoning.
