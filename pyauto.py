import time

import pyautogui

time.sleep(5)
screen=pyautogui.screenshot(region=(0,100,250,250))
screen.save('2.png')
print('finished')