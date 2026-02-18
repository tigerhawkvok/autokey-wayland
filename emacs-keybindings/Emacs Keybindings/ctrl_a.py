# Emacs Keybinding: Ctrl+A - Beginning of Line
# Hotkey: Ctrl+A
# Emacs equivalent: C-a (move-beginning-of-line)
#
# Moves cursor to beginning of line.
# If mark mode is active (Ctrl+Space), extends selection.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, get_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+a")
elif get_mark(store):
    keyboard.send_keys("<shift>+<home>")
else:
    keyboard.send_keys("<home>")
