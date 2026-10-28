---
name: programmatic-svg-diagram-generation
description: >-
  Generate clean, responsive, publication-ready vector graphic (SVG) architecture diagrams in pure Python with drop shadows, marker arrows, and cohesive palette styling. Use when generating visual diagrams, workflow charts, and system blueprints without external GUI tools.
---

# Programmatic SVG & System Architecture Diagram Generation

## Overview
Originated from the AI Mastery Masterclass textbook engine (`D:\AI SKILLS\AI-Mastery-Masterclass\gen_diagrams.py`), this skill provides a pure-Python, zero-dependency blueprint for generating publication-quality Scalable Vector Graphics (SVG) diagrams.

---

## 1. Design System & Palette Specification
Always maintain high visual contrast and modern corporate aesthetics:
- **Base Slate**: `#334155` (text, borders, default markers)
- **Primary Blue**: `#1a73e8` (bg: `#e8f0fe`)
- **Accent Violet**: `#7c3aed` (bg: `#f1eafe`)
- **Accent Teal**: `#0d9488` (bg: `#e0f5f2`)
- **Accent Amber**: `#d97706` (bg: `#fef3e2`)
- **Accent Green**: `#16a34a` (bg: `#e7f7ec`)
- **Font Stack**: `'Segoe UI', Arial, sans-serif`

---

## 2. Core Python SVG Generator Functions
```python
import pathlib

def make_svg_header(w: int, h: int, title: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" font-family="Segoe UI, Arial, sans-serif">'
        f'<defs>'
        f'  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'    <path d="M0,0 L10,5 L0,10 z" fill="#334155"/>'
        f'  </marker>'
        f'  <filter id="shadow" x="-10%" y="-10%" width="120%" height="130%">'
        f'    <feDropShadow dx="0" dy="2" stdDeviation="2" flood-opacity="0.15"/>'
        f'  </filter>'
        f'</defs>'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>'
        f'<text x="{w/2}" y="34" text-anchor="middle" font-size="22" font-weight="700" fill="#334155">{title}</text>'
    )

def make_card(x: int, y: int, w: int, h: int, color: str, light_bg: str, title: str, lines: list[str]) -> str:
    body = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{light_bg}" stroke="{color}" stroke-width="2.5" filter="url(#shadow)"/>',
        f'<text x="{x + w/2}" y="{y + 32}" text-anchor="middle" font-size="16" font-weight="700" fill="{color}">{title}</text>'
    ]
    for i, line in enumerate(lines):
        body.append(f'<text x="{x + w/2}" y="{y + 58 + i*20}" text-anchor="middle" font-size="13" fill="#334155">{line}</text>')
    return "".join(body)

def make_arrow(x1: int, y1: int, x2: int, y2: int, label: str = "") -> str:
    s = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#334155" stroke-width="2.5" marker-end="url(#arrow)"/>'
    if label:
        s += f'<text x="{(x1+x2)/2}" y="{(y1+y2)/2 - 8}" text-anchor="middle" font-size="12" fill="#334155" font-style="italic">{label}</text>'
    return s
```
