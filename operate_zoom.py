import pyautogui as pg
import sys
print('Press Ctrl-C to quit.')
try:
    while True:
        pg.press('win')
        pg.PAUSE=1
        pg.write('zoom')
        pg.PAUSE=1
        pg.press('enter')
        break
except KeyboardInterrupt:
    print('\n')