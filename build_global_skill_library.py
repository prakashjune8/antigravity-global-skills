"""Script to generate and synchronize the Global Antigravity Skill Library.

Extracts, structures, and deploys skills across:
1. Tharun Project (ScholasticPulse, CBSE Evaluation, Typesetting, Math Typography, Desktop Packaging)
2. Google AI Mastery (Research, MCP Tools, Antigravity Customization, Autonomous Software Loop)
3. Gann Astrological Trading (Astro Retrieval, Temporal Alignment, Harmonics/Square-of-Nine, Midpoints, Market Filtering)
4. Meta-Automation (Auto-Harvesting & Library Synchronization)

Installs directly into:
- Global Antigravity Discovery Root: C:\\Users\\spmad\\.gemini\\config\\skills\\
- Physical Central Library: D:\\AI SKILLS\\GLOBAL_SKILL_LIBRARY\\
- Global Antigravity Workspace Directive: C:\\Users\\spmad\\.gemini\\config\\GEMINI.md
"""
from __future__ import annotations

import os
import shutil
import sys

GLOBAL_CONFIG_SKILLS = r"C:\Users\spmad\.gemini\config\skills"
LOCAL_LIBRARY_ROOT = r"D:\AI SKILLS\GLOBAL_SKILL_LIBRARY"
GLOBAL_GEMINI_MD = r"C:\Users\spmad\.gemini\config\GEMINI.md"

SKILLS_DEFINITIONS: dict[str, dict[str, str]] = {}

# ==============================================================================
# 1. THARUN PROJECT SKILLS
# ==============================================================================

SKILLS_DEFINITIONS["tharun-academic-evaluation-and-rubrics"] = {
    "name": "tharun-academic-evaluation-and-rubrics",
    "description": (
        "Design CBSE-compliant question papers, step-wise evaluation rubrics, Bloom's taxonomy "
        "distributions, and anti-daydreaming test architectures. Use when structuring student assessments, "
        "generating model answer schemes, or evaluating academic answer sheets."
    ),
    "content": """# CBSE Academic Evaluation, Question Framing & Step-Marking Rubrics

## Overview
This skill originates from the **Tharun ScholasticPulse Project** (`D:\\THARUN PROJECT`), an advanced academic evaluation engine designed for Class 8-12 CBSE curricula. It provides deterministic guidelines for framing question papers, allocating cognitive levels across Bloom's Taxonomy, enforcing step-wise grading rubrics, and tracking recurring student mistakes via an Error Bank.

---

## 1. Bloom's Taxonomy Cognitive Distribution
Every structured test paper must balance difficulty according to institutional standards:
- **Remembering & Understanding (35% to 40%)**: Definitions, factual recall, direct formula statements, unit identification.
- **Applying (30% to 35%)**: Direct numerical problems, standard grammatical transformations, step-wise arithmetic proofs.
- **Analyzing & Evaluating (20% to 25%)**: Multi-step word problems, error identification, comparative analysis.
- **Creating / High-Order Thinking (HOTs) (5% to 10%)**: Unseen synthesis, real-world case studies, geometric deduction.

---

## 2. 4-Tier Institutional Section Architecture
Standard examination papers must strictly follow the four-section structure:
1. **Section A (1 Mark)**: Objective Multiple Choice Questions (MCQs) and Assertion-Reasoning. Focus on rapid concept verification.
2. **Section B (2 Marks)**: Very Short Answer (VSA). 2 distinct conceptual steps or 2 calculation points.
3. **Section C (3 Marks)**: Short Answer (SA). Exactly 3 marked milestones: Formula Statement ($1/2$ mark), Step substitution ($1\\frac{1}{2}$ marks), Final value with SI units ($1$ mark).
4. **Section D (5 Marks)**: Long Answer & Case Studies. Multi-part questions subdivided into $(a)[2], (b)[2], (c)[1]$ or clear rubric milestones.

---

## 3. CBSE Step-Marking Rubric Standards
Never assign holistic single-grade marks to subjective or numerical answers. Split every question into auditable steps:
- **Formula & Diagram**: Explicit statement of base theorem or labeled figure ($0.5$ - $1.0$ mark).
- **Substitution & Expansion**: Clean algebraic substitution with given values ($1.0$ - $2.0$ marks).
- **Arithmetic Simplification**: Intermediate operational accuracy ($1.0$ mark).
- **Final Answer & Units**: Value boxed or underlined with mandatory SI/metric unit ($0.5$ - $1.0$ mark). Zero marks for correct number if unit is omitted or erroneous.

---

## 4. Student Error Bank & Anti-Daydreaming Loop
- Track every point deduction in a `student_error_bank.json` under one of three flags:
  1. `CONCEPTUAL_GAP`: Failure to recall theorem or formula.
  2. `CALCULATION_SLIP`: Arithmetic, sign ($+ / -$), or decimal point error.
  3. `FORMAT_OMISSION`: Missing units, missing rough work, or omitted final statement.
- Use time-boxing checkpoints (e.g., 45-minute sprint followed by immediate step-wise audit) to maintain engagement and eliminate daydreaming.
"""
}

