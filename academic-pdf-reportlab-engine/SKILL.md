---
name: academic-pdf-reportlab-engine
description: >-
  Architect and compile professional, multi-page academic textbooks and reports using ReportLab. Implement two-pass NumberedCanvas for dynamic 'Page X of Y' headers/footers, robust Table wrapping, and locked-file process recovery. Use when generating standalone PDF publications.
---

# Academic PDF Architecture, ReportLab Flowables & Process Recovery

## Overview
Developed across the Gann Ephemeris Textbook and AI Mastery publications, this skill formalizes the design of professional PDF documents in Python using ReportLab.

---

## 1. Two-Pass Numbered Canvas for Dynamic Page Totals
Standard single-pass ReportLab canvases cannot compute `Page X of Y` because total page count is unknown until compilation ends. Use a two-pass canvas pattern:

```python
from reportlab.pdfgen import canvas

class AcademicNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages: int):
        if self._pageNumber == 1:
            return  # Skip cover page
        self.saveState()
        self.setFont("SegoeUI", 8)
        self.setFillColorHex("#64748b")
        # Running header
        self.drawString(54, 11 * 72 - 36, "ACADEMIC TREATISE: W.D. GANN QUANTITATIVE FOUNDATIONS")
        # Running footer with dynamic page total
        self.drawRightString(8.5 * 72 - 54, 30, f"Page {self._pageNumber} of {total_pages}")
        self.restoreState()
```

---

## 2. Table Auto-Wrapping & KeepTogether Flowables
- Never place raw un-wrapped strings in ReportLab `Table` cells; long lines will clip or overflow the page boundary.
- Always wrap every text cell in a `Paragraph(..., body_style)`.
- Use `KeepTogether([heading, table])` to prevent orphaned headers at page bottoms.

---

## 3. Locked File Handling (`PermissionError: [Errno 13]`)
When a user has the target PDF open in an external viewer (e.g., Foxit Reader, Acrobat):
1. Detect file lock before compiling:
   ```python
   try:
       with open(pdf_path, 'a'): pass
   except PermissionError:
       # Write to fallback or close viewer process gracefully
       ...
   ```
2. Close viewer gracefully or write to `<name>_Rectified.pdf` to guarantee uninterrupted execution.
