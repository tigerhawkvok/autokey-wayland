# Emacs Keybinding: Ctrl+J - Newline and Indent
# Hotkey: Ctrl+J
# Emacs equivalent: C-j (newline-and-indent)
#
# Sends Enter followed by Tab.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+j")
else:
    set_mark(store, False)
    keyboard.send_keys("<enter>")
    keyboard.send_keys("<tab>")
