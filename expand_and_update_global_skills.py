"""Script to expand the Global Antigravity Skill Library with learned behaviors and advanced project skills.

Adds:
1. multimodal-vision-ocr-and-exam-ingestion
2. character-voiced-audio-synthesis
3. quantitative-intraday-backtesting-and-mfe
4. programmatic-svg-diagram-generation
5. academic-pdf-reportlab-engine
6. agentic-pair-programming-and-autonomous-debugging

Deploys to:
- C:\\Users\\spmad\\.gemini\\config\\skills\\
- D:\\AI SKILLS\\GLOBAL_SKILL_LIBRARY\\
"""
from __future__ import annotations

import os

GLOBAL_CONFIG_SKILLS = r"C:\Users\spmad\.gemini\config\skills"
LOCAL_LIBRARY_ROOT = r"D:\ANTIGRAVITY PROJECT FOLDER\AI SKILLS\GLOBAL_SKILL_LIBRARY"
GLOBAL_GEMINI_MD = r"C:\Users\spmad\.gemini\config\GEMINI.md"

NEW_SKILLS: dict[str, dict[str, str]] = {}

# ==============================================================================
# 1. MULTIMODAL VISION OCR & EXAM INGESTION
# ==============================================================================
NEW_SKILLS["multimodal-vision-ocr-and-exam-ingestion"] = {
    "name": "multimodal-vision-ocr-and-exam-ingestion",
    "description": (
        "Ingest, OCR, and align handwritten exam answer sheets, student notes, and scanned documents "
        "using multimodal Gemini Vision API with automatic fallback and schema alignment. Use when processing "
        "handwritten student submissions, mobile photo scans, or handwritten math/science test papers."
    ),
    "content": """# Multimodal Vision OCR, Handwritten Document Ingestion & Schema Alignment

## Overview
Originated from the Tharun ScholasticPulse project (`D:\\THARUN PROJECT\\exam_vision_ocr_engine_v3.py`), this skill details how to ingest raw camera photos, mobile scans, or PDF uploads of handwritten student work, extract handwritten text/math, and align responses question-by-question against a predefined structured JSON exam schema.

---

## 1. Multimodal Vision API Ingestion Architecture
To handle imperfect student mobile photos (variable lighting, rotation, shadows, crumpled paper):
1. **MIME-Type & Format Normalization**:
   - Convert multi-page PDF documents into high-DPI PNG pages ($300\\text{ DPI}$).
   - Ensure color JPEG/PNG images are base64-encoded or uploaded via the Files API.
2. **Dual-Model Fallback Cascade**:
   - Primary: `gemini-2.5-flash` for high-throughput, low-latency handwriting transcription.
   - Fallback: `gemini-1.5-pro` when handwriting exhibits severe cursive degradation, faint pencil marks, or dense mathematical fractions.

---

## 2. Rigid Question Alignment Prompt Template
When prompting the multimodal vision model, enforce deterministic JSON formatting:

```markdown
You are an expert academic handwriting transcription engine.
Examine this image of a handwritten exam answer sheet.

CRITICAL INSTRUCTIONS:
1. Identify every question number written by the student (e.g., 'Q.1', '1(a)', 'Ans 5').
2. Transcribe the student's exact handwritten text, equations, and diagrams. Do not correct mistakes.
3. For mathematical equations, transcribe into clean LaTeX format: \\( ... \\).
4. If a question is illegible or crossed out, mark 'is_scratched': true.

Output strictly valid JSON with this schema:
{
  "exam_id": "...",
  "page_number": 1,
  "confidence_score": 0.95,
  "responses": [
    {
      "question_id": "Q1",
      "student_answer_raw": "...",
      "equations_latex": ["..."],
      "rough_work_detected": true
    }
  ]
}
```

---

## 3. Schema Alignment & Error Resilience
- Match extracted `question_id` against the master Question Paper JSON schema.
- Flag unmapped answers (`ORPHAN_RESPONSE`) for manual teacher review.
- Persist aligned responses to disk under `EXAM_SYSTEM_V3/04_UPLOADED_ANSWER_SHEETS/<exam_id>_aligned.json`.
"""
}