SKILLS_DEFINITIONS["academic-paper-typesetting-and-math-preview"] = {
    "name": "academic-paper-typesetting-and-math-preview",
    "description": (
        "Format high-DPI academic question papers and documents adhering to ISO A4 geometry, "
        "CBSE institutional headers, flush-right mark brackets, and responsive KaTeX/HTML previews. "
        "Use when generating printable tests, worksheets, or academic layouts."
    ),
    "content": """# Academic Paper Typesetting, Page Geometry & KaTeX Layout

## Overview
Originating from the Tharun ScholasticPulse examination suite, this skill provides rigid formatting rules for producing professional, high-DPI printable question papers and online HTML/KaTeX math previews.

---

## 1. Page Geometry & Physical Margin Standards (ISO A4)
To ensure zero clipping and allow binder punching:
- **Sheet Dimensions**: $210\\text{ mm} \\times 297\\text{ mm}$ (A4).
- **Top Margin**: $16\\text{ mm}$ ($45\\text{ pt}$).
- **Bottom Margin**: $16\\text{ mm}$ ($45\\text{ pt}$).
- **Left Margin**: $18\\text{ mm}$ ($51\\text{ pt}$) (Dedicated gutter for staple/spiral binding).
- **Right Margin**: $16\\text{ mm}$ ($45\\text{ pt}$).
- **Standard Typography**: Serif fonts (`Times New Roman`, `DejaVu Serif`, `STIX Two Text`) at $10.5\\text{ pt}$ body size with $14\\text{ pt}$ line leading.

---

## 2. Institutional Header Block Architecture
Every paper must open with the official institutional metadata grid:
```html
<div class=\"exam-header-block\">
  <div class=\"inst-title\">INSTITUTION / ACADEMIC BOARD</div>
  <div class=\"inst-subtitle\">ACADEMIC AFFILIATION • HOST EXAMINATION SYSTEM</div>
  <div class=\"exam-type-pill\">ACADEMIC EVALUATION & RETENTION SPRINT</div>
  
  <div class=\"exam-meta-grid\">
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
- Always wrap inline math in `\\( ... \\)` and display equations in `\\[ ... \\]`.
- Ensure delimiters are loaded before calling `renderMathInElement(document.body)`.
- Never use unescaped raw currency symbols (`$`) in text paragraphs as they corrupt math parsers.
"""
}

SKILLS_DEFINITIONS["mathematical-typography-and-font-rectification"] = {
    "name": "mathematical-typography-and-font-rectification",
    "description": (
        "Prevent and rectify tofu/box glyph anomalies (□) in PDF generation and ReportLab engines. "
        "Audit Windows TrueType font cmap tables, replace unmapped Unicode characters (∈, ⌊, ⌋, ⇒) with "
        "fully supported academic notations, and enforce rigorous mathematical typesetting."
    ),
    "content": """# Mathematical Typography, Font Cmap Auditing & Tofu Rectification

## Overview
Developed through extensive work on the Tharun project and the Gann Astrological Trading textbook generation engines, this skill details how to prevent, diagnose, and permanently fix tofu/square box anomalies (`□` / `U+25A1` / `U+FFFD`) in PDF generation libraries (such as ReportLab) and print typesetting.

---

## 1. The Root Cause of Tofu / Box Anomalies (`□`)
- When generating PDFs using system TrueType fonts (such as Windows `segoeui.ttf`, `arial.ttf`, or `times.ttf`), the font's internal `cmap` table determines character support.
- While standard fonts support Greek letters ($\theta, \lambda, \omega, \pi, \Delta$), basic arithmetic ($\times, \pm, \le, \ge, \\sqrt{}$), and degree symbols ($^\\circ$), they **consistently lack glyph definitions** for:
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

def audit_text_glyphs(text: str, font_path: str = r"C:\\Windows\\Fonts\\segoeui.ttf") -> set[str]:
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
   assert "\\u25a1" not in text and "□" not in text and "\\ufffd" not in text
   ```
2. Verify visual appearance: no isolated boxes appear adjacent to equations or limits.
"""
}

