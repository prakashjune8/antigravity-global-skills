# GLOBAL ANTIGRAVITY AGENT DIRECTIVE & CONTINUOUS LEARNING PROTOCOL

## 1. UNIVERSAL SKILL LIBRARY ACCESS
All specialized skills harvested across projects (Tharun Project, Google AI Mastery, Gann Astrological Trading)
are centrally stored and active in:
`~/.gemini/config/skills/`
and mirrored in:
`D:\AI SKILLS\GLOBAL_SKILL_LIBRARY\`

Whenever starting or working on any project, always review the available skills and activate the appropriate
domain knowledge (e.g., mathematical typography, academic evaluation, Gann harmonics, or tool integration).

## 2. AUTOMATIC END-OF-PROJECT SKILL HARVESTING MANDATE
Whenever a user's task or project achieves a new capability, resolves a complex engineering problem, or develops
a reusable methodology:
1. **Extract & Synthesize**: Summarize the core methodology, formulas, and code into standard SKILL.md format.
2. **Auto-Install Globally**: Save the skill directly into `~/.gemini/config/skills/<skill_name>/SKILL.md`.
3. **Mirror to Central Library**: Copy to `D:\AI SKILLS\GLOBAL_SKILL_LIBRARY\<skill_name>\SKILL.md`.
4. **Ensure Continuity**: Confirm that the new skill is verified and immediately discoverable for subsequent projects.

## 3. AUTONOMOUS GITHUB REPLICATION & PERSISTENCE MANDATE
All active projects on this machine must be perpetually mirrored and synchronized to GitHub under user `prakashjune8`.
Whenever working in any workspace or starting a new project:
1. **Zero Permission Required**: Never ask the user for permission to initialize git, create repositories, stage files, or push commits. Execute all GitHub replications autonomously.
2. **Auto-Initialization for New Projects**: Whenever a new project is created or started:
   - Ensure a standard `.gitignore` exists (filtering large binaries, virtual environments, node_modules, cache).
   - Initialize git (`git init -b main`).
   - Automatically create the GitHub repository with `gh repo create <repo_name> --public --source=. --remote=origin --push`.
3. **Continuous Progress Sync**: At the conclusion of substantive code changes, file generations, or debugging milestones, automatically run:
   `python "D:\AI SKILLS\auto_project_github_sync.py"`
   or stage, commit with a descriptive message, and push directly to `origin`.
