playCount = 0
FIELD = 8
cells = [[0 for i in range(FIELD)]for j in range(FIELD)]
black = 0
white = 0


log=[]

def setup():
    size(480, 480)
    strokeWeight(5)
    cells[3][3] = 1
    cells[3][4] = 2
    cells[4][3] = 2
    cells[4][4] = 1


def draw():
    
    global playCount
    black = 0
    white = 0
    
    background(0, 100, 0)
    stroke(0)
    noFill()
    rect(0, 0, 480, 480)
    
   
    for i in range(1, 9):
        line(i * 60, 0, i * 60, height)
        line(0, i * 60, width - 160, i * 60)

    for i in range(FIELD):
        for j in range(FIELD):
            if cells[i][j] == 1:
                fill(0)
                stroke(0)
                ellipse(i * 60 + 30, j * 60 + 30, 60, 60)
            elif cells[i][j] == 2:
                fill(255)
                stroke(0)
                ellipse(i * 60 + 30, j * 60 + 30, 60, 60)
            else:
                fill(0, 100, 0)
                stroke(0)
                rect(i * 60, j * 60, 60, 60)
            if canPut(i, j):
                
                fill(0, 255, 0)
                stroke(0)
                rect(i * 60, j * 60, 60, 60)
                
            if playCount!=0:
                noFill();
                stroke(255,0,0)
                rect(log[playCount-1][0]*60,log[playCount-1][1]*60,60,60)
    

    
    judgeGame()

def judgeGame():
    if playCount == 60:
        if black > white:
            print "Black WIN"
        elif white > black:
            print "White WIN"
        else:
            print "DRAW"


def countStone():
    global black
    global white
    black=0
    white=0
    for i in range(FIELD):
        for j in range(FIELD):
            if cells[i][j] == 1:
                black += 1
            if cells[i][j] == 2:
                white += 1
    print "black "+str(black)
    print "white "+str(white)


def mousePressed():
    global playCount

    if mouseX <= 480:
        for i in range(FIELD):
            for j in range(FIELD):
                if mouseX >= i * 60 and mouseX < (i + 1) * 60:
                    if mouseY >= j * 60 and mouseY < (j + 1) * 60:
                        if canPut(i, j):

                            putStone(i, j)
                            reverseStone(i, j)
                            log.append((i,j))

                            playCount += 1


def putStone(_posX, _posY):

    if playCount % 2 == 0:
        cells[_posX][_posY] = 1
    else:
        cells[_posX][_posY] = 2


def reverseStone(_posX, _posY):

    if canPutStone(_posX, _posY, -1, -1):
        reverse(_posX, _posY, -1, -1)
    if canPutStone(_posX, _posY, 0, -1):
        reverse(_posX, _posY, 0, -1)
    if canPutStone(_posX, _posY, 1, -1):
        reverse(_posX, _posY, 1, -1)
    if canPutStone(_posX, _posY, -1, 0):
        reverse(_posX, _posY, -1, 0)
    if canPutStone(_posX, _posY, 1, 0):
        reverse(_posX, _posY, 1, 0)
    if canPutStone(_posX, _posY, -1, 1):
        reverse(_posX, _posY, -1, 1)
    if canPutStone(_posX, _posY, 0, 1):
        reverse(_posX, _posY, 0, 1)
    if canPutStone(_posX, _posY, 1, 1):
        reverse(_posX, _posY, 1, 1)

def reverse(_posX, _posY, _vecX, _vecY):
    
    global playCount
    putStone = 0
    
    if playCount % 2 == 0:
        putStone = 1
    else:
        putStone = 2

    _posX += _vecX
    _posY += _vecY

    while(cells[_posX][_posY] != putStone):

        cells[_posX][_posY] = putStone
        _posX += _vecX
        _posY += _vecY


def canPutStone(_posX, _posY, _vecX, _vecY):
    putStone = 0
    global playCount
    if playCount % 2 == 0:
        putStone = 1
    else:
        putStone = 2

    _posX += _vecX
    _posY += _vecY

    if _posX < 0 or _posX > FIELD - 1 or _posY < 0 or _posY > FIELD - 1:
        return False
    if cells[_posX][_posY] == putStone:
        return False
    if cells[_posX][_posY] == 0:
        return False

    _posX += _vecX
    _posY += _vecY

    while (_posX >= 0 and _posX < FIELD and _posY >= 0 and _posY < FIELD):

        if cells[_posX][_posY] == 0:
            return False
        if cells[_posX][_posY] == putStone:
            return True
        _posX += _vecX
        _posY += _vecY

def canPut(_posX, _posY):
    if _posX >= FIELD or _posY >= FIELD:
        return False
    if cells[_posX][_posY] != 0:
        return False

    if canPutStone(_posX, _posY, -1, -1):
        return True
    if canPutStone(_posX, _posY, 0, -1):
        return True
    if canPutStone(_posX, _posY, 1, -1):
        return True
    if canPutStone(_posX, _posY, -1, 0):
        return True
    if canPutStone(_posX, _posY, 1, 0):
        return True
    if canPutStone(_posX, _posY, -1, 1):
        return True
    if canPutStone(_posX, _posY, 0, 1):
        return True
    if canPutStone(_posX, _posY, 1, 1):
        return True

