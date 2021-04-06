import PySimpleGUI as sg
import datetime as dt
import getschedule as gs
import operate_zoom as oz

sg.theme('DarkBrown1')

layout = [
          [sg.Text('Next', size = (5,1), justification = 'left'), sg.Text(size = (20,1), key='-START-'),sg.Text('~',size = (6,1)), sg.Text(size=(20,1), key='-END-')],
          [sg.Text('Now',size = (5,1),justification = 'left'),sg.Text(size=(20,1), key = '-NOW-')],
          [sg.Text('Log', size  =(5,1), justification = 'left')],
          [sg.Output(size=(100,10), key='-LOG-')],
          [sg.Button('Start/Stop', focus=True), sg.Quit()]
         ]

window = sg.Window('ミーティング開催', layout)

RPA_running = False
next_start_date, next_end_date = '0000-00-00 00:00', '0000-00-00 00:00'
count = -1  #初回ループ時に予定取得させるため


while True:
    event, values = window.read(timeout=60000)  #ループ間隔は60秒

    #現在時刻を取得
    now = dt.datetime.now()

    #比較のためにstr型に変換
    now_date = now.strftime('%Y-%m-%d %H:%M')

    #現在時刻の表示
    window['-NOW-'].update(now_date)

    if event in ('Quit'):
        break
    elif event == 'Start/Stop':
        RPA_running = not RPA_running
        if RPA_running:
            print('{} Start'.format(now_date))
        else:
            print('{} Stop'.format(now_date))

    if RPA_running:

        #30分間隔で予定取得
        if count == -1 or count == 30:

            #カウンタを戻す
            count = 0

            #予定を5つ取得し、直近の予定の開始時刻と終了時刻を格納
            schedule = gs.get_events()
            start_date = schedule[0]
            end_date = schedule[1]

            #予定を整形
            start_date = start_date[0:10] + ' ' + start_date[11:16]
            end_date = end_date[0:10] + ' ' + end_date[11:16]

            #予定を取得したらログに記述
            print('{} Get next schedule'.format(now_date))

            #次の予定が変更されたらログに記述
            if start_date != next_start_date:
                next_start_date = start_date
                next_end_date = end_date
                print('{} Update next schedule'.format(now_date))

            #GUI表示
            window['-START-'].update(start_date)
            window['-END-'].update(end_date)

        #開始時刻になったらZoomを立ち上げる
        if start_date == now_date:
            print('Start meeting')
            oz.Operate()
        
        #カウンタを増やす
        count += 1
            
window.close()