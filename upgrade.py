import tkinter as tk
import os,easygui
window=tk.Tk()
window.geometry('300x500')
window.resizable(False,False)
scorenum=int(open('score.txt',encoding='utf-8',mode='r').read())
planenum=int(open('plane.txt',encoding='utf-8',mode='r').read())
bulletnum=int(open('bullet.txt',encoding='utf-8',mode='r').read())
score=tk.Label(text='金币数量:'+str(scorenum))
score.place(x=0,y=0)
def back():
    choose=easygui.buttonbox('您确定要初始化吗,这将删除你的一切游戏记录',choices=('确定','取消'))
    if choose=='确定':
        scoret=open('score.txt',encoding='utf-8',mode='w+')
        scoret.write('0')
        scoret.flush()
        planet=open('plane.txt',encoding='utf-8',mode='w+')
        planet.write('1')
        planet.flush()
        bullett=open('bullet.txt',encoding='utf-8',mode='w+')
        bullett.write('1')
        bullett.flush()
def up_plane():
    global scorenum
    global planenum
    if scorenum<500:
        easygui.msgbox('您的金币数量不够')
    else:
        if planenum<12:
            scorenum=scorenum-500
            with open('score.txt',encoding='utf-8',mode='w+')as f:
                f.write(str(scorenum))
            planenum=planenum+1
            with open('plane.txt',encoding='utf-8',mode='w+')as f:
                f.write(str(planenum))
        else:
            easygui.msgbox('飞机等级已满')
def up_bullet():
    global scorenum
    global bulletnum
    if scorenum<500:
        easygui.msgbox('您的金币数量不够')
    else:
        scorenum=scorenum-500
        with open('score.txt',encoding='utf-8',mode='w+')as f:
            f.write(str(scorenum))
        bulletnum=bulletnum+1
        with open('speed.txt',encoding='utf-8',mode='w+')as f:
            f.write(str(bulletnum))
def up_bullet_speed():
    global scorenum
    global bulletnum
    if scorenum<500:
        easygui.msgbox('您的金币数量不够')
    else:
        with open('score.txt',encoding='utf-8',mode='w+')as f:
            f.write(str(scorenum))
        speednum=speednum/2
        with open('speed.txt',encoding='utf-8',mode='w+')as f:
            f.write(str(speednum))
if planenum<12:
    plane=tk.Label(text='飞机等级:'+str(planenum))
    plane.place(x=0,y=30)
    b1=tk.Button(window,text='升级飞机',command=up_plane)
    b1.place(x=100,y=30)
else:
    plane=tk.Label(text='飞机等级:12(MAX)')
    plane.place(x=0,y=30)
bullet=tk.Label(text='子弹伤害:'+str(bulletnum))
bullet.place(x=0,y=60)
b2=tk.Button(window,text='增加子弹伤害',command=up_bullet)
b2.place(x=100,y=60)
b3=tk.Button(window,text='恢复初始化',command=back)
b3.place(x=0,y=90)
window.mainloop()