# ==============================================================================
# 2. CHARACTER-VOICED AUDIO SYNTHESIS
# ==============================================================================
NEW_SKILLS["character-voiced-audio-synthesis"] = {
    "name": "character-voiced-audio-synthesis",
    "description": (
        "Generate character-voiced motivational audio, study reminders, and verbal walkthroughs "
        "using Edge TTS, SAPI, and PowerShell speech engines. Use when creating interactive study audio, "
        "pedagogical voice prompts, or habit-reinforcing verbal feedback."
    ),
    "content": """# Character-Voiced Audio Synthesis & Motivational Pacing

## Overview
Originated from the Tharun ScholasticPulse project (`D:\\THARUN PROJECT\\generate_naruto_audio.py`), this skill provides the mechanics for synthesizing character-driven audio prompts (e.g., Naruto Uzumaki, gentle academic coach) to eliminate procrastination, sustain student focus, and announce study checkpoints.

---

## 1. Speech Normalization for Natural Breathing
Raw text sounds robotic when synthesized directly. Apply phonetic speech preprocessing:
1. **Contraction Expansion**: Expand contractions (`"I'm"` $\\rightarrow$ `"I am"`, `"Let's"` $\\rightarrow$ `"Let us"`).
2. **Punctuation Pauses**: Insert ellipses (`...`) or commas before key affirmations to create natural oratorical pauses.
3. **Phonetic Spelling**: Spell out unfamiliar names phonetically (e.g., `"Dattebayo"` $\\rightarrow$ `"Dat-te-ba-yo"`).
4. **Volume & Pitch Modulation**: Set pitch to $+5\\text{Hz}$ to $+10\\text{Hz}$ and rate to $+10\\%$ for energetic character delivery.

---

## 2. Multi-Engine Synthesis Cascade
- **Edge TTS (Primary)**: High-fidelity neural voice synthesis (`en-US-GuyNeural`, `en-US-ChristopherNeural`, `en-IN-PrabhatNeural`).
- **PowerShell / SAPI Fallback (Offline)**:
  ```powershell
  Add-Type -AssemblyName System.Speech
  $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
  $synth.SelectVoice("Microsoft David Desktop")
  $synth.Rate = 1
  $synth.SetOutputToWaveFile("$PSScriptRoot\\assets\\quote.wav")
  $synth.Speak("I am not gonna run away! That is my ninja way!")
  $synth.Dispose()
  ```

---

## 3. Storage & Metadata Catalog
- Save audio assets to `<project_root>/assets/<voice_id>/<quote_id>.wav`.
- Accompany with an auditable JSON metadata index containing:
  - `character`, `role`, `theme`, `quote_text`, `speech_text`, `audio_file`, `duration_sec`.
"""
}

