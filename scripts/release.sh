#!/usr/bin/env bash
set -euo pipefail

# Usage: scripts/release.sh 1.0.0

version=${1:-}
if [[ -z "$version" ]]; then
  echo "Usage: $0 <version> (e.g., 1.2.3)" >&2
  exit 1
fi

if [[ ! $version =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Version must be semver (X.Y.Z)" >&2
  exit 1
fi

echo "$version" > VERSION

# Update AUR pkgver
sed -i -E "s/^(pkgver=).*/\\1$version/" aur/PKGBUILD

# Update Dockerfile label version if present
sed -i -E "s/^(LABEL version=)\"[^"]*\"/\\1\"$version\"/" Dockerfile || true

# Optionally regenerate .SRCINFO (requires makepkg)
if command -v makepkg >/dev/null 2>&1; then
  ( cd aur && makepkg --printsrcinfo > .SRCINFO ) || true
else
  echo "Note: makepkg not found; skipping .SRCINFO regeneration"
fi

git add VERSION aur/PKGBUILD aur/.SRCINFO || true
git commit -m "chore(release): v$version" || echo "Nothing to commit"
git tag -a "v$version" -m "Release v$version"

echo "Tag created: v$version"
echo "Now push with:"
echo "  git push && git push --tags"
