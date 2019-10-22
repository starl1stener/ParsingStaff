import pyautogui
from time import sleep

num = 1

while num != 1000:
    screenshot = pyautogui.screenshot()
    screenshot.save(str(num) + ".png")
    sleep(1)
    pyautogui.typewrite(['pagedown'])
    num += 1
    sleep(1)



