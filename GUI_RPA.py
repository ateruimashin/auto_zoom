import PySimpleGUI as sg
import datetime as dt
import getschedule as gs
import operate_zoom as oz
import time

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
interval = 0 #ミーティング開始時、終了時から1分間カウントする変数
zoom_flag = False   #何度も起動するのを防ぐため。Trueの場合1分経過でFalseに戻す。


while True:
    event, values = window.read(timeout=1000)  #ループ間隔は1秒

    #現在時刻を取得
    now = dt.datetime.now()

    #時刻表示のために整形
    now_time = now.strftime('%Y-%m-%d %H:%M:%S')

    #比較のためにstr型に変換
    now_date = now.strftime('%Y-%m-%d %H:%M')

    #現在時刻の表示
    window['-NOW-'].update(now_time)

    #ボタン操作
    if event in ('Quit'):
        break
    elif event == 'Start/Stop':
        RPA_running = not RPA_running
        if RPA_running:
            print('{} Start'.format(now_date))
        else:
            print('{} Stop'.format(now_date))
            #再開時に予定を取得させるため
            count = -1

    if RPA_running:

        #30分間隔で予定取得
        if count == -1 or count == 1800:

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

        #ミーティング開始時、終了時にカウントを始める
        if zoom_flag == True:
            interval += 1

        #60秒経過したらフラッグを反転させ、変数を初期値に戻す
        if interval == 60:
            zoom_flag = not zoom_flag
            interval = 0

        #開始時刻かつ直前にミーティングを起動していないならミーティングを開始する
        if start_date == now_date and zoom_flag == False:
            zoom_flag = True
            oz.Start_Zoom()
            print('{} Start meeting'.format(now_date))
            
            #タイミング調整
            time.sleep(5)

            #画面共有開始
            oz.screen_sharing()

        #終了時刻にかつ直前にミーティングを終了していないならミーティングを終了する
        if end_date == now_date and zoom_flag == False:
            zoom_flag = True
            oz.Stop_Zoom()
            print('{} Quit meeting'.format(now_date))
            #ミーティング終了後、即座に予定を再取得する
            count = -1
            continue
        
        #カウンタを増やす
        count += 1

    else:
        continue
            
window.close()