---
name: academic-paper-typesetting-and-math-preview
description: >-
  Format high-DPI academic question papers and documents adhering to ISO A4 geometry, CBSE institutional headers, flush-right mark brackets, and responsive KaTeX/HTML previews. Use when generating printable tests, worksheets, or academic layouts.
---

# Academic Paper Typesetting, Page Geometry & KaTeX Layout

## Overview
Originating from the Tharun ScholasticPulse examination suite, this skill provides rigid formatting rules for producing professional, high-DPI printable question papers and online HTML/KaTeX math previews.

---

## 1. Page Geometry & Physical Margin Standards (ISO A4)
To ensure zero clipping and allow binder punching:
- **Sheet Dimensions**: $210\text{ mm} \times 297\text{ mm}$ (A4).
- **Top Margin**: $16\text{ mm}$ ($45\text{ pt}$).
- **Bottom Margin**: $16\text{ mm}$ ($45\text{ pt}$).
- **Left Margin**: $18\text{ mm}$ ($51\text{ pt}$) (Dedicated gutter for staple/spiral binding).
- **Right Margin**: $16\text{ mm}$ ($45\text{ pt}$).
- **Standard Typography**: Serif fonts (`Times New Roman`, `DejaVu Serif`, `STIX Two Text`) at $10.5\text{ pt}$ body size with $14\text{ pt}$ line leading.

---

## 2. Institutional Header Block Architecture
Every paper must open with the official institutional metadata grid:
```html
<div class="exam-header-block">
  <div class="inst-title">INSTITUTION / ACADEMIC BOARD</div>
  <div class="inst-subtitle">ACADEMIC AFFILIATION • HOST EXAMINATION SYSTEM</div>
  <div class="exam-type-pill">ACADEMIC EVALUATION & RETENTION SPRINT</div>
  
  <div class="exam-meta-grid">
    <div><strong>CLASS:</strong> [Class Name]</div>
    <div><strong>SUBJECT:</strong> [Subject]</div>
    <div><strong>DATE:</strong> [DD-MM-YYYY]</div>
    <div><strong>TIME ALLOWED:</strong> [Minutes]</div>
    <div><strong>EXAM PHASE:</strong> [Test Name]</div>
    <div><strong>MAX. MARKS:</strong> [Marks]</div>
  </div>
</div>
```

---

## 3. Right-Aligned Mark Bracket Mechanics
Mark allocations must be positioned flush against the right-hand boundary to prevent cognitive clutter:
- Format strictly as `[1]`, `[2]`, `[3]`, `[5]`.
- For sub-questions:
  ```text
  Q.12 (a) State the Work-Energy Theorem with an example.                     [2]
       (b) Calculate the kinetic energy of a 2 kg body moving at 10 m/s.      [2]
       (c) What is the SI unit of work?                                       [1]
  ```
- In CSS / Flexbox: use `display: flex; justify-content: space-between; align-items: flex-start;`.

---

## 4. KaTeX Math Preview Integration
- Always wrap inline math in `\( ... \)` and display equations in `\[ ... \]`.
- Ensure delimiters are loaded before calling `renderMathInElement(document.body)`.
- Never use unescaped raw currency symbols (`$`) in text paragraphs as they corrupt math parsers.
