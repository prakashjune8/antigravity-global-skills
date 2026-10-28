# One-Click Sync & Push to GitHub
param (
    [string]$CommitMessage = "Update global skills library with newly learned capabilities"
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  SYNC & PUSH SKILLS TO GITHUB" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# Step 1: Run local sync from ~/.gemini/config/skills to current repo
python sync_skill_library.py

# Step 2: Git stage, commit, and push
git add -A
$status = git status --porcelain
if ($status) {
    git commit -m $CommitMessage
    git push origin main
    Write-Host "Changes successfully pushed to GitHub!" -ForegroundColor Green
} else {
    Write-Host "No changes to commit. Everything is up to date." -ForegroundColor Yellow
}
