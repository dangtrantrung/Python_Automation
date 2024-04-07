import time

import pyautogui as pag

time.sleep(2)
print(pag.position())
pag.moveTo(8,767)
time.sleep(1)

# click browser
pag.click(329,743)
time.sleep(2)
# search text
pag.typewrite('vnexpress')
time.sleep(1)
pag.press('enter')
time.sleep(5)
print(pag.position())
# click top 1 - page search result
pag.click(216,487)
