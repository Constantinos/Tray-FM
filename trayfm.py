#!/usr/bin/env python3
import subprocess
from pathlib import Path

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("AyatanaAppIndicator3", "0.1")
from gi.repository import Gtk, AyatanaAppIndicator3

#!/usr/bin/env python3

import os
import subprocess
from pathlib import Path

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("AyatanaAppIndicator3", "0.1")
from gi.repository import Gtk, AyatanaAppIndicator3

HOME = Path.home()

FILES = [
    HOME / ".shelldio" / "my_stations.txt",
    HOME / ".shelldio" / "all_stations.txt",
]

mpv_proc = None


def stations():
    for f in FILES:
        if f.exists():
            out = []

            for line in f.read_text(errors="ignore").splitlines():
                if "," in line:
                    name, url = line.split(",", 1)
                    out.append((name.strip(), url.strip()))

            return out

    return []


def stop(*_):
    global mpv_proc

    if mpv_proc and mpv_proc.poll() is None:
        mpv_proc.terminate()

        try:
            mpv_proc.wait(timeout=2)
        except Exception:
            mpv_proc.kill()

    mpv_proc = None


def play(_item, url):
    global mpv_proc

    stop()

    mpv_proc = subprocess.Popen(
        ["mpv", "--no-video", url],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )


def quit_app(*_):
    stop()
    Gtk.main_quit()
    os._exit(0)


# Δημιουργία menu
menu = Gtk.Menu()

for name, url in stations():
    item = Gtk.MenuItem(label=name)
    item.connect("activate", play, url)
    menu.append(item)

menu.append(Gtk.SeparatorMenuItem())

stop_item = Gtk.MenuItem(label="Stop")
stop_item.connect("activate", stop)
menu.append(stop_item)

exit_item = Gtk.MenuItem(label="Exit")
exit_item.connect("activate", quit_app)
menu.append(exit_item)

menu.show_all()

# Δημιουργία indicator
indicator = AyatanaAppIndicator3.Indicator.new(
    "shelldio-tray",
    "multimedia-player",
    AyatanaAppIndicator3.IndicatorCategory.APPLICATION_STATUS
)

indicator.set_status(
    AyatanaAppIndicator3.IndicatorStatus.ACTIVE
)

indicator.set_menu(menu)

Gtk.main()
