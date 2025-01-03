import math
import tkinter as tk
import tkinter.ttk as ttk
from time import perf_counter,sleep
from turtle import *

G = 50 # 引力常量
d_t = 0.00001 # 一轮计算经过的"时间", 经测试说明越小越精确
speed = 900 # 刷新一次屏幕之前执行计算的次数, 越大越快
FPS=60 # 锁定FPS
lst=[]

class Star(Turtle):
    def __init__(self, mass, position, velocity):
        super().__init__()
        self.shape("circle")
        self.m=mass # 行星质量
        self.x,self.y=position # 行星初始位置
        self.dx,self.dy=velocity # 行星初始速度
        self.ax=self.ay=0  # 行星加速度
        lst.append(self)
        self.penup()
        self.setpos((self.x,self.y))
        self.pendown()
    def gravity(self):
        # 计算行星自身受到的加速度，以及列表中位于自己之后的行星受到自己引力的加速度
        for i in range(lst.index(self)+1, len(lst)):
            p=lst[i] # 另一个行星
            dx=p.x-self.x
            dy=p.y-self.y

            d = math.hypot(dx,dy) # 相当于 (dx**2 + dy**2)再开根号
            f = G * self.m * p.m / d**2
            # 将力正交分解为水平、竖直方向并计算加速度
            self.ax+=f / self.m * dx / d
            self.ay+=f / self.m * dy / d
            p.ax-=f / p.m * dx / d
            p.ay-=f / p.m * dy / d
    def step(self):
        # 计算行星速度、位移
        self.dx += d_t*self.ax
        self.dy += d_t*self.ay

        self.x+= d_t*self.dx
        self.y+= d_t*self.dy
    def update(self):
        self.setpos((self.x,self.y))
    def getOrbitSpeed(self,r):
        # 获取某一半径的圆轨道上天体的速率
        # 引力=向心力=m * v**2 / r
        g = G * self.m / r**2
        return math.sqrt(g * r)

class Sun(Star): # 太阳固定在中心, 继承自Star类
    def gravity(self):
        for i in range(lst.index(self)+1, len(lst)):
            p=lst[i] # 另一个行星
            dx=p.x-self.x
            dy=p.y-self.y

            d = math.hypot(dx,dy)
            f = G * self.m * p.m / d**2
            # 将力正交分解为水平、竖直方向并计算加速度
            p.ax-=f / p.m * dx / d
            p.ay-=f / p.m * dy / d
    def step(self):
        pass

def calc_square(a,b,c): # 根据边长计算三角形面积
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))

def clear_screen(*_): # 清除行星轨迹
    for p in lst:
        p.clear()
    d.clear()

def play():
    global d_t
    d_t=0.00001
    sp["text"]="速度: %.2f" % (d_t*10**6)
def stop():
    global d_t
    d_t=0
    sp["text"]="速度: %.2f" % (d_t*10**6)
def increase_speed():
    global d_t
    d_t*=1.2
    sp["text"]="速度: %.2f" % (d_t*10**6)
def decrease_speed():
    global d_t
    d_t/=1.2
    sp["text"]="速度: %.2f" % (d_t*10**6)

def acc_planet():
    global t,S
    t=1e-10; S=0 # 重置时间和扫过面积
    p.dx*=1.1
    p.dy*=1.1
def slow_planet():
    global t,S
    t=1e-10; S=0 # 重置时间和扫过面积
    p.dx/=1.1
    p.dy/=1.1
def exit():
    win.destroy();scr.bye() # 关闭窗口

# 创建tkinter 界面
win=tk.Tk()
win.title("控制")
win.geometry("295x80")
btns=tk.Frame(win)
btns.pack(side=tk.LEFT)

ttk.Button(btns,text="播放",command=play,width=5).grid(row=0,column=1)
ttk.Button(btns,text="暂停",command=stop,width=5).grid(row=0,column=2)
ttk.Button(btns,text="加快",command=increase_speed,width=5).grid(row=0,column=3)
ttk.Button(btns,text="减慢",command=decrease_speed,width=5).grid(row=0,column=4)
ttk.Button(btns,text="清屏",command=clear_screen,width=5).grid(row=0,column=5)
ttk.Button(btns,text="行星加速",command=acc_planet).grid(row=1,column=1,columnspan=2)
ttk.Button(btns,text="行星减速",command=slow_planet).grid(row=1,column=3,columnspan=2)
ttk.Button(btns,text="退出",command=exit,width=5).grid(row=1,column=5)

labels=tk.Frame(win)
labels.pack(side=tk.RIGHT,expand=True)

fps=tk.Label(labels,text="FPS: 0")
fps.pack(side=tk.TOP)
sp=tk.Label(labels,text="速度: %.2f" % (d_t*10**6))
sp.pack(side=tk.TOP)


scr=Screen()
scr.title("Python 天体引力模拟的探索 - 开普勒第二定律演示")
scr.bgcolor("black")
scr.tracer(0,0)
scr.onclick(clear_screen) #点击屏幕清屏

w=Turtle() # w 用于输出文字
w.penup();w.hideturtle()
w.color("white") # 设置文字颜色为白色
d=Turtle() # d 用于画出行星扫过的部分
d.penup();d.hideturtle()
d.color("gray")
d.begin_fill()


sun = Sun(1e6, (0,0), (0,0))
sun.penup()
sun.color("yellow")
sun.shapesize(2)

p = Star(1e4, (260,0), (0,300))
p.color("blue")
p.shapesize(0.7)

count = 0 # 循环的次数
t = 0 # 程序运行的总"时间"
time=perf_counter() # 用于计算FPS
S = 0 # 累计扫过面积
prev_x, prev_y = 260,0 # 行星的前一个坐标
while True:
    # 计算行星的位置
    for i in range(speed):
        t += d_t
        # 分别计算每个行星受到的加速度
        for p in lst:
            p.gravity()
        # 根据计算的加速度, 求出速度和位移
        for p in lst:
            p.step()
        for p in lst:
            p.ax=p.ay=0 # 重置加速度
    try:
        # 刷新行星
        for p in lst:
            p.update()
        update()
        # 锁定FPS
        sleep(max(1 / FPS - (perf_counter()-time),0))
        fps["text"]='FPS: %d' % int(1 / (perf_counter()-time))

        time=perf_counter()

        # 画出行星与太阳连线扫过的部分
        count += 1
        if count%2==0:
            d.goto(p.x,p.y)
            d.goto(sun.x,sun.y)
            d.end_fill()
            d.begin_fill()
        # 每隔一定时间清除画出图形，并输出文字
        if count%20==0 and d_t!=0: # d_t!=0：未暂停
            clear_screen()
            # 输出文字
            w.clear()
            w.goto(scr.window_width()//2-360,
                 scr.window_height()//2-80)
            w.write("时间间隔:%.4f"%t+"\n行星扫过面积:%.4f"%S + \
              "\n行星扫过面积÷时间 = %.4f"%(S/t) + \
                "\n提示：加速/减速行星，可计算不同轨道下的结果。", font=(None,12)) # 如果行星扫过面积÷时间 是一个定值, 则验证通过
            t=0
            S=0
        d.goto(p.x,p.y)
        # 算出3条边
        a = math.hypot(p.x-prev_x, p.y-prev_y)
        b = math.hypot(p.x, p.y)
        c = math.hypot(prev_x, prev_y)
        S += calc_square(a,b,c) # 累加轨道扫过的图形面积
        
        prev_x, prev_y = p.x,p.y
    except (Terminator,tk.TclError):break # 如果窗口已关闭，忽略错误

