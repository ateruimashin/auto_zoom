import pyautogui as pg
import sys
from functools import wraps
import time
print('Press Ctrl-C to quit.')

def stop_watch(func):
    @wraps(func)
    def wrapper(*args,**kargs):
        start = time.time()
        result = func(*args,**kargs)
        elapsed_time = time.time() - start
        print(f"{func.__name__}は{elapsed_time:.2f}秒かかりました")
        return result
    return wrapper

def run_zoom():
    pg.press('win')
    pg.PAUSE = 3
    pg.write('zoom')
    pg.PAUSE = 3
    pg.press('enter')

@stop_watch
def start_meeting():
    buttton_active = [r'button\active\zoom_meeting_active.PNG',r'button\active\zoom_igrashi_meeting_active.PNG']
    button_nonactive = [r'button\nonactive\zoom_meeting_non.PNG',r'button\nonactive\zoom_igarashi_meeting_non.PNG']
    button_start = r'button\active\zoom_igarashi-meeting_start.PNG'
    for button_a, button_n in zip(buttton_active, button_nonactive):
        button_loc_n = pg.locateOnScreen(button_n)

        if button_loc_n is None:
            button_loc_a = pg.locateOnScreen(button_a)
            if button_loc_a is None:
                sys.exit()
            else:
                continue
        else:
            button_loc = button_loc_n

        button_center = pg.center(button_loc)
        button_x, button_y = button_center
        pg.click(button_x,button_y)
        pg.PAUSE = 1
    button_x, button_y = pg.center(pg.locateOnScreen(button_start))
    pg.click(button_x,button_y)
    
try:
    while True:
        run_zoom()
        pg.PAUSE = 1.5
        start_meeting()
        break
except KeyboardInterrupt:
    print('\n')