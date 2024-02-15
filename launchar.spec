# Launcherアプリケーション

これはPythonのTkinterを使用して作成されたランチャーアプリケーションです。

## 使い方

- アプリケーションを実行すると、さまざまなアプリケーションを起動するためのボタンが表示されます。
- ボタンをクリックすると、対応するアプリケーションが開きます。
- ウィンドウサイズに応じてボタンのサイズが調整されます。

## コード

```python
from tkinter import Tk, Button
import subprocess 

# アプリケーションを開く関数
def open_application(path):
    subprocess.Popen(path)  # 指定されたアプリケーションパスを開く
    root.destroy()          # アプリを開いた後、アプリケーションを終了する

root = Tk()
root.title("Launcher")      # ウィンドウタイトルの設定
root.geometry("300x150")    # ウィンドウサイズの設定

# ショートカットの設定
shortcut = {
    "Google Chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "メモ帳": "C:\\Windows\\notepad.exe",
    "コマンドプロンプト": "C:\\WINDOWS\\system32\\conhost.exe",
    "コントロールパネル": "C:\\WINDOWS\\system32\\control.exe",
    "エクスプローラー": "C:\\Windows\\explorer.exe",
    "VSCode": "C:\\Users\\7d03\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}

# ボタンの配置    
row = 1 # 行
col = 0 # 列
for name, path in shortcut.items():
    btn = Button(root, text=name, command=lambda p=path: open_application(p))
    btn.grid(column=col, row=row, sticky="NSEW")    # ボタンの配置
    col += 1        
    if col > 2:
        col = 0
        row += 1

# ウィンドウサイズに応じてボタンの形状を調整する
root.grid_columnconfigure(0, weight=1)  
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop() # ウィンドウを開いたままにする
