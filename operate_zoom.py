import pyautogui as pg
import sys

#フェールセーフショートカットキー
print('Press Ctrl-C to quit.')

#ズーム起動部分(windows専用)
def run_zoom():

    pg.press('win')
    pg.PAUSE = 1
    pg.write('zoom')
    pg.PAUSE = 2
    pg.press('enter')

#定期ミーティング起動部分
def start_meeting():

    #ボタンがアクティブ\非アクティブ状態両方のスクリーンショットをそれぞれリストに入れる。スタートは変数で持つ。
    buttton_active = [r'button\active\zoom_meeting_active.PNG',r'button\active\zoom_igrashi_meeting_active.PNG']
    button_nonactive = [r'button\nonactive\zoom_meeting_non.PNG',r'button\nonactive\zoom_igarashi_meeting_non.PNG']
    button_start = r'button\active\zoom_igarashi-meeting_start.PNG'

    #画像認識部分
    for button_a, button_n in zip(buttton_active, button_nonactive):

        #非アクティブ時のボタンを探す
        button_loc_n = pg.locateOnScreen(button_n)

        if button_loc_n is None:
            #非アクティブ時のボタンが見つからない場合、アクティブ時のボタンを探す
            button_loc_a = pg.locateOnScreen(button_a)

            if button_loc_a is None:
                #ボタンが見つからないならばプログラムを終了する
                sys.exit()
            else:
                #ボタンがアクティブならば操作は必要ない
                continue

        #公式ドキュメントのサンプルコードを参考に実装
        #ボタンの中心の位置の座標を取得しクリックする
        button_center = pg.center(button_loc_n)
        button_x, button_y = button_center
        pg.click(button_x,button_y)

        #画面遷移のために1秒停止する
        pg.PAUSE = 1

    #ミーティング開始ボタンを押す部分    
    button_x, button_y = pg.center(pg.locateOnScreen(button_start))
    pg.click(button_x,button_y)
    
#メイン部分
try:
    while True:
        run_zoom()
        pg.PAUSE = 1
        start_meeting()
        break
except KeyboardInterrupt:
    print('\n')