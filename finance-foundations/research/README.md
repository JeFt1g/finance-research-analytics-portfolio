# Finance Research System

This folder turns articles, source notes, and market commentary into organized portfolio research. It connects reading work to finance theory and to runnable analytics projects.

## What The Research System Does

- Stores raw articles in `research/articles/`
- Processes local `.txt`, `.md`, and optional `.pdf` files with the shared article reader
- Saves extracted insights to `research/processed/`
- Connects articles to theory folders and practical projects
- Produces source notes and portfolio case study ideas

## How To Add An Article

Save article text, notes, or a PDF into `research/articles/`. Use clear file names such as `apple-margin-risk.txt` or `market-efficiency-event.md`.

## How To Process An Article

```bash
python shared/article_reader/article_reader.py --input research/articles/sample_company_article.txt
```

The processed markdown output is saved to `research/processed/`.

## How To Connect An Article To A Theory

Review the processed output and copy the useful points into the relevant theory folder, especially `08-article-notes.md` and `09-reading-list.md`.

## How To Connect An Article To A Practical Project

If the article creates a useful example, scenario, risk, or assumption, add it to the relevant project under `practical-projects/<project>/research/`.

## How To Turn An Article Into A Portfolio Case Study

Use the templates in `research/templates/` to document the source, extract finance claims, connect them to theory, and translate the idea into a project enhancement or dashboard screenshot.

## Limitations

The article reader is rule-based. It helps organize research, but it does not replace professional analyst judgment.
