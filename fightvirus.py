#coding:utf-8
import pygame,random,easygui
from pygame.locals import *
import time
import random
import sys
import os
class GameVar():
    def __init__(self):
        self.state="RUNNING"
        self.nowtime=time.time()
        self.viruspasttime=self.nowtime
        self.helppasttime=self.nowtime
        self.virusappendtime=1
        self.virus=[]
        self.virustype=random.randint(1,60)
        self.bullets=[]
        self.bulletpasttime=self.nowtime
        self.plane=int(open('plane.txt',encoding='utf-8',mode='r').read())
gv=GameVar()
#初始化pygame环境
pygame.init ()
#创建一个长宽分别为1300/700窗口
os.environ[ 'SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 25)
canvas = pygame.display.set_mode((1000,600))
canvas.fill((255,255,255))
pygame.key.set_repeat(10,10)
#设置窗口标题
pygame.display.set_caption("大战病毒")
bg=pygame.image.load('images/bg.jpg')
virus1=pygame.image.load('images/virus1.png')
virus2=pygame.image.load('images/virus2.png')
virus3=pygame.image.load('images/virus4.png')
plane=pygame.image.load('images/plane'+str(gv.plane)+'.png')
bullet=pygame.image.load('images/bullet.png')
lose=pygame.image.load('images/lose.png')
class Virus():
    def __init__(self,type,life,speed,width,height,img,score):
        self.type=type
        self.life=life
        self.speed=speed
        self.width=width
        self.height=height
        self.y=-self.height
        self.img=img
        self.x=random.randint(0,1000-self.width)
        self.score=score
    def move(self):
        self.y=self.y+self.speed
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
class Player():
    def __init__(self,x,y,height,width,img,speed,life):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.img=img
        self.speed=speed
        self.life=int(open('plane.txt',encoding='utf-8',mode='r').read())*2
        self.score=int(open('score.txt',encoding='utf-8',mode='r').read())
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def back(self):
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0
        if self.y>600-self.height:
            self.y=600-self.height
        if self.x>1000-self.width:
            self.x=1000-self.width
player=Player(500,300,127,127,plane,5,10)
class Bullet():
    def __init__(self,x,y,img,height,width):
        self.x=x
        self.y=y
        self.img=img
        self.height=height
        self.width=width
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
    def move(self):
        self.y=self.y-15
def virusappend():
    if gv.nowtime-gv.viruspasttime>=0.5:
        if gv.virustype>=1 and gv.virustype<40:
            gv.virus.append(Virus(1,5,5,25,25,virus1,1))
        if gv.virustype>=40 and gv.virustype<55:
            gv.virus.append(Virus(2,10,4,25,25,virus2,2))
        if gv.virustype>=55:
            gv.virus.append(Virus(3,30,3,60,60,virus3,3))
        gv.virustype=random.randint(1,60)
        gv.viruspasttime=gv.nowtime
def bulletsappend():
    if gv.nowtime-gv.bulletpasttime>=0.1:
        gv.bullets.append(Bullet(player.x+55,player.y,bullet,48,17))
        gv.bulletpasttime=gv.nowtime
gv=GameVar()
def handleEvent():  
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit() 
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                player.y=player.y-player.speed
            if event.key==K_DOWN:
                player.y=player.y+player.speed
            if event.key==K_LEFT:
                player.x=player.x-player.speed
            if event.key==K_RIGHT:
                player.x=player.x+player.speed
def Hit():
    for i in gv.virus:
        if player.x+player.width>=i.x and player.x<=i.x+i.width and player.y+player.height>=i.y and player.y<+i.y+i.height:
            try:
                gv.virus.remove(i)
                player.life=player.life-1
                if player.life<=0:
                    gv.state="LOSE"
            except:
                print('')
        for z in gv.bullets:
            if z.x+z.width>=i.x and z.x<=i.x+i.width and z.y+z.height>=i.y and z.y<+i.y+i.height:
                try:
                    #gv.virus.remove(i)
                    i.life=i.life-int(open('bullet.txt',encoding='utf-8',mode='r').read())
                    gv.bullets.remove(z)
                    if i.life<=0:
                        gv.virus.remove(i)
                        player.score=player.score+i.score
                except:
                    print('')
            if z.x<0:
                try:
                    gv.bullets.remove(z)
                except:
                    print('')
        if i.x<0:
            try:
                gv.bullets.remove(i)
            except:
                print('')
def paint():
    canvas.blit(bg,(0,0))
    for i in gv.virus:
        i.paint()
        i.move()
    for y in gv.bullets:
        y.paint()
        y.move()
    player.paint()
    player.back()
def fillText(text, position,size):
    TextFont = pygame.font.Font('font/WRYH.ttf', size)
    newText = TextFont.render(text, True, (255, 255, 255))
    canvas.blit(newText, position)
while True:
    if gv.state=="RUNNING":
        paint()
        virusappend()
        bulletsappend()
        Hit()
        gv.nowtime=time.time()
        fillText('生命:'+str(player.life),(0,0),30)
        fillText('金币:'+str(player.score),(850,0),30)
    else:
        canvas.blit(lose,(0,0))
        fillText('金币:'+str(player.score),(450,500),30)
        with open('score.txt',encoding='utf-8',mode='w+')as f:
            f.write(str(player.score))
    # 监听有没有按下退出按钮
    handleEvent()
    # 更新屏幕内容
    pygame.display.update()
    #延时10毫秒 
    pygame.time.delay(10)