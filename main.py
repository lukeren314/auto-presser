import pyautogui
import keyboard
import time

MAIN_DELAY = 1

ACTIVATE_HOTKEY = '`'
SHUTDOWN_HOTKEY = 'ctrl+shift+del'
switch = False
on = True

def move_mouse_to(x, y):
    pass

def click(duration):
    pass

def hold_click():
    pass

def release_click():
    pass

def press_button(key, duration=0.01):
    hold_button(key)
    wait(duration)
    release_button(key)

def hold_button(key):
    pyautogui.keyDown(key)

def release_button(key):
    pyautogui.keyUp(key)

def wait(time):
    time.sleep(time)

def doPresses():
    pass

def activate():
    global switch
    switch = not switch
    print(f"Switch {('On' if switch else 'Off')}")

if __name__ == "__main__":
    keyboard.add_hotkey(ACTIVATE_HOTKEY, activate)
    keyboard.add_hotkey(ACTIVATE_HOTKEY, activate)
    while on:
        while switch:
            doPresses()
            time.sleep(MAIN_DELAY)