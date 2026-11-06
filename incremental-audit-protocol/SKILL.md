---
name: incremental-audit-protocol
description: Enforce segmented task decomposition, isolated atomic execution, mandatory 60-second simulated cooldown audits, and zero-truncation sequential progression across all large-scale generation and engineering tasks.
---

# The Incremental Audit Protocol (IAP)

## Overview
When executing large-scale, high-density generation tasks (such as institutional textbooks, multi-file software scaffolding, or exhaustive empirical backtests), single-prompt execution leads to critical failures: token exhaustion, silent truncation, hallucinated placeholders, and cognitive drift. 

The **Incremental Audit Protocol (IAP)** is a mandatory operational constraint that eliminates truncation risk by enforcing hard task decomposition, atomic isolation, and simulated 60-second audit checkpoints.

---

## The Four Execution Pillars

```
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│ 1. TASK DECOMPOSITION  │ ───► │ 2. ISOLATED EXECUTION  │ ───► │ 3. 60s AUDIT PROTOCOL  │ ───► │ 4. SEQUENTIAL PROGRESS │
│ Break into atomic steps│      │ Execute ONLY 1 subtask │      │ Verify zero-truncation │      │ Proceed to next subtask│
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

### 1. Task Decomposition (The Blueprint)
Before generating any final content or code:
- Decompose the master task into discrete, atomic sub-tasks.
- Ensure each sub-task is bounded by a strict output token ceiling (e.g., maximum 1–2 chapters or 1–2 modules per turn).
- Present the exhaustive atomic roadmap to the user before launching execution.

### 2. Isolated Execution
- Execute *strictly* one sub-task at a time.
- Hard barrier: generation must halt immediately at the boundary of the active sub-task. Bleeding into subsequent sub-tasks is strictly forbidden.

### 3. The 60-Second Simulated Cooldown & Audit Checkpoint
Immediately upon generating the sub-task:
1. Announce:
   > *"Sub-task complete. Initiating 60-second audit protocol..."*
2. Execute a rigorous multi-point audit:
   - **Truncation Check**: Did the output finish its concluding section, checklist, and code blocks cleanly?
   - **Mathematical Rigor**: Are all equations formatted with KaTeX and supported by Variable Isolation Ledgers?
   - **Design Fidelity**: Are all required callouts, analogies, and UI navigation brackets intact?
3. Output the definitive audit verdict:
   > *"Audit Passed: Zero truncation, mathematical integrity verified, formatting holds."*

### 4. Sequential Progression
- Only after a successful audit verdict may execution advance to the subsequent sub-task on the roadmap.
- When waiting for user authorization, state the next scheduled sub-task and request explicit clearance.
