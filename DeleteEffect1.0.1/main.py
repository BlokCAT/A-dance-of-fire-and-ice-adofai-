import json , os
import tkinter as tk


from tkinter import messagebox
from tkinter import filedialog
from tkinter import *


cor={
    ', }': '}',
    ',  }': '}',
    ']\n\t"decorations"': '],\n\t"decorations"',
    '],\n}': ']\n}',
    ',,': ',',
    '}\n\t\t{':'},\n\t\t{',
    '},\n\t]':'}\n\t]',
    '\n\\n':'\\n'
}


# 创建主窗口
window = tk.Tk()
window.title("DeleteEffect 1.0.1")
window.iconbitmap('message/HEAD.ico')
window.geometry("600x400")


path = None

def browse_file():
    """当用户点击浏览按钮时，打开文件对话框并设置选择的文件路径到输入框中"""
    global path
    filepath = filedialog.askopenfilename()  # 弹出文件选择对话框
    entry_path.delete(0, tk.END)  # 清除输入框当前内容
    entry_path.insert(0, filepath)  # 将选择的文件路径插入到输入框中
    path = filepath


def login1():
    global path
    if path != None:
        dir_path = os.path.dirname(path)

        new_file_name = os.path.splitext(os.path.basename(path))[0] + "_无特效" + os.path.splitext(path)[1]
        new_path = os.path.join(dir_path, new_file_name)

        with open(path, encoding="utf-8-sig") as f:
            info = f.read()
            for i in cor: info = info.replace(i, cor[i])
            contents = json.loads(info)

        contents['decorations'] = []

        contents['actions'] = [
            action for action in contents.get("actions", [])
            if action.get("eventType") == "SetSpeed" or action.get("eventType") == "Twirl" or action.get(
                "eventType") == "MoveCamera" or  action.get("eventType") == "FreeRoamRemove" or action.get("eventType") == "Hold"
               or action.get("eventType") == "PositionTrack"
        ]

        with open(new_path, 'w', encoding='utf-8-sig') as file:
            json.dump(contents, file, ensure_ascii=False, indent=4)

        messagebox.showinfo("A dance of fire and ice" , "更改成功！新adofai文件已在原adofai文件同文件夹内生成！")
    else :
        messagebox.showinfo("A dance of fire and ice" , "请选择adofai文件！")


def login2():
    global path
    if path != None:
        dir_path = os.path.dirname(path)
        new_file_name = os.path.splitext(os.path.basename(path))[0] + "_无装饰" + os.path.splitext(path)[1]
        new_path = os.path.join(dir_path, new_file_name)

        with open(path, encoding="utf-8-sig") as f:
            info = f.read()
            for i in cor: info = info.replace(i, cor[i])
            contents = json.loads(info)

        contents['decorations'] = []

        with open(new_path, 'w', encoding='utf-8-sig') as file:
            json.dump(contents, file, ensure_ascii=False, indent=4)

        messagebox.showinfo("A dance of fire and ice" , "更改成功！新adofai文件已在原adofai文件同文件夹内生成！")
    else :
        messagebox.showinfo("A dance of fire and ice" , "请选择adofai文件！")


photo = PhotoImage(file="message/back.png"),
label = Label(window , image=photo , width = 600 , height = 150)
label.pack()

label1 = tk.Label(window,text="选择adofai文件",font=('黑体',12) , fg = 'red')
label1.pack(pady=8)


button = tk.Button(window, text='去特效', font=('黑体', 12 ), width=25, height=1, command=login1 )
button.pack(pady=9)

button2 = tk.Button(window, text='去装饰物', font=('黑体', 12 ), width=25, height=1, command=login2)
button2.pack(pady=9)

center_frame = tk.Frame(window)
center_frame.pack(expand=True, anchor=tk.CENTER)

entry_path = tk.Entry(center_frame, width=30 )
entry_path.pack(side=tk.LEFT, padx=(0, 5))

button_browse = tk.Button(center_frame, text="浏览", command=browse_file )
button_browse.pack(side=tk.LEFT, padx=(5, 0))

window.mainloop()