SKILLS_DEFINITIONS["desktop-application-packaging-and-shortcuts"] = {
    "name": "desktop-application-packaging-and-shortcuts",
    "description": (
        "Package Python applications (CustomTkinter, PyQt, Electron, or Flask/WebView) into standalone "
        "Windows executables with PyInstaller, embed custom assets/icons, generate silent VBS launchers, "
        "and automate desktop shortcut creation. Use when shipping desktop software to end users."
    ),
    "content": """# Desktop Application Packaging, Silent Launchers & Windows Shortcuts

## Overview
Derived from both the Tharun ScholasticPulse and Gann Ephemeris desktop deployments, this skill provides a complete recipe for compiling Python applications into standalone, single-executable Windows binaries with high-DPI desktop shortcuts and silent launching.

---

## 1. PyInstaller Build Script Pattern
Avoid fragile command-line invocations by using a dedicated `.spec` file or automated Python build script:

```python
import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'main.py',
    '--name=MyDesktopApp',
    '--noconsole',
    '--onefile',
    '--icon=assets/app_icon.ico',
    '--add-data=assets;assets',
    '--clean'
])
```

---

## 2. Silent VBS Launcher Pattern (`LAUNCH_SILENT.vbs`)
When launching a Python background server or non-console script without displaying an unwanted black Command Prompt window:

```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "pythonw.exe main.py", 0, False
Set WshShell = Nothing
```

---

## 3. Automated Windows Desktop Shortcut Script (PowerShell)
Provide an automated shortcut creator (`CREATE_DESKTOP_SHORTCUT.ps1`):

```powershell
$WshShell = New-Object -ComObject WScript.Shell
$DesktopPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::Desktop)
$ShortcutPath = Join-Path -Path $DesktopPath -ChildPath "My Desktop App.lnk"
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)
$Shortcut.TargetPath = "$PSScriptRoot\\dist\\MyDesktopApp.exe"
$Shortcut.WorkingDirectory = "$PSScriptRoot"
$Shortcut.IconLocation = "$PSScriptRoot\\assets\\app_icon.ico"
$Shortcut.Description = "Launch My Desktop Application"
$Shortcut.Save()
Write-Host "Desktop shortcut created successfully at: $ShortcutPath"
```
"""
}

# ==============================================================================
# 2. GOOGLE AI MASTERY SKILLS
# ==============================================================================

SKILLS_DEFINITIONS["google-gemini-research-mastery"] = {
    "name": "google-gemini-research-mastery",
    "description": (
        "Master Level 1 AI research workflows: execute deep research synthesis, ground models using "
        "NotebookLM source constraints, construct high-accuracy multi-part prompts, and manage context windows. "
        "Use when researching complex technical subjects, synthesizing literature, or preventing AI hallucinations."
    ),
    "content": """# Google Gemini & Deep Research Mastery

## Overview
Synthesized from **Chapter 1 of The 5 Levels of AI Mastery**, this skill formalizes structured prompt anatomy, source-grounded research (NotebookLM), context window economics, and cross-verification techniques.

---

## 1. The 5-Part Prompt Anatomy
Never issue one-sentence prompts for complex tasks. Use the standard 5-part architecture:
1. **Persona / Role**: The expert identity the model adopts (e.g., `Senior Quantitative Developer`).
2. **Context / Background**: The exact environment, project state, and existing constraints.
3. **Core Task**: Clear, single-minded objective expressed with action verbs.
4. **Boundary Constraints**: Rigid negative boundaries (e.g., *Do NOT use bullion; use strictly IST*).
5. **Output Specification**: Structural format (e.g., *Output only valid JSON with keys: [...]*, or *Collegiate PDF layout*).

---

## 2. Source-Grounded Research (NotebookLM Protocol)
When dealing with sensitive data, legal documents, or proprietary domain theory:
- Restrict generation strictly to uploaded authoritative source texts.
- Force citation of specific pages, paragraphs, or section headings.
- Explicitly instruct the model: *\"If the uploaded sources do not contain sufficient evidence to answer, state 'Insufficient source documentation' rather than extrapolating.\"*

---

## 3. Context Window Management & Anti-Degradation
- **Context Priming**: Place the most critical constraints at both the extreme beginning and extreme end of the prompt (the \"Primacy and Recency\" effect in LLMs).
- **Compaction**: When conversation transcripts grow beyond token thresholds, compact intermediate discovery into structured summary artifacts before continuing.
"""
}

