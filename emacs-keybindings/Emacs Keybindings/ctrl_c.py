# Emacs Keybinding: Ctrl+C / Kill Emacs
# Hotkey: Ctrl+C
# Emacs equivalent: C-x C-c (save-buffers-kill-terminal) when prefixed; passthrough otherwise
#
# After Ctrl+X: closes window (Alt+F4)
# Otherwise: passes through native Ctrl+C (usually "Copy")

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, get_pre_x, set_pre_x

if is_excluded(window):
    keyboard.send_keys("<ctrl>+c")
elif get_pre_x(store):
    # C-x C-c → close window
    set_pre_x(store, False)
    keyboard.send_keys("<alt>+<f4>")
else:
    # Pass through native Ctrl+C
    keyboard.send_keys("<ctrl>+c")
