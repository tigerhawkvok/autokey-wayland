# Emacs Keybindings for AutoKey

Systemwide emacs-like keyboard shortcuts for Linux, converted from the
[Windows AutoHotKey script](https://github.com/tigerhawkvok/emacs.ahk).

These keybindings are **opt-out**: they apply everywhere by default.
You add exclusions for specific applications where they shouldn't apply.

## Installation

```bash
cd emacs-keybindings
./install.sh
```

This copies:
- `emacs_helpers.py` → `~/.config/autokey/emacs_helpers.py` (shared helper module)
- `Emacs Keybindings/` → `~/.config/autokey/data/Emacs Keybindings/` (all scripts)

Then restart AutoKey.

## Configuration: Excluding Applications

Edit `~/.config/autokey/emacs_helpers.py` and add regex patterns to the
`EXCLUDED_PATTERNS` list for windows where emacs keybindings should NOT apply:

```python
EXCLUDED_PATTERNS = [
    r"gnome-terminal",      # GNOME Terminal
    r"kitty",               # Kitty terminal
    r"code\.Code",          # VS Code
    r"Emacs",               # GNU Emacs
    r"jetbrains-.*",        # JetBrains IDEs
]
```

### Discovering Window Classes

Use the included **Show WM Class** debug script:
- Press **Ctrl+Alt+Shift+W** in any window
- A notification will show the `WM_CLASS` and `WM_TITLE`
- Add the relevant pattern to `EXCLUDED_PATTERNS`

## Keybinding Reference

### Navigation

| Hotkey | Emacs | Action |
|--------|-------|--------|
| `Ctrl+A` | `C-a` | Beginning of line |
| `Ctrl+E` | `C-e` | End of line |

### Editing

| Hotkey | Emacs | Action |
|--------|-------|--------|
| `Ctrl+K` | `C-k` | Kill (cut) to end of line |
| `Ctrl+D` | — | Duplicate current line |
| `Ctrl+M` | `C-m` | Newline (Enter) |
| `Ctrl+J` | `C-j` | Newline and indent (Enter + Tab) |
| `Ctrl+I` | `C-i` | Indent / Tab |
| `Ctrl+/` | `C-/` | Undo |

### Selection & Clipboard

| Hotkey | Emacs | Action |
|--------|-------|--------|
| `Ctrl+Space` | `C-SPC` | Toggle mark (selection) mode |
| `Ctrl+W` | `C-w` | Kill (cut) region, or pass through if nothing selected |
| `Alt+W` | `M-w` | Copy region |
| `Ctrl+Y` | `C-y` | Yank (paste) |

### Search

| Hotkey | Emacs | Action |
|--------|-------|--------|
| `Ctrl+S` | `C-s` | Incremental search forward (opens Find) |
| `Ctrl+R` | `C-r` | Incremental search backward (opens Find) |

### Ctrl+X Prefix Commands

Press `Ctrl+X` first, then the second key:

| Sequence | Emacs | Action |
|----------|-------|--------|
| `C-x C-f` | `C-x C-f` | Find/open file (sends Ctrl+O) |
| `C-x C-s` | `C-x C-s` | Save file (sends Ctrl+S) |
| `C-x C-c` | `C-x C-c` | Close window/quit (sends Alt+F4) |
| `C-x h` | `C-x h` | Select all (sends Ctrl+A) |
| `C-x C-x` | — | Send real Ctrl+X (cut) |

### Other

| Hotkey | Emacs | Action |
|--------|-------|--------|
| `Ctrl+G` | `C-g` | Quit / cancel (Escape + reset all state) |
| `Ctrl+F` | — | Pass through (native Find), or `C-x C-f` for open file |
| `Ctrl+C` | — | Pass through (native Copy), or `C-x C-c` for close |

### Debug

| Hotkey | Action |
|--------|--------|
| `Ctrl+Alt+Shift+W` | Show WM_CLASS/WM_TITLE of focused window |

## Mark Mode (Selection)

Press `Ctrl+Space` to enter mark mode. While active, navigation keys
(`Ctrl+A`, `Ctrl+E`) will extend the selection instead of just moving the cursor.

Deactivate mark mode by:
- Pressing `Ctrl+Space` again
- Pressing `Ctrl+G` (quit)
- Performing a clipboard operation (`Ctrl+W`, `Alt+W`, `Ctrl+Y`)

## Architecture

```
~/.config/autokey/
├── emacs_helpers.py              # Shared module (exclusion list, state management)
└── data/
    └── Emacs Keybindings/        # AutoKey script folder
        ├── .folder.json          # Folder metadata
        ├── ctrl_a.py + .json     # Individual keybinding scripts
        ├── ctrl_e.py + .json
        ├── ctrl_k.py + .json
        └── ...
```

**State management**: Scripts share state via AutoKey's global store
(`store.set_global_value()` / `store.get_global_value()`). State variables:
- `emacs_pre_x` — True when `Ctrl+X` prefix is active
- `emacs_mark` — True when mark/selection mode is active

**Exclusion checking**: Each script imports `emacs_helpers.py` and calls
`is_excluded(window)`. If the active window matches any pattern in
`EXCLUDED_PATTERNS`, the script passes through the original keystroke.

## Notes

- The **bare `h` key** is intercepted system-wide (matching the original AHK
  script). This adds negligible latency but if it bothers you, delete
  `h_key.py` + `h_key.json` — you'll lose `C-x h` (select all) but nothing
  else.

- **Ctrl+Space** may conflict with input method switching (e.g., IBus, Fcitx).
  If so, remap your input method toggle to a different key in your desktop
  settings.

- **Ctrl+/** (undo) replaces the original AHK's `Ctrl+_` (`Ctrl+Shift+-`).
  Both are standard emacs undo bindings; `/` is more ergonomic.

- Functions defined in the original AHK script but not bound to hotkeys
  (`forward_char`, `backward_char`, `previous_line`, `next_line`,
  `scroll_up`, `scroll_down`, `delete_char`, `delete_backward_char`) were
  not converted since they had no hotkey bindings. You can easily add them
  by creating new script files following the same pattern.
