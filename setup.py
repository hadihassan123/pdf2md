from setuptools import setup, find_packages

setup(
    name="pdf2md",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["markitdown"],
    entry_points={
        "console_scripts": [
            "pdf2md=pdf2md_tool.cli:main"
        ]
    },
)