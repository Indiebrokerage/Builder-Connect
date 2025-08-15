#!/usr/bin/env bash
# Initialize a Git repository, create an initial commit, and push to a remote in one go.
# Usage:
#   ./bootstrap_repo.sh <REMOTE_URL> [main|master]
set -euo pipefail
REMOTE="${1:-}"
BRANCH="${2:-main}"
if [ -z "$REMOTE" ]; then
  echo "Usage: $0 <REMOTE_URL> [branch]"; exit 1
fi
git init
git checkout -b "$BRANCH" 2>/dev/null || git switch -c "$BRANCH"
git add .
git -c user.name="${GIT_USER:-REC Bot}" -c user.email="${GIT_EMAIL:-devnull@example.com}"     commit -m "chore(init): Real Estate Conduit Factory one-click repo"
git remote add origin "$REMOTE" || git remote set-url origin "$REMOTE"
git push -u origin "$BRANCH"
echo "✅ Repo bootstrapped and pushed to $REMOTE ($BRANCH)"