SKILLS_DEFINITIONS["agentic-tool-integrations-and-mcp"] = {
    "name": "agentic-tool-integrations-and-mcp",
    "description": (
        "Design and integrate tools using the Model Context Protocol (MCP), REST APIs, and webhook "
        "event architectures. Use when connecting agents to external databases, custom execution servers, "
        "or third-party enterprise tools."
    ),
    "content": """# Agentic Tool Integrations, APIs & Model Context Protocol (MCP)

## Overview
Synthesized from **Chapter 2 of The 5 Levels of AI Mastery**, this skill covers tool definitions, parameter schemas, Model Context Protocol (MCP) servers, and robust error-handling protocols for agent-tool interactions.

---

## 1. Model Context Protocol (MCP) Configuration
Antigravity and Gemini agents connect to external tools via `mcp_config.json`:

```json
{
  "mcpServers": {
    "custom_tools": {
      "command": "python",
      "args": ["-m", "my_mcp_server"],
      "env": {
        "API_TOKEN": "secret_key"
      }
    }
  }
}
```

---

## 2. Rigid Tool Schema Design Principles
1. **Strong Typing & Explicit Descriptions**: Every parameter must have an explicit JSON Schema `type`, `description`, and `required` flag.
2. **Deterministic Outputs**: Tools must return structured JSON or plain text with explicit status indicators (`STATUS: SUCCESS` / `STATUS: ERROR`).
3. **Error Transparency**: Never swallow exceptions. Return exact error codes, system messages, and actionable troubleshooting steps so the agent can self-correct.
"""
}

SKILLS_DEFINITIONS["antigravity-customization-engineering"] = {
    "name": "antigravity-customization-engineering",
    "description": (
        "Author professional Antigravity skills, workspace rules (GEMINI.md/AGENTS.md), and lifecycle hooks. "
        "Enforce progressive disclosure, frontmatter compliance, and discovery precedence across global "
        "and project scopes."
    ),
    "content": """# Antigravity Customization Engineering (Skills, Rules & Hooks)

## Overview
Synthesized from **Chapter 3 of The 5 Levels of AI Mastery** and Antigravity core architecture, this skill governs how to write and maintain skills, workspace rules, plugins, and lifecycle hooks.

---

## 1. Discovery Precedence Hierarchy
Antigravity loads customizations in strict priority order (highest to lowest):
1. **Workspace Project**: Walking up from current working directory to repository root (`.agents/`).
2. **Workspace JSON Configs**: Declared in `skills.json` or `plugins.json`.
3. **Global Configuration (Machine-Local)**: `~/.gemini/config/` (Applies to all projects on this machine).
4. **Built-in System Skills**: Bundled with the application.
5. **Global Declared JSON Configs**: Configured in global settings.

---

## 2. Skill Architecture Standards
Every skill must reside in its own subdirectory:
```text
skills/<skill_name>/
├── SKILL.md          # Required: Frontmatter + Step-by-step instructions
├── scripts/          # Optional: Python or shell helper scripts
└── references/       # Optional: In-depth manuals and documentation
```

### Frontmatter Validation:
```markdown
---
name: kebab-case-name
description: >-
  Third-person explanation of what the skill does and when the agent should trigger it.
---
```

---

## 3. Directory Rules (`GEMINI.md` / `AGENTS.md`)
- Plain markdown files placed in any directory or at global root `~/.gemini/config/GEMINI.md`.
- No YAML frontmatter.
- Always loaded when the agent operates within that directory scope or globally.
- Maximum size budget: 24,000 bytes per rule file.
"""
}

SKILLS_DEFINITIONS["autonomous-software-development-loop"] = {
    "name": "autonomous-software-development-loop",
    "description": (
        "Execute end-to-end autonomous software development loops: systematic planning, silent test-driven "
        "execution, browser/UI verification, self-correcting error recovery, and zero-intervention debugging. "
        "Use when delegating complex coding projects or automated backtesting."
    ),
    "content": """# Autonomous Software Development Loop & Agent Orchestration

## Overview
Synthesized from **Chapters 4 & 5 of The 5 Levels of AI Mastery**, this skill defines the autonomous 5-phase loop required for agents to deliver complete, verified software projects without requiring hand-holding.

---

## 1. The 5-Phase Autonomous Agent Loop
1. **Plan & Deconstruct**: Break complex user requirements into auditable milestones. Identify required packages and environment limits before writing code.
2. **Execute & Author**: Write modular, clean code directly into files. Never ask the user to copy/paste code.
3. **Silent Automated Verification**: Run tests, compiler checks, or headless scripts directly in the workspace. Verify exit codes and standard error streams.
4. **Self-Correction & Recovery**: When errors occur (e.g., `PermissionError`, missing modules, font glyph mismatch), analyze the traceback immediately and rewrite the offending code without prompting the user.
5. **Artifact Delivery**: Compile final outputs (executables, PDF reports, web apps) and present clickable markdown file links (`file:///...`).
"""
}

