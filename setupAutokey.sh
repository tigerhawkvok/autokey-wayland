#!/bin/bash

cd autokey-gnome-extension
make
gnome-extensions install autokey-gnome-extension@autokey.zip
#  Add a new udev rule configuration file that grants the "input" user group access to the /dev/uinput kernel device (copy these three lines together as one into a terminal window and press enter)
sudo tee /etc/udev/rules.d/10-autokey.rules > /dev/null <<EOF
KERNEL=="uinput", SUBSYSTEM=="misc", OPTIONS+="static_node=uinput", TAG+="uaccess", GROUP="input", MODE="0660"
EOF

read -n1 -r -p "Press any key to restart..." key
sudo shutdown -r now
