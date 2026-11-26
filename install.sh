#!/usr/bin/env sh
# Installs Claude for Paid Ads into Claude Code on macOS and Linux.
# Usage:  ./install.sh        (installs from GitHub)
#         ./install.sh .      (installs from this folder)
set -e

SOURCE="${1:-jawadbuilds/claude-for-paid-ads}"

if ! command -v claude >/dev/null 2>&1; then
  echo "Claude Code is not installed. Get it from https://claude.com/claude-code and run this again."
  exit 1
fi

echo "Adding the marketplace..."
claude plugin marketplace add "$SOURCE"

for plugin in paid-ads claude-ads claude-seo claude-blog; do
  echo "Installing $plugin..."
  claude plugin install "$plugin@jawadbuilds"
done

echo ""
echo "Done. Restart Claude Code, then say: help me with my ads"
