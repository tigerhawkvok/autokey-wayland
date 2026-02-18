# Emacs Keybinding: Ctrl+K - Kill Line
# Hotkey: Ctrl+K
# Emacs equivalent: C-k (kill-line)
#
# Selects from cursor to end of line and cuts to clipboard.

import sys, os
import time
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+k")
else:
    set_mark(store, False)
    keyboard.send_keys("<shift>+<end>")
    time.sleep(0.05)
    keyboard.send_keys("<ctrl>+x")
