# Emacs Keybinding: Ctrl+Space - Set/Toggle Mark
# Hotkey: Ctrl+Space
# Emacs equivalent: C-SPC / C-@ (set-mark-command)
#
# Toggles mark mode. When mark is active, movement keys extend the selection.
# Press again or Ctrl+G to deactivate.
#
# NOTE: Ctrl+Space may conflict with input method switching on some
# Linux desktop environments. If so, remap your input method toggle
# to a different key combination.

import sys, os
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, get_mark, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+ ")
else:
    if get_mark(store):
        set_mark(store, False)
    else:
        set_mark(store, True)
