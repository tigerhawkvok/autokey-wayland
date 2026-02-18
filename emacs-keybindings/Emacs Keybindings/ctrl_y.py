# Emacs Keybinding: Ctrl+Y - Yank (Paste)
# Hotkey: Ctrl+Y
# Emacs equivalent: C-y (yank)
#
# Pastes from clipboard.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+y")
else:
    keyboard.send_keys("<ctrl>+v")
    set_mark(store, False)