# ==============================================================================
# 3. QUANTITATIVE INTRADAY BACKTESTING & MFE
# ==============================================================================
NEW_SKILLS["quantitative-intraday-backtesting-and-mfe"] = {
    "name": "quantitative-intraday-backtesting-and-mfe",
    "description": (
        "Execute automated, high-frequency quantitative backtests of intraday timing nodes, "
        "price equilibrium pivots, and swing reversals using 1-minute OHLC market data, realistic volatility "
        "synthesis, and Maximum Favorable Excursion (MFE) metrics. Use when backtesting trading strategies."
    ),
    "content": """# Quantitative Intraday Backtesting & Maximum Favorable Excursion (MFE)

## Overview
Developed during the autonomous Gann Time Node backtest (`d:\\ephemeris\\run_gann_backtest.py`), this skill covers the end-to-end quantitative evaluation of intraday time-based trading models on high-frequency market data.

---

## 1. Data Acquisition & Resilient Ingestion
- **Real Market Data**: Fetch 1-minute bars using `yfinance` (`^NSEI`, `^NSEBANK`). Convert timestamps strictly to `Asia/Kolkata` (IST).
- **Synthetic Gap Filling**: If API request limits constrain the historical window (e.g., Yahoo Finance 7-8 day 1m limit), synthesize additional trading days using geometric Brownian motion with intraday volatility clustering:
  $$\\sigma_{\\text{open}} > \\sigma_{\\text{midday}} < \\sigma_{\\text{close}}$$
  Enforce standard session boundaries (`09:15` to `15:30` IST, exactly $375$ bars per day).

---

## 2. Pivot Window Evaluation Logic
For any target Time Node $T_{\\text{target}}$ (e.g., $13:56$ or $14:27$ IST):
1. **Evaluation Window**: Define a symmetric or asymmetric observation window around the node:
   - Window: $T_{\\text{target}} - 15\\text{ mins}$ to $T_{\\text{target}} + 30\\text{ mins}$.
2. **Swing Extrema Identification**:
   - $P_{\\text{High}} = \\max(\\text{High}_{\\text{window}})$, $t_{\\text{High}} = \\text{timestamp of } P_{\\text{High}}$
   - $P_{\\text{Low}} = \\min(\\text{Low}_{\\text{window}})$, $t_{\\text{Low}} = \\text{timestamp of } P_{\\text{Low}}$
3. **Rigid Hit Condition**:
   - A \"Swing Hit\" is confirmed if and only if:
     $$|t_{\\text{extremum}} - T_{\\text{target}}| \\le \\Delta t_{\\text{tolerance}} \\quad (\\text{e.g., } \\pm 3\\text{ minutes})$$

---

## 3. Maximum Favorable Excursion (MFE) Metric
Measure the quality of the reaction over a subsequent forward holding window (e.g., $30\\text{ minutes}$):
- **Short Setup** (High Hit):
  $$\\text{MFE} = \\text{Close}_{\\text{entry}} - \\min(\\text{Low}_{[t_{\\text{entry}}, t_{\\text{entry}} + 30\\text{m}]})$$
- **Long Setup** (Low Hit):
  $$\\text{MFE} = \\max(\\text{High}_{[t_{\\text{entry}}, t_{\\text{entry}} + 30\\text{m}]}) - \\text{Close}_{\\text{entry}}$$

---

## 4. Reporting Standards
Always report:
1. Total valid trading days analyzed.
2. Total confirmed Swing Hits at each node.
3. Hit Rate Percentage: $(\\text{Hits} / \\text{Total Days}) \\times 100\\%$.
4. Average and Median MFE Price Reaction (in underlying index points).
"""
}

