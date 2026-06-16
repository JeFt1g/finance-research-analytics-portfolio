from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
ARTICLE_READER_DIR = REPO_ROOT / "shared" / "article_reader"
sys.path.insert(0, str(ARTICLE_READER_DIR))

from article_reader import analyze_text, render_markdown


def save_analysis(markdown: str, source_name: str) -> Path:
    safe_name = "".join(char if char.isalnum() or char in {"-", "_"} else "_" for char in source_name).strip("_")
    if not safe_name:
        safe_name = "pasted_article"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = REPO_ROOT / "research" / "processed" / f"{safe_name}_{timestamp}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    return output_path


def main() -> None:
    try:
        import streamlit as st
    except ImportError:
        print("Streamlit is not installed. Install requirements.txt, then run: streamlit run apps/finance_research_app/app.py")
        return

    st.set_page_config(page_title="Finance Research App", layout="wide")
    st.title("Finance Research App")

    pasted_text = st.text_area("Article text", height=260)
    upload = st.file_uploader("Upload .txt or .md", type=["txt", "md"])
    source_name = "pasted_article"
    article_text = pasted_text

    if upload is not None:
        source_name = Path(upload.name).stem
        article_text = upload.read().decode("utf-8", errors="replace")

    if st.button("Analyze Article", type="primary", disabled=not article_text.strip()):
        analysis = analyze_text(article_text, source_name)
        markdown = render_markdown(analysis)
        output_path = save_analysis(markdown, source_name)

        left, right = st.columns(2)
        with left:
            st.subheader("Summary")
            for item in analysis["summary"]:
                st.write(f"- {item}")
            st.subheader("Important Numbers")
            st.write(analysis["numbers"] or ["None detected"])
            st.subheader("Risks")
            st.write(analysis["risks"] or ["None detected"])
        with right:
            st.subheader("Theory Connections")
            st.write(analysis["theory_connections"])
            st.subheader("Project Connections")
            st.write(analysis["project_connections"])
            st.subheader("Saved Output")
            st.code(str(output_path.relative_to(REPO_ROOT)))

        st.subheader("Markdown Output")
        st.markdown(markdown)


if __name__ == "__main__":
    main()
