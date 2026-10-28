---
name: google-gemini-research-mastery
description: >-
  Master Level 1 AI research workflows: execute deep research synthesis, ground models using NotebookLM source constraints, construct high-accuracy multi-part prompts, and manage context windows. Use when researching complex technical subjects, synthesizing literature, or preventing AI hallucinations.
---

# Google Gemini & Deep Research Mastery

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
- Explicitly instruct the model: *"If the uploaded sources do not contain sufficient evidence to answer, state 'Insufficient source documentation' rather than extrapolating."*

---

## 3. Context Window Management & Anti-Degradation
- **Context Priming**: Place the most critical constraints at both the extreme beginning and extreme end of the prompt (the "Primacy and Recency" effect in LLMs).
- **Compaction**: When conversation transcripts grow beyond token thresholds, compact intermediate discovery into structured summary artifacts before continuing.
