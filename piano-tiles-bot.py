from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(749, 698)[0] == 0:
        click(749, 698)
    if pyautogui.pixel(908, 698)[0] == 0:
        click(908, 698)
    if pyautogui.pixel(1019, 698)[0] == 0:
        click(1019, 698)
    if pyautogui.pixel(1159, 698)[0] == 0:
        click(1159, 698)
