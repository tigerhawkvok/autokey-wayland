# Emacs Keybinding: Ctrl+F / Find File
# Hotkey: Ctrl+F
# Emacs equivalent: C-x C-f (find-file) when prefixed; passthrough otherwise
#
# After Ctrl+X: opens file dialog (Ctrl+O)
# Otherwise: passes through native Ctrl+F (usually "Find")

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, get_pre_x, set_pre_x

if is_excluded(window):
    keyboard.send_keys("<ctrl>+f")
elif get_pre_x(store):
    # C-x C-f → find/open file
    set_pre_x(store, False)
    keyboard.send_keys("<ctrl>+o")
else:
    # Pass through native Ctrl+F
    keyboard.send_keys("<ctrl>+f")
