# 外観
![RPA](https://ateruimashin.com/diary/wp-content/uploads/2021/04/34c62f94b172c84db0f7e4c8cfb1c9b5.png)

# 開発目的
研究室のオンラインミーティングを自動で開始/終了させることで、私が寝坊しても研究室メンバーに迷惑を掛けないため。

# 環境
- OS: Windows10 Pro
- Python: Python 3.9.1 64-bit

# 使用モジュール
- PyAutoGUI: 0.9.52
- PySimpleGUI: 4.38.0

# このツールでできること
指定のGoogleカレンダーの予定を取得し、開始時刻になったらミーティングを自動で開始し、終了時刻になったらミーティングを自動で終了する。

# 更新履歴
## 2021/02/03
新規: Google Calendar APIを用いて予定を取得できるようにした 
https://ateruimashin.com/diary/2021/02/google-calender-api/

## 2021/02/22
新規: PyAutoGUIでZoomミーティングの開催を自動化した 
https://ateruimashin.com/diary/2021/02/pyautogui-zoom/

## 2021/03/31
新規: PySimpleGUIを用いてGUIを作成した 
https://ateruimashin.com/diary/2021/03/pysimplegui-gui/

## 2021/04/07
完成: 予定取得、Zoom操作をモジュール化し、GUIから操作できるようにした 
https://ateruimashin.com/diary/2021/04/auto-zoom-meeting/

## 2021/04/11
追加: ミーティングを終了させる機能を追加 
修正: 
- 時計の表示を秒単位に変更
- ミーティング開始、終了時のログ出力の順序を変更
- 重複してミーティングが開かないための措置
- ミーティングを終了時に次の予定を取得するように変更
- Stopした後Startすると予定を取得するように変更
https://ateruimashin.com/diary/2021/04/rpa-add-function/

# 予定
時計部分の表示がZoom操作時に停止するため、並列処理で常に動かせるようにする。

# 希望
画像認識がとても遅いので、画像認識を高速化させる。 
やる気が残っているならば、私の修論のテーマにする。