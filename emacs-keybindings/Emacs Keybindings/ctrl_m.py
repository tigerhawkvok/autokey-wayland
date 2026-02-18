# Emacs Keybinding: Ctrl+M - Newline
# Hotkey: Ctrl+M
# Emacs equivalent: C-m (newline)
#
# Sends Enter key.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+m")
else:
    set_mark(store, False)
    keyboard.send_keys("<enter>")
