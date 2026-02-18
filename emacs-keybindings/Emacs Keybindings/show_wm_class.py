# Debug Helper: Show WM Class
# Hotkey: Ctrl+Alt+Shift+W
#
# Displays the WM_CLASS of the currently focused window.
# Use this to discover window class names for the exclusion list
# in emacs_helpers.py.

import subprocess

wm_class = window.get_active_class() or "(unknown)"
wm_title = window.get_active_title() or "(unknown)"

msg = "WM_CLASS: {}\nWM_TITLE: {}".format(wm_class, wm_title)

try:
    subprocess.Popen(["notify-send", "AutoKey - Window Info", msg])
except FileNotFoundError:
    # notify-send not available, try zenity
    try:
        subprocess.Popen(["zenity", "--info", "--title=Window Info", "--text=" + msg])
    except FileNotFoundError:
        # Last resort: use xdg-open or just print
        pass
