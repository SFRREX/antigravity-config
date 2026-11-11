#!/usr/bin/env python3
"""Convert PDF pages to PNG images.

Supports pypdfium2 (built-in, self-contained) and pdf2image (poppler-based).
"""

import os
import sys

def convert_with_pdfium(pdf_path, output_dir, max_dim=1000):
    import pypdfium2 as pdfium
    pdf = pdfium.PdfDocument(pdf_path)
    os.makedirs(output_dir, exist_ok=True)
    count = len(pdf)

    for i, page in enumerate(pdf):
        image = page.render(scale=2).to_pil()
        width, height = image.size
        if width > max_dim or height > max_dim:
            scale_factor = min(max_dim / width, max_dim / height)
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            image = image.resize((new_width, new_height))
        image_path = os.path.join(output_dir, f"page_{i+1}.png")
        image.save(image_path)
        print(f"Saved page {i+1} as {image_path} (size: {image.size})")

    print(f"Converted {count} pages to PNG images")
    return True

def convert_with_pdf2image(pdf_path, output_dir, max_dim=1000):
    from pdf2image import convert_from_path
    os.makedirs(output_dir, exist_ok=True)
    images = convert_from_path(pdf_path, dpi=200)

    for i, image in enumerate(images):
        width, height = image.size
        if width > max_dim or height > max_dim:
            scale_factor = min(max_dim / width, max_dim / height)
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            image = image.resize((new_width, new_height))
        image_path = os.path.join(output_dir, f"page_{i+1}.png")
        image.save(image_path)
        print(f"Saved page {i+1} as {image_path} (size: {image.size})")

    print(f"Converted {len(images)} pages to PNG images")
    return True

def convert(pdf_path, output_dir, max_dim=1000):
    try:
        return convert_with_pdfium(pdf_path, output_dir, max_dim)
    except Exception as e1:
        try:
            return convert_with_pdf2image(pdf_path, output_dir, max_dim)
        except Exception as e2:
            print(f"Error converting PDF to images: {e1} / {e2}", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
        print("Usage: convert_pdf_to_images.py [input pdf] [output directory]")
        sys.exit(0 if (len(sys.argv) >= 2 and sys.argv[1] in ("-h", "--help")) else 1)
    pdf_path = sys.argv[1]
    output_directory = sys.argv[2]
    convert(pdf_path, output_directory)
