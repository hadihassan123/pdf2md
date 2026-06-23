from markitdown import MarkItDown
import re

def clean_markdown(text):
    # Remove PDF encoding artifacts
    text = re.sub(r"\(cid:\d+\)", "", text)

    # Replace weird bullets
    text = text.replace("•", "-")

    # Replace weird question marks
    text = text.replace("?", "-")

    # Remove isolated "n"
    text = re.sub(r"\bn\s+", "", text)

    # Collapse multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Collapse multiple blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    return text.strip()

md = MarkItDown()


def clean_text(text: str) -> str:

    # Remove PDF cid artifacts
    text = re.sub(r"\(cid:\d+\)", "", text)

    # Convert isolated separator question marks to dash
    text = re.sub(r"\s+\?\s+", " - ", text)

    # Remove standalone weird n
    text = re.sub(r"\bn\b", "", text)

    # Remove repeated spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Trim spaces around newlines
    text = re.sub(r" *\n *", "\n", text)

    # Keep paragraphs (max 2 blank lines)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

def convert_pdf(file_path: str) -> str:
    result = md.convert(file_path)
    raw_text = result.text_content
    return clean_text(raw_text)