import tkinter as tk
from tkinter import messagebox
def show_popup():
    messagebox.showinfo("提示", "你的桌面被占领了！")
root = tk.Tk()
root.attributes("-fullscreen", True)
root.attributes("-alpha", 0.1)
test = tk.Label(root,text="桌面已被占领")
test.pack()
输入框 = tk.Entry(root)
输入框.pack()
if 输入框.get() == "debug:close":
    button = tk.Button(root,text='close',command=root.destroy,width=20(),height=20())
    button.pack()
button = tk.Button(root,command=show_popup,width=root.winfo_screenwidth(),height=root.winfo_screenheight())
button.pack()
root.mainloop()

