# Emacs Keybinding: Ctrl+I - Indent / Tab
# Hotkey: Ctrl+I
# Emacs equivalent: C-i (indent-for-tab-command)
#
# Sends Tab key.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+i")
else:
    set_mark(store, False)
    keyboard.send_keys("<tab>")
