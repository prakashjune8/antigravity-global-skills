---
name: project-skill-harvesting-and-library-sync
description: >-
  Automatically harvest newly discovered workflows, domain knowledge, and specialized methodologies at the conclusion of any project. Formats them into standardized SKILL.md packages and syncs them to the global Antigravity discovery root (~/.gemini/config/skills/) so they are immediately available in all subsequent projects.
---

# Project Skill Harvesting, Packaging & Global Synchronization

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
   - Save to `C:\Users\spmad\.gemini\config\skills\<skill_name>\SKILL.md`.
   - Mirror to `D:\AI SKILLS\GLOBAL_SKILL_LIBRARY\<skill_name>\SKILL.md`.
4. **Update Library Catalog**:
   - Re-index `D:\AI SKILLS\GLOBAL_SKILL_LIBRARY\README.md`.

---

## 3. Immediate Global Availability
Because `C:\Users\spmad\.gemini\config\skills\` is Antigravity's machine-local global discovery directory, any skill written here is **immediately visible to every existing and future project** launched on this system.