# ==============================================================================
# 3. GANN ASTROLOGICAL TRADING SKILLS
# ==============================================================================

SKILLS_DEFINITIONS["gann-astro-data-retrieval"] = {
    "name": "gann-astro-data-retrieval",
    "description": (
        "Query NASA JPL Horizons REST API for high-precision geocentric planetary coordinates, "
        "ecliptic longitude/latitude, and right ascension/declination across historical and future dates. "
        "Use when calculating astronomical ephemerides or tracking planetary aspects."
    ),
    "content": """# NASA JPL Horizons Ephemeris Data Retrieval & Celestial Mechanics

## Overview
Originated from the Gann Ephemeris project (`D:\\ephemeris`), this skill defines the protocol for querying NASA JPL Horizons REST API to obtain geocentric, apparent ecliptic coordinates for astronomical and financial harmonic calculations.

---

## 1. NASA JPL Horizons REST API Configuration
- **Endpoint**: `https://ssd.jpl.nasa.gov/api/horizons.api`
- **Center**: `'500@399'` (Geocentric, Earth center).
- **Ephemeris Type**: `OBSERVER`
- **Quantity Code**: `QUANTITIES='1'` (Astrometric / Apparent Ecliptic Longitude and Latitude).
- **Body Identifiers**:
  - Sun: `'10'`
  - Moon: `'301'`
  - Mercury: `'199'`
  - Venus: `'299'`
  - Mars: `'499'`
  - Jupiter: `'599'`
  - Saturn: `'699'`
  - Uranus: `'799'`
  - Neptune: `'899'`
  - Pluto: `'999'`

---

## 2. Parsing Ecliptic Coordinates
NASA JPL returns text-delimited tables between `$$SOE` (Start of Ephemeris) and `$$EOE` (End of Ephemeris):
- Extract **ObsSub-LON** (Apparent Ecliptic Longitude $\\lambda$, $0^\\circ \\le \\lambda < 360^\\circ$).
- Extract **ObsSub-LAT** (Apparent Ecliptic Latitude $\\beta$).
- Extract daily motion / speed in longitude ($d\\lambda / dt$). Identify retrograde stations when velocity flips from positive to negative.
"""
}

SKILLS_DEFINITIONS["gann-temporal-exchange-alignment"] = {
    "name": "gann-temporal-exchange-alignment",
    "description": (
        "Convert Universal Time (UT/UTC) astronomical timestamps to Indian Standard Time (IST, UTC+05:30) "
        "and synchronize planetary events with Indian exchange trading sessions (NSE, BSE, MCX). "
        "Use when evaluating market timing triggers for Indian financial markets."
    ),
    "content": """# Temporal Exchange Alignment: UTC to Indian Standard Time (IST)

## Overview
Originated from the Gann Ephemeris project, this skill establishes the exact temporal conversion and session alignment rules between Universal Time (UT/UTC) and Indian Standard Time (IST, UTC+05:30).

---

## 1. Mathematical Time Offset
$$\\text{IST} = \\text{UTC} + 5\\text{ hours } 30\\text{ minutes}$$
- Indian Standard Time does not observe Daylight Saving Time (DST). The offset remains invariant year-round.

---

## 2. Indian Exchange Session Definitions
1. **NSE / BSE Equity & Derivatives**:
   - Pre-Open: `09:00:00` to `09:08:00` IST
   - Regular Continuous Session: `09:15:00` to `15:30:00` IST
   - Total Continuous Duration: $375\\text{ minutes}$ ($6.25\\text{ hours}$)
2. **MCX Commodity Derivatives**:
   - Base Metals & Energy (Standard): `09:00:00` to `23:30:00` IST
   - US Daylight Saving Period: `09:00:00` to `23:55:00` IST
"""
}

