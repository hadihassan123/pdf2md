# pdf2md

![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-active-green)

A lightweight CLI tool that converts PDF files into clean Markdown using [MarkItDown](https://github.com/microsoft/markitdown).

## Features

- PDF → Markdown conversion via MarkItDown
- Simple CLI interface
- Output to a specific file, a folder, or default to the same directory as input
- Automatically generates output filename from the input PDF name
- Cleans common PDF encoding artifacts

## Installation

```bash
git clone https://github.com/hadihassan123/pdf2md.git
cd pdf2md
pip install -e .
```

This installs the `pdf2md` command globally (or within your active virtualenv).

> **Recommended:** use a virtual environment.
> ```bash
> python -m venv .venv
> source .venv/bin/activate
> pip install .
> ```

## Usage

```bash
# Convert and save next to the original PDF
pdf2md file.pdf

# Convert and save to a specific file
pdf2md file.pdf -o output.md

# Convert and save into a folder (trailing slash required)
pdf2md file.pdf -o ./out/
```

The converted Markdown is both printed to the terminal and written to the output file.

## Project Structure

```
pdf2md/
├── pdf2md_tool/
│   ├── __init__.py
│   ├── cli.py          # Argument parsing and entry point
│   └── src/
│       └── converter.py  # PDF → Markdown conversion logic
├── setup.py
├── .gitignore
└── README.md
```

## Dependencies

- Python 3.10+
- [`markitdown`](https://pypi.org/project/markitdown/) — Microsoft's document-to-Markdown library

## License

Not specified. All rights reserved by the author unless otherwise stated.