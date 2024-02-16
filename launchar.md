```python
from tkinter import Tk, Button
import subprocess 

# tkinterを用いたランチャーアプリの作成
# アプリケーションを開いた時の動作
def open_application(path):
    subprocess.Popen(path)  # 指定されたパスのアプリを開く
    root.destroy()          # アプリケーションを開いたときにアプリを終了する

# メインウィンドウ(root)の設定
root = Tk()                 # tkinterでウィンドウの作成
root.title("Launcher")      # タイトル名
root.geometry("300x150")    # windowサイズ

# ショートカット設定　変更する場合　ボタン名＋パスで変更可
shortcut = {
    "GoogleCrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "メモ帳": "C:\\Windows\\notepad.exe",
    "コマンドプロンプト": "C:\\WINDOWS\\system32\\conhost.exe",
    "コントロールパネル": "C:\\WINDOWS\\system32\\control.exe",
    "エクスプローラー": "C:\\Windows\\explorer.exe",
    "vscode": "C:\\Users\\7d03\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}
# ボタン 初期配置   
row = 1 # 行
col = 0 # 列

# shortcutに入っている各項目についてnameを取り出して繰り返す
for name, path in shortcut.items(): 
    # lambdaに7行目のopen_application関数を代入
    btn = Button(root, text=name, command=lambda p=path: open_application(p))   
    # 指定位置にボタンを配置
    btn.grid(column=col, row=row, sticky="NSEW") 
    # ３行の表示なので３行目以上になった場合次の２列目に移行
    col += 1        
    if col > 2:     # もし3列より大きいなら
        col = 0     # カラム位置の初期配置に
        row += 1    # +1して2列目に移行

# 各ボタンがwindowサイズに応じて形状変化するように設定
root.grid_columnconfigure(0, weight=1)  
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

# 勝手に終了しないようにループさせる
root.mainloop()

コード解説

from tkinter import Tk, Button: tkinterモジュールからTkクラスとButtonクラスをインポートします。
import subprocess: サブプロセスを実行するためのモジュールをインポートします。

def open_application(path):: open_application関数を定義します。この関数は、指定されたパスのアプリを開くために使用されます。
subprocess.Popen(path): subprocessモジュールを使用して、指定されたパスのアプリを開きます。
root.destroy(): アプリケーションを開いたときにアプリを終了します。

root = Tk(): Tkクラスのインスタンスを作成し、メインウィンドウを定義します。
root.title("Launcher"): ウィンドウのタイトルを設定します。
root.geometry("300x150"): ウィンドウのサイズを設定します。

shortcut = { ... }: ショートカットの名前とパスを辞書として定義します。

for name, path in shortcut.items():: shortcut辞書の各要素について、名前とパスを取得します。
btn = Button(root, text=name, command=lambda p=path: open_application(p)): 
各アプリのショートカットのボタンを作成し、クリックされたときに対応するアプリを開くように設定します。
btn.grid(column=col, row=row, sticky="NSEW"): グリッドレイアウトを使用してボタンを指定位置に配置します。
root.grid_columnconfigure(0, weight=1): 
ウィンドウの列のサイズが変更されたときにウィジェットがウィンドウに対してどのように拡大/縮小されるかを設定します。

root.grid_rowconfigure(1, weight=1): 
ウィンドウの行のサイズが変更されたときにウィジェットがウィンドウに対してどのように拡大/縮小されるかを設定します。

root.mainloop(): イベントループを開始し、ウィンドウを表示します。