# ==============================================================================
# 4. PROGRAMMATIC SVG & CONCEPT ARCHITECTURE DIAGRAMS
# ==============================================================================
NEW_SKILLS["programmatic-svg-diagram-generation"] = {
    "name": "programmatic-svg-diagram-generation",
    "description": (
        "Generate clean, responsive, publication-ready vector graphic (SVG) architecture diagrams "
        "in pure Python with drop shadows, marker arrows, and cohesive palette styling. "
        "Use when generating visual diagrams, workflow charts, and system blueprints without external GUI tools."
    ),
    "content": """# Programmatic SVG & System Architecture Diagram Generation

## Overview
Originated from the AI Mastery Masterclass textbook engine (`D:\\AI SKILLS\\AI-Mastery-Masterclass\\gen_diagrams.py`), this skill provides a pure-Python, zero-dependency blueprint for generating publication-quality Scalable Vector Graphics (SVG) diagrams.

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
        f'<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 {w} {h}\" width=\"{w}\" height=\"{h}\" font-family=\"Segoe UI, Arial, sans-serif\">'
        f'<defs>'
        f'  <marker id=\"arrow\" viewBox=\"0 0 10 10\" refX=\"9\" refY=\"5\" markerWidth=\"7\" markerHeight=\"7\" orient=\"auto-start-reverse\">'
        f'    <path d=\"M0,0 L10,5 L0,10 z\" fill=\"#334155\"/>'
        f'  </marker>'
        f'  <filter id=\"shadow\" x=\"-10%\" y=\"-10%\" width=\"120%\" height=\"130%\">'
        f'    <feDropShadow dx=\"0\" dy=\"2\" stdDeviation=\"2\" flood-opacity=\"0.15\"/>'
        f'  </filter>'
        f'</defs>'
        f'<rect width=\"{w}\" height=\"{h}\" fill=\"#ffffff\"/>'
        f'<text x=\"{w/2}\" y=\"34\" text-anchor=\"middle\" font-size=\"22\" font-weight=\"700\" fill=\"#334155\">{title}</text>'
    )

def make_card(x: int, y: int, w: int, h: int, color: str, light_bg: str, title: str, lines: list[str]) -> str:
    body = [
        f'<rect x=\"{x}\" y=\"{y}\" width=\"{w}\" height=\"{h}\" rx=\"12\" fill=\"{light_bg}\" stroke=\"{color}\" stroke-width=\"2.5\" filter=\"url(#shadow)\"/>',
        f'<text x=\"{x + w/2}\" y=\"{y + 32}\" text-anchor=\"middle\" font-size=\"16\" font-weight=\"700\" fill=\"{color}\">{title}</text>'
    ]
    for i, line in enumerate(lines):
        body.append(f'<text x=\"{x + w/2}\" y=\"{y + 58 + i*20}\" text-anchor=\"middle\" font-size=\"13\" fill=\"#334155\">{line}</text>')
    return \"\".join(body)

def make_arrow(x1: int, y1: int, x2: int, y2: int, label: str = \"\") -> str:
    s = f'<line x1=\"{x1}\" y1=\"{y1}\" x2=\"{x2}\" y2=\"{y2}\" stroke=\"#334155\" stroke-width=\"2.5\" marker-end=\"url(#arrow)\"/>'
    if label:
        s += f'<text x=\"{(x1+x2)/2}\" y=\"{(y1+y2)/2 - 8}\" text-anchor=\"middle\" font-size=\"12\" fill=\"#334155\" font-style=\"italic\">{label}</text>'
    return s
```
"""
}

# ==============================================================================
# 5. ACADEMIC PDF REPORTLAB ENGINE & FLOWABLES
# ==============================================================================
NEW_SKILLS["academic-pdf-reportlab-engine"] = {
    "name": "academic-pdf-reportlab-engine",
    "description": (
        "Architect and compile professional, multi-page academic textbooks and reports using ReportLab. "
        "Implement two-pass NumberedCanvas for dynamic 'Page X of Y' headers/footers, robust Table wrapping, "
        "and locked-file process recovery. Use when generating standalone PDF publications."
    ),
    "content": """# Academic PDF Architecture, ReportLab Flowables & Process Recovery

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
"""
}

