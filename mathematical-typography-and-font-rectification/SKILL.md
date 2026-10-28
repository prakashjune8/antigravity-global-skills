---
name: mathematical-typography-and-font-rectification
description: >-
  Prevent and rectify tofu/box glyph anomalies (□) in PDF generation and ReportLab engines. Audit Windows TrueType font cmap tables, replace unmapped Unicode characters (∈, ⌊, ⌋, ⇒) with fully supported academic notations, and enforce rigorous mathematical typesetting.
---

# Mathematical Typography, Font Cmap Auditing & Tofu Rectification

## Overview
Developed through extensive work on the Tharun project and the Gann Astrological Trading textbook generation engines, this skill details how to prevent, diagnose, and permanently fix tofu/square box anomalies (`□` / `U+25A1` / `U+FFFD`) in PDF generation libraries (such as ReportLab) and print typesetting.

---

## 1. The Root Cause of Tofu / Box Anomalies (`□`)
- When generating PDFs using system TrueType fonts (such as Windows `segoeui.ttf`, `arial.ttf`, or `times.ttf`), the font's internal `cmap` table determines character support.
- While standard fonts support Greek letters ($	heta, \lambda, \omega, \pi, \Delta$), basic arithmetic ($	imes, \pm, \le, \ge, \sqrt{}$), and degree symbols ($^\circ$), they **consistently lack glyph definitions** for:
  - Set theory membership: `∈` (`U+2208`)
  - Ceiling and Floor brackets: `⌊` (`U+230A`), `⌋` (`U+230B`), `⌈` (`U+2308`), `⌉` (`U+2309`)
  - Double implications: `⇒` (`U+21D2`), `⇔` (`U+21D4`)
  - Astrological & Misc Symbols: `☌`, `☍`, `△`, `★`, `✓`
- When ReportLab or PDF engines encounter an unmapped codepoint, they fail silently and output the font's fallback missing character glyph (`□`).

---

## 2. Programmatic Font `cmap` Audit Script
Before compiling any document with mathematical or astrological symbols, run this audit:

```python
from fontTools.ttLib import TTFont

def audit_text_glyphs(text: str, font_path: str = r"C:\Windows\Fonts\segoeui.ttf") -> set[str]:
    font = TTFont(font_path)
    cmap = font.getBestCmap()
    missing = {char for char in text if ord(char) not in cmap and ord(char) > 127}
    return missing
```

---

## 3. Rigid Mathematical Glyph Substitution Matrix
Always replace unmapped Unicode characters with fully supported academic equivalents:

| Unsupported Glyph | Unicode | Universal Supported Replacement | Meaning / Context |
| :--- | :--- | :--- | :--- |
| `∈` | `U+2208` | `where 0° ≤ θ < 360°` or `in` | Set membership |
| `⌊` `⌋` | `U+230A` / `U+230B` | `floor[ ... ]` | Integer floor division |
| `⌈` `⌉` | `U+2308` / `U+2309` | `ceil[ ... ]` | Integer ceiling |
| `⇒` | `U+21D2` | `→` (`U+2192`) or `yields` | Implication / mapping |
| `☌` | `U+260C` | `Conjunction (0°)` | 0° planetary alignment |
| `☍` | `U+260D` | `Opposition (180°)` | 180° planetary alignment |
| `△` | `U+25B3` | `Trine (120°)` | 120° harmonic aspect |
| `★` | `U+2605` | `[MID]` or `*` | Midpoint marker |
| `✓` | `U+2713` | `•` (`U+2022`) or `[OK]` | Checkmark / bullet |

---

## 4. Verification Protocol
1. Extract generated PDF text streams using `pypdf`:
   ```python
   import pypdf
   reader = pypdf.PdfReader("output.pdf")
   text = "".join(page.extract_text() for page in reader.pages)
   assert "\u25a1" not in text and "□" not in text and "\ufffd" not in text
   ```
2. Verify visual appearance: no isolated boxes appear adjacent to equations or limits.
