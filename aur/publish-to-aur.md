# Publish to AUR

This repository contains the PKGBUILD for `apex-launcher-bin`.

Steps to publish a new version:

1. Update version and tag in the main repo:
   ```bash
   ./scripts/release.sh 1.2.3
   git push && git push --tags
   ```

2. Update the AUR repo (requires you to be the package maintainer):
   ```bash
   git clone ssh://aur@aur.archlinux.org/apex-launcher-bin.git /tmp/apex-launcher-bin-aur
   cp -v aur/PKGBUILD aur/apex-launcher.install /tmp/apex-launcher-bin-aur/
   ( cd /tmp/apex-launcher-bin-aur && makepkg --printsrcinfo > .SRCINFO )
   ( cd /tmp/apex-launcher-bin-aur && git add PKGBUILD .SRCINFO apex-launcher.install && git commit -m "Update to v$(cat VERSION)" && git push )
   ```

3. Verify build on a clean Arch environment:
   ```bash
   cd /tmp/apex-launcher-bin-aur
   makepkg -si
   ```

Notes:
- Ensure `source=("https://github.com/reza-ygb/apex-launcher/archive/v$pkgver.tar.gz")` matches the GitHub tag.
- Update `sha256sums` after the release is published:
  ```bash
  updpkgsums
  ```