SKILLS_DEFINITIONS["gann-market-harmonics-and-square-of-nine"] = {
    "name": "gann-market-harmonics-and-square-of-nine",
    "description": (
        "Apply W.D. Gann's Law of Vibration, Square of Nine spiral root derivations, planetary "
        "longitude-to-price conversions, and major harmonic aspect triggers (0°, 45°, 90°, 120°, 180°). "
        "Use when generating geometric price support/resistance levels and cycle timing nodes."
    ),
    "content": """# W.D. Gann Market Harmonics & Square of Nine Mathematics

## Overview
Developed in the Gann Ephemeris and Academic Textbook engines, this skill details W.D. Gann's quantitative methodologies: the Square of Nine spiral, planetary longitude mapping, and aspect trigonometry.

---

## 1. Square of Nine Odd-Square Mathematical Derivation
The Gann Square of Nine begins at origin $1$ and expands outward in concentric rings.
Every full $360^\\circ$ rotation increases the square root of the price by exactly $+2.0$:
$$\\Delta \\sqrt{P} = \\frac{\\theta}{180^\\circ}$$
- **Angle from Price**:
  $$\\theta(P) = [ (\\sqrt{P} - 1.0) \\pmod{2.0} ] \\times 180^\\circ \\quad \\text{where } 0^\\circ \\le \\theta < 360^\\circ$$
- **Price from Target Angle $\\theta$**:
  $$P(k, \\theta) = \\left[ 2k + 1.0 + \\frac{\\theta \\pmod{360^\\circ}}{180^\\circ} \\right]^2$$
  where $k = \\text{floor}\\left[ \\frac{\\sqrt{P_{\\text{ref}}} - 1.0 - \\theta / 180^\\circ}{2} \\right]$.

---

## 2. Major Harmonic Aspects & Angular Harmonics
- **Conjunction ($0^\\circ$)**: Planetary seeds, major trend initiator.
- **Semi-Square ($45^\\circ$)**: Harmonic sub-pivot ($1/8$ circle).
- **Square ($90^\\circ$)**: Major resistance / price-time squaring ($1/4$ circle).
- **Trine ($120^\\circ$)**: Harmonic equilibrium ($1/3$ circle).
- **Opposition ($180^\\circ$)**: Extreme price polarity / cycle reversal ($1/2$ circle).
"""
}

SKILLS_DEFINITIONS["gann-intraday-session-midpoint-analysis"] = {
    "name": "gann-intraday-session-midpoint-analysis",
    "description": (
        "Calculate intraday 50% price equilibrium levels, 180° temporal session midpoints, Spencer Equation "
        "of Time true solar noon, and micro-harmonic time nodes (90° at 13:56, 120° at 14:27 IST). "
        "Use when analyzing intraday swing pivots for Indian equity indices."
    ),
    "content": """# Intraday Session Midpoint Analysis & 360° Time Harmonics

## Overview
Derived from W.D. Gann's *45 Years in Wall Street* and *The Basis of My Forecasting Method*, this skill covers intraday equilibrium squaring: 50% price midpoints, session temporal centers, and solar noon offsets.

---

## 1. The 50% Price Equilibrium Principle
Gann considered the $50\\%$ division of any range the highest-gravity price pivot:
$$P_{50\\%} = \\frac{P_{\\text{High}} + P_{\\text{Low}}}{2}$$
When price crosses above $P_{50\\%}$, the trend is bullish; when price trades below, the trend is bearish.

---

## 2. NSE Continuous Session 360° Time Harmonics (09:15 to 15:30 IST)
The $375$-minute NSE trading session is mapped onto the $360^\\circ$ circle:
- **Session Open ($0^\\circ$)**: `09:15:00` IST ($0\\text{ mins}$)
- **$45^\\circ$ Harmonic**: `11:45:00` IST ($150\\text{ mins}$)
- **$50\\%$ Equilibrium / $180^\\circ$ Temporal Midpoint**: `12:22:30` IST ($187.5\\text{ mins}$)
- **$90^\\circ$ Squaring Node**: `13:56:15` IST ($281.25\\text{ mins}$)
- **$120^\\circ$ Trine Node**: `14:27:30` IST ($312.5\\text{ mins}$)
- **Session Close ($360^\\circ$)**: `15:30:00` IST ($375\\text{ mins}$)

---

## 3. Spencer Equation of Time True Solar Noon
Solar noon deviates from mean clock noon ($12:00$) due to orbital eccentricity and axial obliquity:
$$\\text{EoT} = 229.18 \\times [0.000075 + 0.001868\\cos(\\Gamma) - 0.032077\\sin(\\Gamma) - 0.014615\\cos(2\\Gamma) - 0.040849\\sin(2\\Gamma)]$$
For Mumbai ($72.87^\\circ\\text{ E}$) / NSE Servers: True Solar Noon prints between `12:28` and `12:44` IST depending on the seasonal day of the year.
"""
}

