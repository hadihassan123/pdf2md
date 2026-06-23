from markitdown import MarkItDown
import re

md = MarkItDown()

def clean_text(text: str) -> str:
    text = re.sub(r"\(cid:\d+\)", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def convert_pdf(file_path: str) -> str:
    result = md.convert(file_path)
    raw_text = result.text_content
    return clean_text(raw_text)