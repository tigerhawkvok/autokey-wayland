# Emacs Keybinding: Ctrl+D - Duplicate Line
# Hotkey: Ctrl+D
# Emacs equivalent: custom duplicate-line (not standard emacs)
#
# Copies the current line and pastes it on a new line below.

import sys, os
import time
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+d")
else:
    set_mark(store, False)
    # Select entire line
    keyboard.send_keys("<home>")
    keyboard.send_keys("<shift>+<end>")
    time.sleep(0.05)
    # Copy
    keyboard.send_keys("<ctrl>+c")
    time.sleep(0.05)
    # New line and paste
    keyboard.send_keys("<end>")
    keyboard.send_keys("<enter>")
    keyboard.send_keys("<ctrl>+v")
