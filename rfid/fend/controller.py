import time
import webbrowser
import uinput

device = uinput.Device([
        uinput.KEY_LEFTCTRL,
        uinput.KEY_W,
        ])

webbrowser.open_new_tab("https://python.org")
time.sleep(10)
device.emit_combo([
        uinput.KEY_LEFTCTRL,
        uinput.KEY_W,
        ])
webbrowser.open_new_tab("https://eff.org")