# ==============================================================================
# 6. AGENTIC PAIR PROGRAMMING & AUTONOMOUS DEBUGGING
# ==============================================================================
NEW_SKILLS["agentic-pair-programming-and-autonomous-debugging"] = {
    "name": "agentic-pair-programming-and-autonomous-debugging",
    "description": (
        "Internalize the expert agent behavior protocol: execute silent self-correction, perform "
        "first-principles mathematical proofs, inspect Windows process locks and console encodings, enforce "
        "zero-hallucination rigor, and deliver deterministic verified artifacts. Use on all complex pair-programming tasks."
    ),
    "content": """# Agentic Pair Programming, Autonomous Debugging & Zero-Hallucination Behaviors

## Overview
This skill crystallizes the core agent behaviors, problem-solving habits, and debugging instincts proven across the Tharun Project, Google AI Mastery, and Gann Quantitative Trading ecosystems.

---

## 1. Silent Self-Correction & Zero-Hesitation Problem Solving
- **Never Throw Errors Back to the User**: When encountering runtime exceptions (e.g., `PermissionError: [Errno 13]`, `UnicodeEncodeError: 'charmap'`, missing packages, or missing font glyphs), immediately diagnose the underlying operating system or library cause.
- **Inspect System State**: Check active processes (`Get-Process`), font `cmap` tables (`fontTools`), or character encodings (`sys.stdout.reconfigure(encoding='utf-8')`).
- Resolve the roadblock programmatically, recompile the asset, and verify before responding.

---

## 2. First-Principles Mathematical Verification
- **Never Guess or Hallucinate Formulas**:
  - Every calculation (Gann Square of Nine spiral root modulo 2, Spencer Equation of Time series, Bloom's cognitive distribution, MFE excursions) must be grounded in verified mathematical and physical laws.
  - When in doubt, derive the formula step-by-step and write an automated unit test script in `scratch/` to verify numerical accuracy against known historical test cases.

---

## 3. Strict Deterministic Verification Before Declaring Done
Before presenting any work as completed:
1. Verify the process exit code (`code == 0`).
2. Verify output file existence, non-zero file size, and timestamp on disk.
3. For documents: Inspect text streams using `pypdf` to ensure 0 tofu square boxes (`□`), 0 replacement characters (`\\ufffd`), and proper header/footer alignment.
4. Provide immediate, clickable markdown file links (`file:///...`) using forward slashes for Windows compatibility.

---

## 4. Continuous Knowledge Capture Flywheel
At the conclusion of every project or complex problem resolution:
- Formalize the learned workflow into a `SKILL.md` package.
- Install directly to `C:\\Users\\spmad\\.gemini\\config\\skills\\` and mirror to `D:\\AI SKILLS\\GLOBAL_SKILL_LIBRARY\\`.
- Keep the global Antigravity library perpetually synchronized.
"""
}


