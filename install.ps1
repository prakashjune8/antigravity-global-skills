# Windows PowerShell One-Click Installer for Antigravity Global Skills Library
# Can be run locally or remotely via:
#   irm https://raw.githubusercontent.com/prakashjune8/antigravity-global-skills/main/install.ps1 | iex

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  ANTIGRAVITY GLOBAL SKILL LIBRARY INSTALLER" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

$UserHome = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::UserProfile)
$TargetSkillsDir = Join-Path $UserHome ".gemini\config\skills"
$TargetGeminiMd = Join-Path $UserHome ".gemini\config\GEMINI.md"

Write-Host "Target Skills Directory: $TargetSkillsDir" -ForegroundColor Yellow

# Ensure target directories exist
if (-not (Test-Path $TargetSkillsDir)) {
    New-Item -ItemType Directory -Path $TargetSkillsDir -Force | Out-Null
}

$ScriptDir = $PSScriptRoot
if (-not $ScriptDir -or -not (Test-Path "$ScriptDir\README.md")) {
    # If run via irm/iex, clone to temporary directory
    Write-Host "Remote execution detected. Downloading latest skills from GitHub..." -ForegroundColor Cyan
    $TempRepo = Join-Path ([System.IO.Path]::GetTempPath()) "antigravity-global-skills"
    if (Test-Path $TempRepo) { Remove-Item -Recurse -Force $TempRepo }
    git clone --depth 1 https://github.com/prakashjune8/antigravity-global-skills.git $TempRepo
    $ScriptDir = $TempRepo
}

# Copy all skill folders
$InstalledCount = 0
Get-ChildItem -Path $ScriptDir -Directory | Where-Object {
    Test-Path (Join-Path $_.FullName "SKILL.md")
} | ForEach-Object {
    $SkillName = $_.Name
    $DestSkillDir = Join-Path $TargetSkillsDir $SkillName
    if (-not (Test-Path $DestSkillDir)) {
        New-Item -ItemType Directory -Path $DestSkillDir -Force | Out-Null
    }
    Copy-Item -Path (Join-Path $_.FullName "*") -Destination $DestSkillDir -Recurse -Force
    Write-Host "  [OK] Installed: $SkillName" -ForegroundColor Green
    $InstalledCount++
}

# Install global GEMINI.md directive
$SourceGeminiMd = Join-Path $ScriptDir "GEMINI.md"
if (Test-Path $SourceGeminiMd) {
    Copy-Item -Path $SourceGeminiMd -Destination $TargetGeminiMd -Force
    Write-Host "  [OK] Installed Global Workspace Directive: $TargetGeminiMd" -ForegroundColor Green
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "SUCCESS! $InstalledCount skills successfully deployed to this computer." -ForegroundColor Green
Write-Host "All skills are now immediately active for Antigravity & Gemini agents." -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan
