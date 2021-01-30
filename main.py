import pyautogui
import time

MAIN_DELAY = 1

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
def press_button(key, duration):
    pass

def hold_button(key):
    pass

def release_button(key):
    pass

def wait(time):
    pass




def doPresses():
    pass



if __name__ == "__main__":
    while on:
        while switch:
            doPresses()
            time.sleep(MAIN_DELAY)