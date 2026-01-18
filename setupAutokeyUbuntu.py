#!python3

from pathlib import Path
import subprocess


def dependencies():
    subprocess.run(["sudo", "apt", "update"], check= True)
    subprocess.run([
        "sudo", "apt", "install",
        "make", "build-essential", "libcairo2-dev",
        "python3-venv", "gnome-shell-extension-manager",
        "libgirepository-2.0-dev", "libayatana-appindicator3-dev",
        "-y"
    ], check= True)
    subprocess.run([
        "xargs", "-a", "apt-requirements.txt", "sudo", "apt", "install", "-y"
    ], check= True)
    _ = input("If you're on Fedora, please install the requirements as listed in the `wayland-install.md` file now, then press any key to continue...")
    subprocess.run([
        "./setupAutokey.sh"
    ], check= True)


if __name__ == "__main__":
    dependencies()
