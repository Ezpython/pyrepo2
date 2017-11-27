import random
x = 0
y = 0
speed = 10
def setup ():
 size(400,400)
def draw():
    global x 
    global speed
    a = color(255,215,0)
    to = color(128,0,128)
    c = lerpColor(a, to, 0.5)
    background(c)
    fill(0,0,190)
    rect(0,300,500,200)
    fill(75)
    triangle(-50, 300, 50, 150, 200, 300) 
 