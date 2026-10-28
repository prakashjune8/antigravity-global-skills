---
name: antigravity-customization-engineering
description: >-
  Author professional Antigravity skills, workspace rules (GEMINI.md/AGENTS.md), and lifecycle hooks. Enforce progressive disclosure, frontmatter compliance, and discovery precedence across global and project scopes.
---

# Antigravity Customization Engineering (Skills, Rules & Hooks)

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
