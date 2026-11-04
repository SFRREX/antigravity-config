---
name: document-master
description: "Comprehensive master document processing suite for Microsoft Office and PDF files: programmatic creation, editing, formula modeling, formatting, conversion, and analysis across Word (.docx/.dotx), Excel (.xlsx/.xlsm/.csv), PowerPoint (.pptx/.potx), and PDF (.pdf) documents. Covers openpyxl formula models, docx-js / python-docx formatting, pptxgenjs slide presentations with native charts, pdfplumber / pypdf extraction, form filling, OCR, and headless LibreOffice conversion. Use whenever creating, manipulating, converting, or inspecting documents, spreadsheets, presentations, or PDFs. Do NOT use for frontend web apps, databases, or non-document software development."
license: Proprietary
---

# Master Document Processing & Office Engineering Suite

A unified, production-grade guide for creating, inspecting, editing, converting, and validating Microsoft Word (`.docx`), Excel (`.xlsx`), PowerPoint (`.pptx`), and Adobe PDF (`.pdf`) documents.

---

## 1. Quick Format Decision Matrix

| Deliverable | Recommended Engine | Primary Script / Library | Verification / Inspection |
|---|---|---|---|
| **Word Document (`.docx`)** | `docx` (Node.js) or `python-docx` | `require('docx')` or `docx` Python | Unpack XML or convert to PDF for preview |
| **Word Redline / Comment** | Direct XML modification | `python scripts/comment.py` | `python scripts/office/validate.py` |
| **Excel Model (`.xlsx`)** | `openpyxl` (formulas) + `pandas` (data) | Python `openpyxl`, `pandas` | `python scripts/recalc.py` |
| **Slide Deck (`.pptx`)** | `pptxgenjs` (Node.js) | `require('pptxgenjs')` | `python scripts/office/validate.py` |
| **Slide Duplication / Mod** | XML cloning | `python scripts/add_slide.py` | `python scripts/thumbnail.py` |
| **PDF Extraction / Form** | `pdfplumber` / `pypdf` | Python `pypdf`, `pdfplumber` | `python scripts/extract_form_structure.py` |
| **Cross-Format Conversion** | Headless LibreOffice | `python scripts/office/soffice.py` | Headless PDF rendering & image diff |

> [!NOTE]
> All scripts referenced are located relative to this skill's `scripts/` directory:
> - Office Validation & Conversion: `scripts/office/`
> - Word Modification: `scripts/comment.py`, `scripts/merge_runs.py`, `scripts/accept_changes.py`
> - Excel Recalculation: `scripts/recalc.py`
> - PowerPoint Slide Tools: `scripts/add_slide.py`, `scripts/clean.py`, `scripts/thumbnail.py`
> - PDF Forms & Extraction: `scripts/extract_form_structure.py`, `scripts/fill_fillable_fields.py`

---

## 2. Microsoft Word (`.docx` / `.dotx`) Engineering

A `.docx` file is a ZIP archive containing XML parts (primarily `word/document.xml`).

### 2.A Document Creation with docx-js (Node.js)
Install if not present: `npm install docx`

```javascript
const { Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell, WidthType, BorderStyle } = require("docx");
const fs = require("fs");

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 }, // US Letter (DXA: 1440 = 1 inch). For A4: 11906 x 16838
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    children: [
      new Paragraph({ text: "Executive Summary", heading: HeadingLevel.HEADING_1 }),
      new Paragraph({
        children: [
          new TextRun("This report outlines quarterly operational and financial performance. "),
          new TextRun({ text: "Key metrics exceeded projections.", bold: true })
        ]
      })
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => fs.writeFileSync("report.docx", buffer));
```

#### Critical Word Formatting Rules:
- **Dimensions in DXA**: Word uses DXA (1/20 of a point; 1440 DXA = 1 inch; 567 DXA = 1 cm).
- **Dual Column Widths**: When creating tables, set `columnWidths` on the `Table` AND explicit `width` on every `TableCell` using `WidthType.DXA`. The cell widths must sum exactly to the table width.
- **Table Shading**: Use `ShadingType.CLEAR` with fill color, never `ShadingType.SOLID` (renders completely black).
- **Never insert `\n`**: Always create distinct `Paragraph` instances for line breaks.
- **PageBreak**: Must always reside inside a `Paragraph` element (`new Paragraph({ children: [new PageBreak()] })`).
- **Lists & Bullets**: Never use literal unicode bullets (`•`). Use `numbering` configuration with `LevelFormat.BULLET`.

