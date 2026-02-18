# Emacs Keybinding: Ctrl+R - Incremental Search Backward
# Hotkey: Ctrl+R
# Emacs equivalent: C-r (isearch-backward)
#
# Opens find/search dialog (same as forward search on most Linux apps).

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+r")
else:
    set_mark(store, False)
    keyboard.send_keys("<ctrl>+f")
