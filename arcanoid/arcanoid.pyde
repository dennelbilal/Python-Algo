ballX = 0
ballY = 0

speedx = 5
speedy = 5
ballRadius = 5

racketwidth = 125
racketheight = 20
racketx = 0
rackety = 0

def setup():
    global ballX, ballY, racketx, rackety, racketwidth, racketheigth
    ballX = width/2
    size(379, 508)
    frameRate(60)
    ballX = width/2
    ballY = height/2
    racketx = mouseX - (racketwidth/2)
    rackety = height -25

def draw():
    clear()
    drawRacket()
    drawBall()
    
def drawRacket():
    global racketwidth, racketx, rackety
    fill(255, 255, 255)
    racketx = mouseX - (racketwidth/2)
    rect(racketx, rackety, racketwidth, 10, 5)
    


    
    
def drawBall():
    global ballX, ballY, speedx, speedy, ballRadius, racketwidth, racketheight
    global racketwidth, racketx, rackety
    ballX = ballX + speedx
    ballY = ballY + speedy
    #ballX += speedx
    #ballY += speedy
    
    #droit et gauche
    if(ballX + ballRadius > width): 
        speedx *= -1 
        ballX = width - ballRadius
    elif(ballX - ballRadius < 0): 
         speedx *= -1
         ballX= ballRadius
         
    #bas et haut     
    if(ballY +ballRadius > height):
        speedy *= -1
        ballY = height - ballRadius
        racketwidth = racketwidth * 0.9
    elif(ballY - ballRadius < 0):
        speedy *= -1
        ballY = ballRadius
        
    if(rackety < ballY+ballRadius < rackety + racketheight and ballY > 0):
        if(racketx < ballX < racketx + racketwidth):
            speedy *= -1
            ballY = rackety - ballRadius

    circle(ballX, ballY, 10);
    
    
        


    
