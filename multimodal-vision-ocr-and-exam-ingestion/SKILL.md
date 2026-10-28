---
name: multimodal-vision-ocr-and-exam-ingestion
description: >-
  Ingest, OCR, and align handwritten exam answer sheets, student notes, and scanned documents using multimodal Gemini Vision API with automatic fallback and schema alignment. Use when processing handwritten student submissions, mobile photo scans, or handwritten math/science test papers.
---

# Multimodal Vision OCR, Handwritten Document Ingestion & Schema Alignment

## Overview
Originated from the Tharun ScholasticPulse project (`D:\THARUN PROJECT\exam_vision_ocr_engine_v3.py`), this skill details how to ingest raw camera photos, mobile scans, or PDF uploads of handwritten student work, extract handwritten text/math, and align responses question-by-question against a predefined structured JSON exam schema.

---

## 1. Multimodal Vision API Ingestion Architecture
To handle imperfect student mobile photos (variable lighting, rotation, shadows, crumpled paper):
1. **MIME-Type & Format Normalization**:
   - Convert multi-page PDF documents into high-DPI PNG pages ($300\text{ DPI}$).
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
3. For mathematical equations, transcribe into clean LaTeX format: \( ... \).
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
