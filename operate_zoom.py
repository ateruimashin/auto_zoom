#! python3
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    pyautogui.moveTo(10,10)
    while True:
        pyautogui.move(50,50,0.5)
        x,y=pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

        if y >= 700:
            pyautogui.moveTo(0,0)
except KeyboardInterrupt:
    print('\n')