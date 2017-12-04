fallingball =PVector(random(400), 0)
fallingball2 = PVector(random(400), 0)
fallingball3 = PVector(random(400), 0)
speed1 = random(10)
speed2 = random(10)
speed3 = random(10)
score = 0 
speedtop = 5

def init():
    global speed1
    global speed2
    global speed3
    global score
    global speedtop
    global fallingball
    fallingball =PVector(random(400), 0)
    fallingball2 = PVector(random(400), 0)
    fallingball3 = PVector(random(400), 0)
    speed1 = random(10)
    speed2 = random(10)
    speed3 = random(10)
    score = 0 
    speedtop = 5

    
    
    

def setup():
    size(400, 500)
    init()
    
def draw():
    global speed1
    global speed2
    global speed3
    global score
    global speedtop
    global fallingball
    global pointdistance
    background(0)
    fallingball.y = fallingball.y + speed1
    fallingball2.y = fallingball2.y + speed2
    fallingball3.y = fallingball3.y + speed3
    speedtop = speedtop + 0.1
    pointdistance = sqrt((mouseX - fallingball.x)**2+(473 - fallingball.y)**2)
    pointdistance2 = sqrt((mouseX - fallingball2.x)**2+(473 - fallingball2.y)**2)
    pointdistance3 = sqrt((mouseX - fallingball3.x)**2+(473 - fallingball3.y)**2)
    if pointdistance < 50:
        score = 0
        speed1 = 0
        speed2 = 0
        speed3 = 0
        fill(255)
        rect(0,0,400,500)
        fill(0,0,255)
        textSize(14)
        text("You lose, move cursor out of ball click to play again", 10,200)
    if pointdistance2 < 50:
        score = 0
        speed1 = 0
        speed2 = 0
        speed3 = 0
        fill(255)
        rect(0,0,400,500)
        textSize(14)
        fill(0,0,255)
        text("You lose, move cursor out of ball click to play again", 10,200)
    if pointdistance3 < 50:
        score = 0
        speed1 = 0
        speed2 = 0
        speed3 = 0
        fill(255)
        rect(0,0,400,500)
        textSize(14)
        fill(0,0,255)
        text("You lose, move cursor out of ball click to play again", 10,200)
    fill(255,255,0)
    if fallingball.y > 550:
        fallingball.y = -100
        fallingball.x = random(400)
        score = score + 1
        speed = random(3,speedtop)
    if fallingball2.y > 550:
        fallingball2.y = -100
        fallingball2.x = random(400)
        score = score + 1
        speed2 = random(3,speedtop)
    if fallingball3.y > 550:
        fallingball3.y = -100
        score = score +1
        speed3 = random(3, speedtop)
        fallingball3.x = random(400)
    ellipse(fallingball.x, fallingball.y, 60, 60)
    ellipse(fallingball2.x, fallingball2.y, 60, 60)
    ellipse(fallingball3.x, fallingball3.y, 60, 60)
    fill(255)
    ellipse(mouseX, 473, 50, 50)
    textSize(32)
    fill(0,0,255)
    text("Score: " + str(score),10,30)
    
def mousePressed():
    init()
        
    
    