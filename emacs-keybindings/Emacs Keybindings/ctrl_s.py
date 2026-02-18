# Emacs Keybinding: Ctrl+S / Save or Search
# Hotkey: Ctrl+S
# Emacs equivalent: C-x C-s (save-buffer) when prefixed; C-s (isearch-forward) otherwise
#
# After Ctrl+X: saves the current file/document (Ctrl+S)
# Otherwise: opens find/search dialog (Ctrl+F)

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, get_pre_x, set_pre_x, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+s")
elif get_pre_x(store):
    # C-x C-s → save buffer
    set_pre_x(store, False)
    keyboard.send_keys("<ctrl>+s")
else:
    # C-s → isearch-forward (mapped to native Find)
    set_mark(store, False)
    keyboard.send_keys("<ctrl>+f")