SKILLS_DEFINITIONS["indian-market-instrument-filtering"] = {
    "name": "indian-market-instrument-filtering",
    "description": (
        "Filter and route Gann timing and price levels strictly to NSE broad indices (Nifty 50), "
        "MCX energy (Crude Oil, Natural Gas), and MCX base metals (Copper, Zinc, Aluminium, Lead), "
        "while enforcing an absolute, unbreakable exclusion of gold and silver instruments."
    ),
    "content": """# Indian Market Instrument Filtering & Asset Routing

## Overview
Originated from the Gann Ephemeris trading system, this skill defines the strict eligibility rules for routing signals and harmonic levels across Indian exchanges.

---

## 1. Permitted Instrument Universe
Signals and calculators must only target:
1. **NSE Broad Indices**: Nifty 50 (`^NSEI`), Bank Nifty (`^NSEBANK`), FinNifty.
2. **NSE Index Derivatives**: Nifty 50 Options & Futures contracts.
3. **MCX Energy Futures**:
   - Crude Oil (`CRUDEOIL`)
   - Natural Gas (`NATURALGAS`)
4. **MCX Base Metal Futures**:
   - Copper (`COPPER`)
   - Zinc (`ZINC`)
   - Aluminium (`ALUMINIUM`)
   - Lead (`LEAD`)

---

## 2. Hard Exclusion Directive: Bullion
> **CRITICAL MANDATORY CONSTRAINT**:  
> Under NO circumstances may any gold or silver instrument (`GOLD`, `GOLDM`, `GOLDPETAL`, `SILVER`, `SILVERM`, `SILVERMIC`) be analyzed, backtested, listed, or displayed in alerts. Any reference to bullion must be strictly rejected or filtered at ingestion.
"""
}

# ==============================================================================
# 4. META SYSTEM: AUTO-HARVESTING & SYNCHRONIZATION
# ==============================================================================

SKILLS_DEFINITIONS["project-skill-harvesting-and-library-sync"] = {
    "name": "project-skill-harvesting-and-library-sync",
    "description": (
        "Automatically harvest newly discovered workflows, domain knowledge, and specialized methodologies "
        "at the conclusion of any project. Formats them into standardized SKILL.md packages and syncs "
        "them to the global Antigravity discovery root (~/.gemini/config/skills/) so they are immediately "
        "available in all subsequent projects."
    ),
    "content": """# Project Skill Harvesting, Packaging & Global Synchronization

## Overview
This meta-skill implements the continuous learning flywheel across all projects in the Antigravity ecosystem. Whenever a project concludes or achieves a new technical capability, this procedure extracts the knowledge into a persistent, reusable skill and installs it into the global library.

---

## 1. End-of-Project Skill Extraction Criteria
At the conclusion of any project, inspect if the project developed:
1. A unique domain formula or mathematical algorithm (e.g., Gann Square of Nine, CBSE step rubrics).
2. A repeatable tool connection, API integration, or deployment recipe (e.g., PyInstaller, JPL Horizons).
3. A critical debugging or rendering fix (e.g., TrueType font cmap rectification, preventing tofu boxes).
4. A specialized industry workflow (e.g., Indian market derivatives filtering).

---

## 2. Automated Harvesting Protocol
1. **Draft YAML Frontmatter**:
   - `name`: Lowercase, hyphenated kebab-case identifier.
   - `description`: 3rd-person summary specifying when and why to activate the skill.
2. **Structure the Content**:
   - Overview & Origin Project.
   - Core Concepts & Quantitative Formulas.
   - Step-by-Step Practical Algorithm.
   - Reference Code / Templates.
   - Boundary Constraints & Negative Rules.
3. **Write to Global Discovery**:
   - Save to `C:\\Users\\spmad\\.gemini\\config\\skills\\<skill_name>\\SKILL.md`.
   - Mirror to `D:\\AI SKILLS\\GLOBAL_SKILL_LIBRARY\\<skill_name>\\SKILL.md`.
4. **Update Library Catalog**:
   - Re-index `D:\\AI SKILLS\\GLOBAL_SKILL_LIBRARY\\README.md`.

---

## 3. Immediate Global Availability
Because `C:\\Users\\spmad\\.gemini\\config\\skills\\` is Antigravity's machine-local global discovery directory, any skill written here is **immediately visible to every existing and future project** launched on this system.
"""
}


