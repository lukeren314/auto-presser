import pyautogui
import keyboard
import time

MAIN_DELAY = 1

ACTIVATE_HOTKEY = '`'
SHUTDOWN_HOTKEY = 'ctrl+shift+del'
switch = False
on = True

def move_mouse_to(x, y, duration=0):
    pyautogui.moveTo(x, y, duration=duration)

def click(button="left", duration=0.01):
    pyautogui.mouseDown(button=button)
    wait(duration)
    pyautogui.mouseUp(button=button)

def hold_click(button="left"):
    pyautogui.mouseDown(button=button)

def release_click(button="left"):
    pyautogui.mouseUp(button=button)
#up is jeremy down is luke

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

def shutdown():
    global on
    on = False

if __name__ == "__main__":
    keyboard.add_hotkey(ACTIVATE_HOTKEY, activate)
    keyboard.add_hotkey(SHUTDOWN_HOTKEY, shutdown)
    while on:
        while switch:
            doPresses()
            time.sleep(MAIN_DELAY)