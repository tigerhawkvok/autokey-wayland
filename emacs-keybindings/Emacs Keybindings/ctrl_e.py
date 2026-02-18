# Emacs Keybinding: Ctrl+E - End of Line
# Hotkey: Ctrl+E
# Emacs equivalent: C-e (move-end-of-line)
#
# Moves cursor to end of line.
# If mark mode is active (Ctrl+Space), extends selection.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, get_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+e")
elif get_mark(store):
    keyboard.send_keys("<shift>+<end>")
else:
    keyboard.send_keys("<end>")
