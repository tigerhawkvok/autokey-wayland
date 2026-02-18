# Emacs Keybinding: Ctrl+X Prefix
# Hotkey: Ctrl+X
# Emacs equivalent: C-x prefix key
#
# Toggles the Ctrl+X prefix state. If already in prefix state,
# sends a real Ctrl+X (cut) instead.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, get_pre_x, set_pre_x

if is_excluded(window):
    keyboard.send_keys("<ctrl>+x")
elif get_pre_x(store):
    # Ctrl+X pressed twice → send real Ctrl+X (cut)
    set_pre_x(store, False)
    keyboard.send_keys("<ctrl>+x")
else:
    # Enter Ctrl+X prefix mode, waiting for next key
    set_pre_x(store, True)
