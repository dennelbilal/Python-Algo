xBall = 0
yBall = 0

xRack = 0
yRack = 0

xspdB = 5
yspdB = 2

def setup():
    global xBall, yBall, xRack, yRack
    size(800,800)
    clear()
    frameRate(60)
    
    xBall = width / 2
    yBall = height / 2

    xRack = width / 2
    yRack = height - 40
    
def draw():
    clear()
    #fill(random(255), random(255), random(255))
    fill(255)
    #e1 = ellipse(random(width) + sin(millis() * 0.001) * 100, 0 + tan(millis() * 0.002) * 100, 40, 40)
    drawRacket()
    drawBall()
    coll()

def drawRacket():
    global xRack, yRack
    barre = rect(xRack, yRack, 200, 20, 10)
    
    xRack = mouseX - 100
    
def drawBall():
    global xBall, yBall, xspdB, yspdB
    balle = circle(xBall, yBall, 40)
    
    xBall += xspdB
    yBall += yspdB
    
def coll():
    global xBall, yBall, xRack, yRack, xspdB, yspdB
    
    if xBall + 20 == width or xBall + 20 == 0:
        xspdB *= -1
    elif yBall + 10 == 0:
        yspdB *= -1
    elif xBall + 10 == xRack or yBall + 10 == yRack:
        xspdB *= -1
        yspdB *= -1
        
    
    
