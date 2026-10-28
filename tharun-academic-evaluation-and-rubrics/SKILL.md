---
name: tharun-academic-evaluation-and-rubrics
description: >-
  Design CBSE-compliant question papers, step-wise evaluation rubrics, Bloom's taxonomy distributions, and anti-daydreaming test architectures. Use when structuring student assessments, generating model answer schemes, or evaluating academic answer sheets.
---

# CBSE Academic Evaluation, Question Framing & Step-Marking Rubrics

## Overview
This skill originates from the **Tharun ScholasticPulse Project** (`D:\THARUN PROJECT`), an advanced academic evaluation engine designed for Class 8-12 CBSE curricula. It provides deterministic guidelines for framing question papers, allocating cognitive levels across Bloom's Taxonomy, enforcing step-wise grading rubrics, and tracking recurring student mistakes via an Error Bank.

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
3. **Section C (3 Marks)**: Short Answer (SA). Exactly 3 marked milestones: Formula Statement ($1/2$ mark), Step substitution ($1\frac{1}{2}$ marks), Final value with SI units ($1$ mark).
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
