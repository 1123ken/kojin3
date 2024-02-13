from datetime import datetime
from tkinter import Tk, Label, E,Button
import subprocess 

#アプリケーションを開いた時の動作　ボタンクリックでアプリ終了
def open_application(path):
    subprocess.Popen(path)
    root.destroy()

root = Tk()
root.title("Launcher")      #タイトル名
root.geometry("400x200")    #windowサイズ

today = datetime.today().date()

#ショートカット設定　変更する場合　ボタン名＋パスで変更可
shortcut = {
    "GoogleCrome":"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "メモ帳":"C:\\Windows\\notepad.exe",
    "コマンドプロンプト": "C:\\WINDOWS\\system32\\conhost.exe",
    "ユーザーフォルダ": "explorer.exe C:\\Users\\7d03",
    "エクスプローラー": "C:\\Windows\\explorer.exe",
    "コントロールパネル":"C:\\WINDOWS\\system32\\control.exe"
}

# ラベル
label = Label(root, text=today)
label.grid(column=0, row=0, sticky=E, columnspan=3)

# ボタン
row = 1
col = 0
for name, path in shortcut.items():
    btn = Button(root, text=name, command=lambda p=path: open_application(p))
    btn.grid(column=col, row=row, sticky="NSEW")
    col += 1
    if col > 2:
        col = 0
        row += 1

#ボタン位置
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.mainloop()