def build_library():
    print(f"Total skills to build: {len(SKILLS_DEFINITIONS)}")
    
    for skill_name, data in SKILLS_DEFINITIONS.items():
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
            
        print(f"  [OK] Installed skill: {skill_name}")

    # Build Global GEMINI.md directive
    global_directive = """# GLOBAL ANTIGRAVITY AGENT DIRECTIVE & CONTINUOUS LEARNING PROTOCOL

## 1. UNIVERSAL SKILL LIBRARY ACCESS
All specialized skills harvested across projects (Tharun Project, Google AI Mastery, Gann Astrological Trading)
are centrally stored and active in:
`C:\\Users\\spmad\\.gemini\\config\\skills\\`
and mirrored in:
`D:\\AI SKILLS\\GLOBAL_SKILL_LIBRARY\\`

Whenever starting or working on any project, always review the available skills and activate the appropriate
domain knowledge (e.g., mathematical typography, academic evaluation, Gann harmonics, or tool integration).

## 2. AUTOMATIC END-OF-PROJECT SKILL HARVESTING MANDATE
Whenever a user's task or project achieves a new capability, resolves a complex engineering problem, or develops
a reusable methodology:
1. **Extract & Synthesize**: Summarize the core methodology, formulas, and code into standard SKILL.md format.
2. **Auto-Install Globally**: Save the skill directly into `C:\\Users\\spmad\\.gemini\\config\\skills\\<skill_name>\\SKILL.md`.
3. **Mirror to Central Library**: Copy to `D:\\AI SKILLS\\GLOBAL_SKILL_LIBRARY\\<skill_name>\\SKILL.md`.
4. **Ensure Continuity**: Confirm that the new skill is verified and immediately discoverable for subsequent projects.
"""
    with open(GLOBAL_GEMINI_MD, "w", encoding="utf-8") as f:
        f.write(global_directive)
    print(f"  [OK] Installed Global Workspace Directive at: {GLOBAL_GEMINI_MD}")

    # Build README.md in D:\AI SKILLS\GLOBAL_SKILL_LIBRARY
    readme_path = os.path.join(LOCAL_LIBRARY_ROOT, "README.md")
    readme_content = """# Unified Global AI Skill Library
### Central Cross-Project Repository for Google Antigravity & Gemini Agents

This library consolidates and standardizes all specialized skills, academic rubrics, quantitative formulas, and automation workflows developed across:
1. **Tharun ScholasticPulse Project** (`D:\\THARUN PROJECT`)
2. **Google AI Mastery Masterclass** (`D:\\AI SKILLS\\AI-Mastery-Masterclass`)
3. **W.D. Gann Astrological Ephemeris & Trading** (`D:\\ephemeris`)

---

## Active Skills Index

### A. Tharun Academic Engine
1. **`tharun-academic-evaluation-and-rubrics`**: CBSE Question Framing, Bloom's Taxonomy, Step Marking Rubrics, Anti-Daydreaming Architecture.
2. **`academic-paper-typesetting-and-math-preview`**: ISO A4 page geometry, institutional headers, right-aligned mark brackets, KaTeX math preview.
3. **`mathematical-typography-and-font-rectification`**: Font cmap auditing, replacing unmapped Unicode characters (∈, ⌊, ⌋, ⇒) to eliminate tofu boxes (□).
4. **`desktop-application-packaging-and-shortcuts`**: PyInstaller packaging, silent VBS launchers, and PowerShell desktop shortcuts.

### B. Google AI Mastery
5. **`google-gemini-research-mastery`**: Deep research, NotebookLM grounding, 5-part prompt anatomy, and context window economics.
6. **`agentic-tool-integrations-and-mcp`**: Model Context Protocol (MCP), API integration, webhooks, and tool error recovery.
7. **`antigravity-customization-engineering`**: Authoring skills, workspace rules, plugins, and progressive disclosure.
8. **`autonomous-software-development-loop`**: The 5-phase agent loop (Plan, Act, Verify, Self-Correct, Document).

### C. Gann Astrological Trading
9. **`gann-astro-data-retrieval`**: NASA JPL Horizons REST API geocentric queries, DE440/DE441, celestial coordinates.
10. **`gann-temporal-exchange-alignment`**: UTC/UT to IST (+05:30) conversion, aligning celestial events to Indian exchange sessions.
11. **`gann-market-harmonics-and-square-of-nine`**: The Law of Vibration, Square of Nine spiral root math, planetary degree-to-price mapping.
12. **`gann-intraday-session-midpoint-analysis`**: 50% price equilibrium, session midpoint squaring, Spencer Equation of Time solar noon.
13. **`indian-market-instrument-filtering`**: Routing triggers to NSE Nifty 50 and MCX Energy/Base Metals with strict bullion exclusion.

### D. Meta-Learning & Synchronization
14. **`project-skill-harvesting-and-library-sync`**: Continuous learning protocol that extracts end-of-project capabilities and syncs them globally.

---

## Global Discovery & Auto-Loading Architecture
- **Global Path**: `C:\\Users\\spmad\\.gemini\\config\\skills\\`
- All skills in this library are installed into Antigravity's machine-local global discovery folder.
- **Every new project or workspace opened in Antigravity automatically discovers and loads all 14 skills!**
- The global rule `C:\\Users\\spmad\\.gemini\\config\\GEMINI.md` mandates that at the end of every project, newly learned capabilities are automatically added to this library.
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"  [OK] Generated Library README at: {readme_path}")


if __name__ == "__main__":
    build_library()
