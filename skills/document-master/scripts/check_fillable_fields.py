#!/usr/bin/env python3
import sys
from pypdf import PdfReader

def check_fillable(pdf_path):
    reader = PdfReader(pdf_path)
    if reader.get_fields():
        print("This PDF has fillable form fields")
        return True
    else:
        print("This PDF does not have fillable form fields; you will need to visually determine where to enter data")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: check_fillable_fields.py <input.pdf>")
        sys.exit(0 if (len(sys.argv) == 2 and sys.argv[1] in ("-h", "--help")) else 1)
    check_fillable(sys.argv[1])
