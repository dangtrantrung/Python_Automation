import time

import pyautogui as pag

pos=pag.position()
print(pos)
# click source control button
pos1=24,188
time.sleep(3)
# for _ in range(3):
#     pag.click(pos1)
pag.click(pos1)
