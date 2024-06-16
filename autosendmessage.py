import pyautogui
import time
time.sleep(3)
count=0
while count<=101:
    pyautogui.typewrite("I Love you"+str(count))
    pyautogui.press("enter")
    count=count+1