def install_all():
    print(f"Deploying {len(NEW_SKILLS)} new specialized skills...")
    for skill_name, data in NEW_SKILLS.items():
        # Destination 1: Global Config Skills
        global_path = os.path.join(GLOBAL_CONFIG_SKILLS, skill_name)
        os.makedirs(global_path, exist_ok=True)
        global_file = os.path.join(global_path, "SKILL.md")

        # Destination 2: Local Drive D Library
        local_path = os.path.join(LOCAL_LIBRARY_ROOT, skill_name)
        os.makedirs(local_path, exist_ok=True)
        local_file = os.path.join(local_path, "SKILL.md")

        full_content = (
            f"---\n"
            f"name: {data['name']}\n"
            f"description: >-\n  {data['description']}\n"
            f"---\n\n"
            f"{data['content'].strip()}\n"
        )

        with open(global_file, "w", encoding="utf-8") as f:
            f.write(full_content)

        with open(local_file, "w", encoding="utf-8") as f:
            f.write(full_content)

        print(f"  [OK] Installed: {skill_name}")

    # Update README
    readme_path = os.path.join(LOCAL_LIBRARY_ROOT, "README.md")
    readme_content = f"""# Unified Global AI Skill Library
### Central Cross-Project Repository for Google Antigravity & Gemini Agents

This library consolidates and standardizes all specialized skills, academic rubrics, quantitative formulas, learned agent behaviors, and autonomous workflows developed across:
1. **Tharun ScholasticPulse Project** (`D:\\THARUN PROJECT`)
2. **Google AI Mastery Masterclass** (`D:\\AI SKILLS\\AI-Mastery-Masterclass`)
3. **W.D. Gann Astrological Ephemeris & Trading** (`D:\\ephemeris`)

---

## Complete Active Skills Index (21 Total Global Skills)

### A. Tharun Academic Engine & Document Processing
1. **`tharun-academic-evaluation-and-rubrics`**: CBSE Question Framing, Bloom's Taxonomy, Step Marking Rubrics, Anti-Daydreaming Architecture.
2. **`academic-paper-typesetting-and-math-preview`**: ISO A4 page geometry, institutional headers, right-aligned mark brackets, KaTeX math preview.
3. **`mathematical-typography-and-font-rectification`**: Font cmap auditing, replacing unmapped Unicode characters (∈, ⌊, ⌋, ⇒) to eliminate tofu boxes (□).
4. **`multimodal-vision-ocr-and-exam-ingestion`**: Vision OCR for handwritten student papers, multimodal Gemini Vision fallback, schema alignment.
5. **`character-voiced-audio-synthesis`**: Edge TTS, PowerShell SAPI speech synthesis, phonetic normalization, motivational audio prompts.
6. **`desktop-application-packaging-and-shortcuts`**: PyInstaller packaging, silent VBS launchers, and PowerShell desktop shortcuts.

### B. Google AI Mastery & Visual Architecture
7. **`google-gemini-research-mastery`**: Deep research, NotebookLM grounding, 5-part prompt anatomy, and context window economics.
8. **`agentic-tool-integrations-and-mcp`**: Model Context Protocol (MCP), API integration, webhooks, and tool error recovery.
9. **`antigravity-customization-engineering`**: Authoring skills, workspace rules, plugins, and progressive disclosure.
10. **`autonomous-software-development-loop`**: The 5-phase agent loop (Plan, Act, Verify, Self-Correct, Document).
11. **`programmatic-svg-diagram-generation`**: Pure-Python SVG vector graphics, drop-shadow filters, marker arrows, and responsive card geometry.

### C. Gann Astrological Trading & High-Frequency Quantitative Engineering
12. **`gann-astro-data-retrieval`**: NASA JPL Horizons REST API geocentric queries, DE440/DE441, celestial coordinates.
13. **`gann-temporal-exchange-alignment`**: UTC/UT to IST (+05:30) conversion, aligning celestial events to Indian exchange sessions.
14. **`gann-market-harmonics-and-square-of-nine`**: The Law of Vibration, Square of Nine spiral root math, planetary degree-to-price mapping.
15. **`gann-intraday-session-midpoint-analysis`**: 50% price equilibrium, session midpoint squaring, Spencer Equation of Time solar noon.
16. **`quantitative-intraday-backtesting-and-mfe`**: Algorithmic backtesting of high-frequency intraday time nodes, yfinance data handling, synthetic OHLC simulation, and Maximum Favorable Excursion (MFE) metrics.
17. **`indian-market-instrument-filtering`**: Routing triggers to NSE Nifty 50 and MCX Energy/Base Metals with strict bullion exclusion.

### D. Production Publishing & Agent Behaviors
18. **`academic-pdf-reportlab-engine`**: Multi-page PDF architecture, two-pass NumberedCanvas (Page X of Y), table auto-wrap flowables, and locked-file process handling.
19. **`agentic-pair-programming-and-autonomous-debugging`**: Core agent behavior protocol: first-principles derivation, silent self-correction, OS process debugging, and zero-hallucination delivery.
20. **`project-skill-harvesting-and-library-sync`**: Continuous learning protocol that extracts end-of-project capabilities and syncs them globally.
21. **`fullstack-development`**: End-to-end fullstack TypeScript, React, and Node.js web development.

---

## Global Discovery & Auto-Loading Architecture
- **Global Discovery Root**: `C:\\Users\\spmad\\.gemini\\config\\skills\\`
- All skills in this library are installed into Antigravity's machine-local global discovery folder.
- **Every new project or workspace opened in Antigravity automatically discovers and loads all 21 skills!**
- The global rule `C:\\Users\\spmad\\.gemini\\config\\GEMINI.md` mandates that at the end of every project, newly learned capabilities are automatically added to this library.
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"  [OK] Updated README at: {readme_path}")


if __name__ == "__main__":
    install_all()
