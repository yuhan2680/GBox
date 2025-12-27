import tkinter as tk
from PIL import ImageTk
import os
window=tk.Tk()
window.geometry('300x300')
window.resizable(False,False)
play=ImageTk.PhotoImage(file='images/gbox.png')
playLabel=tk.Label(window,image=play)
playLabel.place(x=0,y=0)
def fightvirus():
    os.system('python fightvirus/main.py')
def music():
    os.system('python AImusic/main.py')
def picture():
    os.system('python picture/picture.py')
#text=tk.Label(text='G-Box')
#text.place(x=130,y=0)
b1=tk.Button(window,text='图片拉伸器',command=picture)
b1.place(x=110,y=200)
b2=tk.Button(window,text='智能点歌机',command=music)
b2.place(x=110,y=230)
b3=tk.Button(window,text='大战病毒小游戏',command=fightvirus)
b3.place(x=100,y=260)
window.mainloop()