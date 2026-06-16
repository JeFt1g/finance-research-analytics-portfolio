from __future__ import annotations

from pathlib import Path


def read_text_file(path: Path | str) -> str:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return path.read_text(encoding="utf-8")


def write_text_file(path: Path | str, content: str) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def list_supported_files(path: Path | str, extensions: tuple[str, ...]) -> list[Path]:
    path = Path(path)
    if path.is_file():
        return [path] if path.suffix.lower() in extensions else []
    if not path.exists():
        raise FileNotFoundError(f"Missing path: {path}")
    return sorted(file for file in path.iterdir() if file.is_file() and file.suffix.lower() in extensions)
