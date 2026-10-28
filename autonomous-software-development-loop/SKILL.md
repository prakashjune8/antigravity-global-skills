---
name: autonomous-software-development-loop
description: >-
  Execute end-to-end autonomous software development loops: systematic planning, silent test-driven execution, browser/UI verification, self-correcting error recovery, and zero-intervention debugging. Use when delegating complex coding projects or automated backtesting.
---

# Autonomous Software Development Loop & Agent Orchestration

## Overview
Synthesized from **Chapters 4 & 5 of The 5 Levels of AI Mastery**, this skill defines the autonomous 5-phase loop required for agents to deliver complete, verified software projects without requiring hand-holding.

---

## 1. The 5-Phase Autonomous Agent Loop
1. **Plan & Deconstruct**: Break complex user requirements into auditable milestones. Identify required packages and environment limits before writing code.
2. **Execute & Author**: Write modular, clean code directly into files. Never ask the user to copy/paste code.
3. **Silent Automated Verification**: Run tests, compiler checks, or headless scripts directly in the workspace. Verify exit codes and standard error streams.
4. **Self-Correction & Recovery**: When errors occur (e.g., `PermissionError`, missing modules, font glyph mismatch), analyze the traceback immediately and rewrite the offending code without prompting the user.
5. **Artifact Delivery**: Compile final outputs (executables, PDF reports, web apps) and present clickable markdown file links (`file:///...`).
