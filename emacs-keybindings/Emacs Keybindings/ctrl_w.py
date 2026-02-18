# Emacs Keybinding: Ctrl+W - Kill Region
# Hotkey: Ctrl+W
# Emacs equivalent: C-w (kill-region)
#
# If text is selected (mark mode), cuts it.
# If nothing is selected, passes through native Ctrl+W (close tab in browsers, etc.)

import sys, os
import time
sys.path.insert(0, os.path.expanduser("~/.config/autokey"))
from emacs_helpers import is_excluded, set_mark

if is_excluded(window):
    keyboard.send_keys("<ctrl>+w")
else:
    # Save current clipboard to detect if copy succeeds
    old_clip = clipboard.get_clipboard()
    clipboard.fill_clipboard("")

    # Attempt to copy the selection
    keyboard.send_keys("<ctrl>+c")
    time.sleep(0.1)

    new_clip = clipboard.get_clipboard()
    if new_clip:
        # Something was selected and copied → now cut it
        keyboard.send_keys("<ctrl>+x")
        set_mark(store, False)
    else:
        # Nothing was selected → restore clipboard and pass through
        clipboard.fill_clipboard(old_clip)
        keyboard.send_keys("<ctrl>+w")