### 2.B Modifying Existing Word Documents (XML In-Place)
When editing existing `.docx` files without destroying document styles:
```bash
# 1. Unpack archive (cross-platform):
python -m zipfile -e input.docx unpacked/

# 2. Coalesce fragmented XML runs so text can be accurately searched and replaced:
python scripts/merge_runs.py unpacked/

# 3. Edit unpacked/word/document.xml in-place (do NOT reformat or pretty-print XML)

# 4. Add tracked comments or author redlines if requested:
python scripts/comment.py unpacked/ "Reviewed budget assumptions" --author "Antigravity"

# 5. Repack archive (Windows PowerShell / Python):
python -c "import zipfile, os; z = zipfile.ZipFile('output.docx', 'w', zipfile.ZIP_DEFLATED); [z.write(os.path.join(r, f), os.path.relpath(os.path.join(r, f), 'unpacked')) for r, d, fs in os.walk('unpacked') for f in fs]; z.close()"

# 6. Validate XML integrity:
python scripts/office/validate.py output.docx --original input.docx
```

---

## 3. Microsoft Excel (`.xlsx` / `.xlsm`) Engineering

Install dependencies: `pip install openpyxl pandas`

### 3.A Formula Modeling Principles
- **Always write formulas, never hardcoded totals**: Write `ws['C10'] = '=SUM(C2:C9)'`, not the Python-computed sum. The workbook must remain interactive.
- **Formula naming in uppercase**: Use `=SUM()`, `=AVERAGE()`, `=VLOOKUP()`, `=XLOOKUP()`, `=INDEX(..., MATCH(...))`.
- **Zero formula errors**: Check every cell for `#REF!`, `#VALUE!`, `#NAME?`, or `#DIV/0!`.
- **Document source and inputs**: Clearly mark input cells with distinct background fills (e.g., light blue `#EBF1F5` or subtle cream `#FCFDFD`). Include a legend table indicating editable assumption cells.
- **Number formatting**: Explicitly format currency (`$#,##0.00`), percentages (`0.0%`), and dates (`YYYY-MM-DD`).

### 3.B Python openpyxl Generation Pattern
```python
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Financial Summary"

# Professional font styling
header_font = Font(name="Arial", size=11, bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
currency_format = "$#,##0"

headers = ["Department", "Q1 Budget", "Q2 Budget", "Total Allocated"]
ws.append(headers)

for col_num in range(1, len(headers) + 1):
    cell = ws.cell(row=1, column=col_num)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = Alignment(horizontal="center")

data = [
    ["Engineering", 125000, 140000],
    ["Design", 45000, 50000],
    ["Operations", 60000, 62000],
]

for row_idx, row_data in enumerate(data, start=2):
    ws.cell(row=row_idx, column=1, value=row_data[0])
    ws.cell(row=row_idx, column=2, value=row_data[1]).number_format = currency_format
    ws.cell(row=row_idx, column=3, value=row_data[2]).number_format = currency_format
    # Dynamic formula
    ws.cell(row=row_idx, column=4, value=f"=SUM(B{row_idx}:C{row_idx})").number_format = currency_format

# Autofit column widths
for col in ws.columns:
    max_len = max(len(str(cell.value or '')) for cell in col)
    col_letter = get_column_letter(col[0].column)
    ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

wb.save("financial_summary.xlsx")
```

### 3.C Formula Recalculation
openpyxl writes formula text strings but does not precompute cached values.
To compute and cache values across all sheets before sharing:
```bash
python scripts/recalc.py financial_summary.xlsx
```
*(If LibreOffice is installed, `recalc.py` recalculates all cached results; otherwise, formulas evaluate automatically upon opening in Excel/Google Sheets).*

---

## 4. PowerPoint (`.pptx` / `.potx`) Presentation Engineering

Install if not present: `npm install pptxgenjs`

