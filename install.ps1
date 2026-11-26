# Installs Claude for Paid Ads into Claude Code on Windows.
# Usage:  .\install.ps1            (installs from GitHub)
#         .\install.ps1 -Source .  (installs from this folder)
param([string]$Source = "jawadbuilds/claude-for-paid-ads")

$ErrorActionPreference = "Stop"

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Host "Claude Code is not installed. Get it from https://claude.com/claude-code and run this again."
    exit 1
}

Write-Host "Adding the marketplace..."
claude plugin marketplace add $Source
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

foreach ($plugin in "paid-ads", "claude-ads", "claude-seo", "claude-blog") {
    Write-Host "Installing $plugin..."
    claude plugin install "$plugin@jawadbuilds"
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

Write-Host ""
Write-Host "Done. Restart Claude Code, then say: help me with my ads"
