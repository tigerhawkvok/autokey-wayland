# Emacs Keybinding: Ctrl+G - Quit / Keyboard Quit
# Hotkey: Ctrl+G
# Emacs equivalent: C-g (keyboard-quit)
#
# Sends Escape and resets all emacs state (prefix, mark mode).

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, reset_all

if is_excluded(window):
    keyboard.send_keys("<ctrl>+g")
else:
    reset_all(store)
    keyboard.send_keys("<escape>")
