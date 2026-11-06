---
name: institutional-curriculum-chunking-and-typesetting
description: Architect, chunk, typeset, and integrate comprehensive 16-chapter institutional textbooks and quantitative manuals with zero token truncation, KaTeX variable isolation ledgers, and dynamic multi-tier UI readers.
---

# Institutional Curriculum Chunking & Typesetting Engine

## Overview
When engineering massive technical literature, textbooks, or educational curricula (exceeding 2,000+ lines or 15,000+ words), single-prompt generation invariably fails due to token truncation, hallucinated shortcuts, and formatting degradation. This skill defines the deterministic protocol for modular 8-batch chunking, rigorous KaTeX mathematical typesetting, empirical verification cards, and interactive desktop UI integration.

---

## 1. The 3-Tier Pedagogical Hierarchy
Every institutional curriculum must progress through three discrete cognitive tiers:
1. **Tier 1 (Beginner / Foundation)**:
   - Relies strictly on everyday physical analogies (e.g., grandfather clock hands, sundial shadows, 12-room castles).
   - Zero raw mathematical formulas. Ground the student in physical intuition first.
2. **Tier 2 (Intermediate / Quantitative)**:
   - Formal mathematical derivations, Fourier series, coordinate transformations, and exchange alignment.
   - Rigorous Variable Isolation Ledgers following every equation.
3. **Tier 3 (Master / Harmonic Synthesis)**:
   - Clinical, authoritative execution doctrines, multi-cycle nesting, cymatic wave mechanics, and zero-tolerance sniper confluence rules.

---

## 2. The 8-Part Institutional Chapter Skeleton
Every chapter must adhere strictly to the following 8-part modular anatomy:
1. **Chapter Title Banner**: `# CHAPTER XX: [TITLE IN ALL CAPS]`
2. **Architectural Introduction**: Contextual setup, historical grounding, and core problem definition.
3. **Anchor Analogy**: A tangible physical metaphor explaining the concept without mathematics.
4. **Quantitative Mechanics & KaTeX Formula**:
   - Multi-line centered KaTeX equation block (`$$...$$`).
   - Followed immediately by the **Variable Isolation Ledger** defining every Greek and Latin variable with physical units.
5. **Operational / Classification Matrix**: Structured ASCII or Markdown table defining parameters, states, and rules.
6. **Empirical Verification Card**: A dedicated audit box documenting real historical market data (dates, tick prices, timestamps, variances, and institutional takeaways).
7. **Visual Blueprint & Live Terminal Navigation**: Explicit bracketed UI tokens (`[Master Control Deck]`, `[360° Celestial Wheel]`) guiding the user's eyes to the live software controls.
8. **Chapter Checklist & Verification Gates**: Actionable checkboxes validating technical mastery.

---

## 3. The Sequential Chunking & Relay Protocol
Never generate more than two dense chapters per prompt. Use an 8-batch pipeline:
- **Batch 1**: Chapters 1–2 (Level 1 Launch)
- **Batch 2**: Chapters 3–4 (Level 1 Intermediate)
- **Batch 3**: Chapters 5–6 (Level 1 Completion)
- **Batch 4**: Chapters 7–8 (Level 2 Launch)
- **Batch 5**: Chapters 9–10 (Level 2 Midpoint)
- **Batch 6**: Chapters 11–12 (Level 2 Completion)
- **Batch 7**: Chapters 13–14 (Level 3 Launch)
- **Batch 8**: Chapters 15–16 (Level 3 Completion & Master Capstone)

### State Preservation & Relay Baton
At the start of each batch, load the **Context Relay Header**:
```markdown
[CONTEXT RELAY HEADER]
- Active Project: Gann Celestial Tracker Pro
- Active Phase  : Batch N of 8 (Chapters X & Y)
- Design System : TEXTBOOK_DESIGN_SYSTEM.md (8-part skeleton, KaTeX Variable Ledger)
- Tone Mode     : [Tier 1 Warm Analogy | Tier 2 Precise Quant | Tier 3 Clinical Sniper]
- UI Anchors    : Direct reader eyes to terminal UI elements using [Bracket Tokens]
```

---

## 4. Anti-AI Editorial Modulation
To prevent robotic cadence, strictly ban:
- "In conclusion", "Furthermore", "It is important to remember", "As we delve deeper", "A tapestry of".
Replace them with active institutional verbs: "Derive", "Isolate", "Inspect", "Observe", "Execute".

---

## 5. Desktop UI Reader Architecture (CustomTkinter)
To render massive multi-chapter textbooks inside a desktop terminal:
1. **Header Ribbon**:
   - Level Segmented Button (`All Chapters`, `Level 1`, `Level 2`, `Level 3`).
   - Chapter OptionMenu (dynamically filtered by selected level).
   - Real-time search entry box with auto-scroll jumping.
   - `[Copy Chapter]` and `[Open Markdown File]` utility triggers.
2. **Central Reader Pane**:
   - `ctk.CTkTextbox` with `wrap="word"`, `font=("Consolas", 11)` or `Segoe UI`.
   - Disabled state for read-only integrity, re-enabled transiently during programmatic content injection.
3. **Footer Ribbon**:
   - `[◀ Previous Chapter]`, dynamic progress badge (`Chapter X of 16 • Level Y`), and `[Next Chapter ▶]`.
