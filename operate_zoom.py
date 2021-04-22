import pyautogui as pg
import sys
import os

#画像認識をしてクリックする
def sarch_click(button):
    #マウスポインタがボタン上にあると正しく認識しないことを防ぐ
    #ボタンが存在することのない場所へマウスポインタを移動させる
    pg.moveTo(pg.size())

    #ボタンの位置の座標を取得
    button_loc = pg.locateOnScreen(button)
    #ボタンが見つかったかどうかで分岐
    if button_loc is None:
        #ボタンが見つからなかった時、エラーメッセージを出す
        print('It can not find {} button'.format(button))
    else:
        button_x, button_y = pg.center(button_loc)
        pg.click(button_x, button_y)

# ズーム起動部分(windows専用)
def run_zoom():
    pg.press('win')
    pg.PAUSE = 1
    pg.write('zoom')
    pg.PAUSE = 2
    pg.press('enter')

# 定期ミーティング起動部分
def start_meeting():

    # ボタンがアクティブ\非アクティブ状態両方のスクリーンショットをそれぞれリストに入れる。スタートは変数で持つ。
    buttton_active = [r'button\active\zoom_meeting_active.PNG',
                      r'button\active\zoom_igrashi_meeting_active.PNG']
    button_nonactive = [r'button\nonactive\zoom_meeting_non.PNG',
                        r'button\nonactive\zoom_igarashi_meeting_non.PNG']
    button_start = r'button\active\zoom_igarashi-meeting_start.PNG'

    # 画像認識部分
    for button_a, button_n in zip(buttton_active, button_nonactive):

        # 非アクティブ時のボタンを探す
        button_loc_n = pg.locateOnScreen(button_n)

        if button_loc_n is None:
            # 非アクティブ時のボタンが見つからない場合、アクティブ時のボタンを探す
            button_loc_a = pg.locateOnScreen(button_a)

            if button_loc_a is None:
                # ボタンが見つからないならばプログラムを終了する
                print('It can not find meeting button')
                sys.exit()
            else:
                # ボタンがアクティブならば操作は必要ない
                continue

        # 公式ドキュメントのサンプルコードを参考に実装
        # ボタンの中心の位置の座標を取得しクリックする
        button_center = pg.center(button_loc_n)
        button_x, button_y = button_center
        pg.click(button_x, button_y)

        # 画面遷移のために1秒停止する
        pg.PAUSE = 1

    # ミーティング開始ボタンを押す部分
    #開始ボタンを探す
    button_start = pg.locateOnScreen(button_start)
    #ボタンが見つからない場合
    sarch_click(button_start)

def Stop():
    #ミーティング終了するときに押すボタン
    button_quit = r'button\active\zoom_meeting_quit.PNG'

    #終了ボタンを押す(ショートカットキーで代用)
    pg.hotkey('alt', 'q')

    #画面遷移のために1秒停止する
    pg.PAUSE = 1

    #全員に対してミーティングを終了する
    sarch_click(button_quit)

def close_audio_window():
    #コンピュータオーディオのウィンドウが邪魔なので消す
    pg.hotkey('alt', 'f4')

#ゼミ開始時、画面共有しておく
def sharing():
    #画面共有を開始する
    pg.hotkey('alt', 's')

    #1秒待機
    pg.PAUSE = 1

    #パワーポイントのアイコン
    button_pp = r'button\active\button_powerpoint.PNG'

    #パワーポイントを選択する
    sarch_click(button_pp)

    #共有を開始する
    pg.press('enter')


#ミーティング開始時
def Start_Zoom():
    try:
        run_zoom()
        pg.PAUSE = 5 #Zoomの起動待ち
        start_meeting()
    except KeyboardInterrupt:
        print('ERROR: It can not start zoom meeting.\n')
        pg.FAILSAFE = True

#ミーティング開始時にパワーポイントを共有する
def screen_sharing():
    #邪魔なウィンドウを消す
    close_audio_window()
    pg.PAUSE = 1
    #画面共有開始
    sharing()

#ミーティング終了時
def Stop_Zoom():
    try:
        Stop()
    except KeyboardInterrupt:
        print('ERROR: It can not quit zoom meeting.\n')
        pg.FAILSAFE = True
