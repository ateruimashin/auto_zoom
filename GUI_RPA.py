import PySimpleGUI as sg
import datetime as dt
import time

sg.theme('DarkBrown1')

layout = [
          [sg.Text('Next', size=(5,1), justification='left'),sg.Text(size=(20,1), key='-DATE-')],
          [sg.Text('Log', size=(5,1), justification='left')],
          [sg.Output(size=(100,5), key='-LOG-')],
          [sg.Button('Start/Stop', focus=True),sg.Quit()]
         ]

window = sg.Window('ミーティング開催', layout)

RPA_running = False

while True:
    event, values = window.read(timeout=5000) #timeoutを指定しないとループが1回回って止まる。数値はms。
    if event in ('Quit'):
        break
    elif event == 'Start/Stop':
        RPA_running = not RPA_running
    if RPA_running:
        now = dt.datetime.now()
        window['-DATE-'].update("{0:%m/%d %H:%M:%S}".format(now))
        print("{0:%m/%d %H:%M:%S}".format(now))

window.close()