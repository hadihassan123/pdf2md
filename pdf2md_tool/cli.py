import argparse
import os
from pdf2md_tool.src.converter import convert_pdf


def build_output_path(input_file, output_arg):
    file_name = os.path.splitext(os.path.basename(input_file))[0] + ".md"

    # Case 1: no output provided → same folder
    if not output_arg:
        return os.path.join(os.path.dirname(input_file), file_name)

    # Case 2: output is a folder
    if output_arg.endswith("/"):
        os.makedirs(output_arg, exist_ok=True)
        return os.path.join(output_arg, file_name)

    # Case 3: full file path provided
    return output_arg


def main():
    parser = argparse.ArgumentParser(description="PDF → Markdown converter")

    parser.add_argument("file", help="Path to PDF file")
    parser.add_argument("-o", "--output", help="Output file or folder", default=None)

    args = parser.parse_args()

    print("\n🔄 Converting...\n")

    result = convert_pdf(args.file)

    output_path = build_output_path(args.file, args.output)

    # save file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(result)
    print(f"\n✅ Saved to: {output_path}")


if __name__ == "__main__":
    main()