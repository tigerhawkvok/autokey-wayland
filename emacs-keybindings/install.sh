#!/usr/bin/env bash
# Install emacs keybindings for AutoKey
#
# This script copies the helper module and keybinding scripts
# to the AutoKey configuration directory.
#
# Usage:
#   ./install.sh          # Install (with confirmation)
#   ./install.sh --force  # Install without confirmation

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOKEY_CONFIG="${AUTOKEY_CONFIG_DIR:-$HOME/.config/autokey}"
AUTOKEY_DATA="$AUTOKEY_CONFIG/data"
TARGET_FOLDER="$AUTOKEY_DATA/Emacs Keybindings"

echo "=== AutoKey Emacs Keybindings Installer ==="
echo ""
echo "Source:      $SCRIPT_DIR"
echo "Config dir:  $AUTOKEY_CONFIG"
echo "Scripts dir: $TARGET_FOLDER"
echo ""

# Check if AutoKey config directory exists
if [ ! -d "$AUTOKEY_CONFIG" ]; then
    echo "WARNING: AutoKey config directory not found at $AUTOKEY_CONFIG"
    echo "Creating it. You may need to run AutoKey once first to generate defaults."
    mkdir -p "$AUTOKEY_CONFIG"
fi

if [ ! -d "$AUTOKEY_DATA" ]; then
    mkdir -p "$AUTOKEY_DATA"
fi

# Confirm installation
if [ "${1:-}" != "--force" ]; then
    if [ -d "$TARGET_FOLDER" ]; then
        echo "WARNING: $TARGET_FOLDER already exists."
        echo "Existing files will be overwritten."
        echo ""
    fi
    read -rp "Proceed with installation? [y/N] " response
    if [[ ! "$response" =~ ^[yY] ]]; then
        echo "Installation cancelled."
        exit 0
    fi
fi

# Install helper module
echo ""
echo "Installing helper module..."
cp "$SCRIPT_DIR/emacs_helpers.py" "$AUTOKEY_CONFIG/emacs_helpers.py"
echo "  → $AUTOKEY_CONFIG/emacs_helpers.py"

# Install keybinding scripts
echo "Installing keybinding scripts..."
mkdir -p "$TARGET_FOLDER"
cp "$SCRIPT_DIR/Emacs Keybindings/.folder.json" "$TARGET_FOLDER/.folder.json"

for pyfile in "$SCRIPT_DIR/Emacs Keybindings/"*.py; do
    basename="$(basename "$pyfile" .py)"
    jsonfile="$SCRIPT_DIR/Emacs Keybindings/${basename}.json"

    cp "$pyfile" "$TARGET_FOLDER/"
    if [ -f "$jsonfile" ]; then
        cp "$jsonfile" "$TARGET_FOLDER/"
    fi
    echo "  → $basename"
done

echo ""
echo "=== Installation complete ==="
echo ""
echo "Next steps:"
echo "  1. Edit $AUTOKEY_CONFIG/emacs_helpers.py"
echo "     to add window exclusion patterns for your system."
echo "  2. Restart AutoKey to load the new scripts."
echo "  3. Use Ctrl+Alt+Shift+W to discover WM_CLASS values"
echo "     of windows you want to exclude."
echo ""
echo "See README.md for full documentation."
