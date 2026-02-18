"""
Emacs Keybinding Helpers for AutoKey
=====================================

Shared helper module used by all emacs keybinding scripts.

Installation:
    Place this file at ~/.config/autokey/emacs_helpers.py

Configuration:
    Edit the EXCLUDED_PATTERNS list below to add applications where
    emacs keybindings should NOT apply.
"""

import re

# ============================================================
# WINDOW EXCLUSION LIST
# ============================================================
# Add regex patterns matching WM_CLASS or WM_TITLE values of
# applications where you do NOT want emacs keybindings to apply.
#
# These keybindings are OPT-OUT: they apply everywhere by default.
# Add patterns here for windows that should be excluded.
#
# To discover the WM_CLASS of a window:
#   X11:     xprop WM_CLASS  (then click the window)
#   Wayland: Create an AutoKey script with:
#               import subprocess
#               wm = window.get_active_class()
#               subprocess.Popen(["notify-send", "WM_CLASS", wm])
#   Both:    Use the included "Show WM Class" debug script
#
# Common patterns you might want to exclude:
#   r"gnome-terminal"           - GNOME Terminal
#   r"kitty"                    - Kitty terminal
#   r"Alacritty"                - Alacritty terminal
#   r"konsole"                  - KDE Konsole
#   r"org\.wezfurlong\.wezterm" - WezTerm
#   r"code\.Code"               - Visual Studio Code
#   r"Emacs"                    - GNU Emacs
#   r"jetbrains-.*"             - JetBrains IDEs (have their own emacs mode)
#   r"vim|gvim"                 - GVim

EXCLUDED_PATTERNS = [
    # Uncomment or add patterns for YOUR system.
    # Since this is Linux, the specific window classes will differ
    # from the original Windows AutoHotKey script. Discover them
    # as you encounter apps where these bindings conflict.

    # Terminals (usually have native emacs-style line editing):
    # r"gnome-terminal",
    # r"kitty",
    # r"Alacritty",
    # r"konsole",
    # r"org\.wezfurlong\.wezterm",

    # Editors/IDEs (usually have their own emacs keybinding modes):
    # r"code\.Code",
    # r"Emacs",
    # r"jetbrains-.*",

    # Virtual machines / remote desktops:
    # r"virt-manager",
    # r"remmina",
]


# ============================================================
# Internal implementation
# ============================================================

_excluded_re = None


def _build_excluded_regex():
    global _excluded_re
    active_patterns = [p for p in EXCLUDED_PATTERNS if p]
    if active_patterns:
        combined = "|".join("(?:{})".format(p) for p in active_patterns)
        _excluded_re = re.compile(combined, re.IGNORECASE)
    else:
        _excluded_re = False  # sentinel: no exclusions configured


def is_excluded(window_obj):
    """
    Check if the currently active window should be excluded
    from emacs keybindings.

    Args:
        window_obj: The AutoKey `window` API object

    Returns:
        True if the window is excluded, False otherwise
    """
    global _excluded_re
    if _excluded_re is None:
        _build_excluded_regex()
    if _excluded_re is False:
        return False
    wm_class = window_obj.get_active_class() or ""
    wm_title = window_obj.get_active_title() or ""
    return bool(_excluded_re.search(wm_class) or _excluded_re.search(wm_title))


# ---- State management using AutoKey global store ----

def get_pre_x(store_obj):
    """Get the Ctrl+X prefix state (True if Ctrl+X was just pressed)."""
    return bool(store_obj.get_global_value("emacs_pre_x"))


def set_pre_x(store_obj, value):
    """Set the Ctrl+X prefix state."""
    store_obj.set_global_value("emacs_pre_x", bool(value))


def get_mark(store_obj):
    """Get the mark/selection mode state (set by Ctrl+Space)."""
    return bool(store_obj.get_global_value("emacs_mark"))


def set_mark(store_obj, value):
    """Set the mark/selection mode state."""
    store_obj.set_global_value("emacs_mark", bool(value))


def reset_all(store_obj):
    """Reset all emacs state. Called by Ctrl+G (quit)."""
    store_obj.set_global_value("emacs_pre_x", False)
    store_obj.set_global_value("emacs_mark", False)