### 4.A Presentation Creation with pptxgenjs
```javascript
const pptxgen = require("pptxgenjs");
const pres = new pptxgen();

// Layout: 16:9 widescreen (13.33 x 7.5 inches)
pres.layout = "LAYOUT_WIDE";

// Slide 1: Title Slide
const slide1 = pres.addSlide();
slide1.background = { color: "0F172A" }; // Slate 900
slide1.addText("Quarterly Architecture Review", {
  x: 1.0, y: 2.5, w: 11.3, h: 1.2,
  fontSize: 40, bold: true, color: "F8FAFC", fontFace: "Arial"
});
slide1.addText("Antigravity Autonomous Systems", {
  x: 1.0, y: 3.8, w: 11.3, h: 0.8,
  fontSize: 20, color: "94A3B8", fontFace: "Arial"
});

// Slide 2: Metrics with Native Chart
const slide2 = pres.addSlide();
slide2.addText("Performance Throughput", { x: 0.8, y: 0.5, fontSize: 24, bold: true, color: "0F172A" });

const chartData = [
  { name: "Latency (ms)", labels: ["v1.0", "v1.2", "v2.0"], values: [420, 210, 85] }
];
slide2.addChart(pres.ChartType.bar, chartData, {
  x: 0.8, y: 1.5, w: 7.0, h: 4.5,
  barDir: "col",
  chartColors: ["2563EB"],
  showValue: true
});

// Speaker Notes
slide2.addNotes("Emphasize the 5x latency reduction achieved in the v2.0 release.");

pres.writeFile({ fileName: "presentation.pptx" });
```

#### PowerPoint Gotchas:
- **Never use `#` in hex colors**: Always write `color: "2563EB"`, never `"#2563EB"` (causes corrupt deck).
- **Set layout before adding slides**: `pres.layout = "LAYOUT_WIDE"` must precede any `addSlide()` calls.
- **Charts must be native**: Use `slide.addChart()` rather than rasterized images whenever possible.
- **Validate deck structure**: Run `python scripts/office/validate.py presentation.pptx`.

---

## 5. Adobe PDF (`.pdf`) Engineering

Install dependencies: `pip install pypdf pdfplumber reportlab pdf2image`

### 5.A Text & Tabular Data Extraction
```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for idx, page in enumerate(pdf.pages, start=1):
        print(f"--- Page {idx} ---")
        text = page.extract_text()
        print(text[:300]) # First 300 chars
        
        # Extract tables
        tables = page.extract_tables()
        for t_idx, table in enumerate(tables, start=1):
            print(f"Table {t_idx}:")
            for row in table:
                print(row)
```

### 5.B Merging, Splitting & Rotating Pages
```python
from pypdf import PdfReader, PdfWriter

# Merge multiple PDFs
writer = PdfWriter()
for pdf_file in ["cover.pdf", "body.pdf", "appendix.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("combined_output.pdf", "wb") as f:
    writer.write(f)

# Rotate specific page
reader = PdfReader("combined_output.pdf")
writer = PdfWriter()
for i, page in enumerate(reader.pages):
    if i == 0:
        page.rotate(90) # Clockwise
    writer.add_page(page)

with open("rotated_output.pdf", "wb") as f:
    writer.write(f)
```

### 5.C PDF Forms & Field Filling
For PDF forms, inspect structure and fill programmatic form fields:
```bash
# Inspect all form fields, types, and coordinates:
python scripts/extract_form_structure.py input_form.pdf

# Fill detected fillable fields from JSON payload:
python scripts/fill_fillable_fields.py input_form.pdf fields_data.json output_filled.pdf
```
*(See [references/pdf_forms.md](references/pdf_forms.md) and [references/pdf_reference.md](references/pdf_reference.md) for coordinate calculations and bounding box validation).*

---

## 6. Cross-Format Conversion & Verification

### Headless LibreOffice Conversion
To convert any Office file (`.docx`, `.xlsx`, `.pptx`) directly to PDF:
```bash
python scripts/office/soffice.py --headless --convert-to pdf document.docx
```

### Render PDF Pages to Images for Visual Inspection
```bash
# Render first page to PNG for visual inspection
python scripts/convert_pdf_to_images.py document.pdf --output-dir ./rendered_pages --dpi 150
```

### Package Schema Validation
Always run schema validation on generated or edited Office documents:
```bash
python scripts/office/validate.py output.docx
python scripts/office/validate.py presentation.pptx
```
