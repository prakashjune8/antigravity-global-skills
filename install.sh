#!/usr/bin/env bash
# macOS & Linux Installer for Antigravity Global Skills Library
set -e

echo "=========================================================="
echo "  ANTIGRAVITY GLOBAL SKILL LIBRARY INSTALLER (UNIX/MAC)"
echo "=========================================================="

TARGET_DIR="$HOME/.gemini/config/skills"
TARGET_GEMINI_MD="$HOME/.gemini/config/GEMINI.md"

mkdir -p "$TARGET_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd)"

if [ -z "$SCRIPT_DIR" ] || [ ! -f "$SCRIPT_DIR/README.md" ]; then
    TEMP_DIR=$(mktemp -d)
    echo "Cloning latest skills repository..."
    git clone --depth 1 https://github.com/prakashjune8/antigravity-global-skills.git "$TEMP_DIR"
    SCRIPT_DIR="$TEMP_DIR"
fi

INSTALLED=0
for skill_dir in "$SCRIPT_DIR"/*/; do
    if [ -f "${skill_dir}SKILL.md" ]; then
        skill_name=$(basename "$skill_dir")
        mkdir -p "$TARGET_DIR/$skill_name"
        cp -r "${skill_dir}"* "$TARGET_DIR/$skill_name/"
        echo "  [OK] Installed: $skill_name"
        INSTALLED=$((INSTALLED + 1))
    fi
done

if [ -f "$SCRIPT_DIR/GEMINI.md" ]; then
    cp "$SCRIPT_DIR/GEMINI.md" "$TARGET_GEMINI_MD"
    echo "  [OK] Installed Global Directive at: $TARGET_GEMINI_MD"
fi

echo "=========================================================="
echo "SUCCESS! $INSTALLED skills deployed to $TARGET_DIR."
echo "=========================================================="
