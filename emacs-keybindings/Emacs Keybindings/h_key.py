# Emacs Keybinding: h / Select All
# Hotkey: h (bare key, no modifier)
# Emacs equivalent: C-x h (mark-whole-buffer) when prefixed; passthrough otherwise
#
# After Ctrl+X: selects all text (Ctrl+A)
# Otherwise: types the letter 'h'
#
# NOTE: This intercepts every 'h' keypress system-wide.
# If you experience latency while typing, you may want to disable
# this script and use a different approach for C-x h.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, get_pre_x, set_pre_x

if is_excluded(window):
    keyboard.send_keys("h")
elif get_pre_x(store):
    # C-x h → select all
    set_pre_x(store, False)
    keyboard.send_keys("<ctrl>+a")
else:
    # Just type 'h'
    keyboard.send_keys("h")
