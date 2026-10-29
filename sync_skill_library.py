"""Automated Skill Library Synchronizer.

Discovers skills from any project workspace (e.g., .agents/skills) and
synchronizes them bidirectionally between:
- C:\\Users\\spmad\\.gemini\\config\\skills\\ (Antigravity Global Discovery Root)
- D:\\AI SKILLS\\GLOBAL_SKILL_LIBRARY\\ (Central Disk Storage & Archive)
"""
from __future__ import annotations

import os
import shutil
import sys

GLOBAL_CONFIG_SKILLS = r"C:\Users\spmad\.gemini\config\skills"
LOCAL_LIBRARY_ROOT = r"D:\ANTIGRAVITY PROJECT FOLDER\AI SKILLS\GLOBAL_SKILL_LIBRARY"


def sync_library(project_skills_dir: str | None = None):
    print("=== SYNCHRONIZING ANTIGRAVITY GLOBAL SKILL LIBRARY ===")
    
    os.makedirs(GLOBAL_CONFIG_SKILLS, exist_ok=True)
    os.makedirs(LOCAL_LIBRARY_ROOT, exist_ok=True)
    
    # If project skills dir supplied, harvest newly added project skills
    if project_skills_dir and os.path.exists(project_skills_dir):
        print(f"Scanning project skills from: {project_skills_dir}")
        for item in os.listdir(project_skills_dir):
            src_skill_dir = os.path.join(project_skills_dir, item)
            src_skill_md = os.path.join(src_skill_dir, "SKILL.md")
            if os.path.isdir(src_skill_dir) and os.path.exists(src_skill_md):
                # Normalize skill name
                norm_name = item.lower().replace("_", "-")
                dest_global = os.path.join(GLOBAL_CONFIG_SKILLS, norm_name)
                dest_local = os.path.join(LOCAL_LIBRARY_ROOT, norm_name)
                
                os.makedirs(dest_global, exist_ok=True)
                os.makedirs(dest_local, exist_ok=True)
                
                shutil.copy2(src_skill_md, os.path.join(dest_global, "SKILL.md"))
                shutil.copy2(src_skill_md, os.path.join(dest_local, "SKILL.md"))
                print(f"  -> Harvested & Synced: {norm_name}")

    # Bidirectional sync between Global Config and Local Drive D Library
    local_skills = [
        d for d in os.listdir(LOCAL_LIBRARY_ROOT)
        if os.path.isdir(os.path.join(LOCAL_LIBRARY_ROOT, d))
    ]
    global_skills = [
        d for d in os.listdir(GLOBAL_CONFIG_SKILLS)
        if os.path.isdir(os.path.join(GLOBAL_CONFIG_SKILLS, d))
    ]

    # Mirror local to global
    for s in local_skills:
        src = os.path.join(LOCAL_LIBRARY_ROOT, s, "SKILL.md")
        dest_dir = os.path.join(GLOBAL_CONFIG_SKILLS, s)
        dest_file = os.path.join(dest_dir, "SKILL.md")
        if os.path.exists(src) and not os.path.exists(dest_file):
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy2(src, dest_file)
            print(f"  [+] Installed to Global Config: {s}")

    # Mirror global to local
    for s in global_skills:
        src = os.path.join(GLOBAL_CONFIG_SKILLS, s, "SKILL.md")
        dest_dir = os.path.join(LOCAL_LIBRARY_ROOT, s)
        dest_file = os.path.join(dest_dir, "SKILL.md")
        if os.path.exists(src) and not os.path.exists(dest_file):
            os.makedirs(dest_dir, exist_ok=True)
            shutil.copy2(src, dest_file)
            print(f"  [+] Mirrored to Local Library: {s}")

    active_count = len(os.listdir(GLOBAL_CONFIG_SKILLS))
    print(f"\n[SUCCESS] Synchronization complete! Total active global skills: {active_count}")


if __name__ == "__main__":
    scan_dir = sys.argv[1] if len(sys.argv) > 1 else None
    sync_library(scan_dir)
