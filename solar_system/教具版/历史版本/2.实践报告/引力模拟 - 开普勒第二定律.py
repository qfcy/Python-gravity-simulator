import math
from turtle import *

G = 50 # 引力常量
d_t = 0.00001 # 一轮计算经过的"时间", 经测试说明越小越精确
speed = 300 # 刷新一次屏幕之前执行计算的次数, 越大越快
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

def clear_screen(x,y): # 清除行星轨迹
    for p in lst:
        p.clear()

scr=Screen()
scr.title("Python 天体引力模拟的探索")
scr.bgcolor("black")
scr.tracer(0,0)
scr.onclick(clear_screen) #点击屏幕清屏

sun = Sun(1e6, (0,0), (0,0))
sun.penup()
sun.color("yellow")
sun.shapesize(2)

p = Star(1e4, (260,0), (0,300))
p.color("blue")
p.shapesize(0.7)

t = 0 # 程序运行的总"时间"
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
    # 刷新行星
    for p in lst:
        p.update()
    update()

    # 累加轨道扫过的图形面积
    # 算出3条边
    a = math.hypot(p.x-prev_x, p.y-prev_y)
    b = math.hypot(p.x, p.y)
    c = math.hypot(prev_x, prev_y)
    S += calc_square(a,b,c)
    print("时间:%.4f"%t, "行星扫过面积:%.4f"%S,
          "行星扫过面积÷时间 = %.4f"%(S/t))# 如果行星扫过面积÷时间 是一个定值, 则验证通过
    prev_x, prev_y = p.x,p.y