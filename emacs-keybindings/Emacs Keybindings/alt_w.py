# Emacs Keybinding: Alt+W - Copy Region (Kill Ring Save)
# Hotkey: Alt+W
# Emacs equivalent: M-w (kill-ring-save)
#
# Copies selected text to clipboard without cutting.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<alt>+w")
else:
    keyboard.send_keys("<ctrl>+c")
    set_mark(store, False)
