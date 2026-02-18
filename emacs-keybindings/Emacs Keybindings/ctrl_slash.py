# Emacs Keybinding: Ctrl+/ - Undo
# Hotkey: Ctrl+/
# Emacs equivalent: C-_ or C-/ (undo)
#
# Note: The original AHK script used Ctrl+_ (Ctrl+Shift+-).
# Ctrl+/ is the more common and ergonomic emacs undo binding.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+/")
else:
    keyboard.send_keys("<ctrl>+z")
    set_mark(store, False)
