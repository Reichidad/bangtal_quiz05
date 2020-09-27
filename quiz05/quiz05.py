import random
from bangtal import *
import time


scene1 = Scene("MHW Puzzle", "images/origin.jpg")


exit = Object("images/exit.png")
exit.locate(scene1, 1100, 100)
exit.show()

image1 = "images/output/1.jpg"
image2 = "images/output/2.jpg"
image3 = "images/output/3.jpg"
image4 = "images/output/4.jpg"
image5 = "images/output/5.jpg"
image6 = "images/output/6.jpg"
image7 = "images/output/7.jpg"
image8 = "images/output/8.jpg"
image9 = "images/output/9.jpg"
blank = "images/output/blank.jpg"
blankPosition = None
startTime = None

puzzle = Object("images/puzzle.png")


position1 = (280, 480)
position2 = (520, 480)
position3 = (760, 480)
position4 = (280, 240)
position5 = (520, 240)
position6 = (760, 240)
position7 = (280, 0)
position8 = (520, 0)
position9 = (760, 0)

positions = [position1, position2, position3, position4, position5, position6, position7, position8, position9]
shufflePositions = positions.copy()
images = [image1, image2, image3, image4, image5, image6, image7, image8, image9]


piece1 = Object(images[0])
piece2 = Object(images[1])
piece3 = Object(images[2])
piece4 = Object(images[3])
piece5 = Object(images[4])
piece6 = Object(images[5])
piece7 = Object(images[6])
piece8 = Object(images[7])
piece9 = Object(images[8])


pieces = [piece1, piece2, piece3, piece4, piece5, piece6, piece7, piece8, piece9]


def setPiecesPosition(positions) :
    pieces[0].locate(scene1, positions[0][0], positions[0][1])
    pieces[1].locate(scene1, positions[1][0], positions[1][1])
    pieces[2].locate(scene1, positions[2][0], positions[2][1])
    pieces[3].locate(scene1, positions[3][0], positions[3][1])
    pieces[4].locate(scene1, positions[4][0], positions[4][1])
    pieces[5].locate(scene1, positions[5][0], positions[5][1])
    pieces[6].locate(scene1, positions[6][0], positions[6][1])
    pieces[7].locate(scene1, positions[7][0], positions[7][1])
    pieces[8].locate(scene1, positions[8][0], positions[8][1])



def showPieces() :
    puzzle.locate(scene1, 280, 0)
    pieces[0].show()
    pieces[1].show()
    pieces[2].show()
    pieces[3].show()
    pieces[4].show()
    pieces[5].show()
    pieces[6].show()
    pieces[7].show()
    pieces[8].show()
    puzzle.show()
    
   
start = Object("images/start.png")
start.locate(scene1, 540, 330)
start.show()


def startShuffles(x, y, action):
    global shufflePositions, blankPosition, positions, startTime
    startTime = time.time()
    start.hide()
    blankTarget = pieces[8]
    blankPosition = 8
    blankTarget.setImage(blank)
    shufflePositions = [position2, position5, position3, position1, position6, position9, position7, position8, position4]
    setPiecesPosition(shufflePositions)
    showPieces()


def endCheck():
    global shufflePositions, positions
    for i in range(9):
        if shufflePositions[i] != positions[i]:
            return False
    return True
    

def movePuzzle(x, y, action):
    x = x + 280
    global blankPosition, startTime, shufflePositions
    position = shufflePositions[blankPosition]

    if position[0] - 240 < x < position[0] and position[1] < y < position[1] + 240:
        swapPosition = shufflePositions.index((position[0] - 240, position[1]))
        shufflePositions[blankPosition], shufflePositions[swapPosition] = shufflePositions[swapPosition], shufflePositions[blankPosition]

    elif position[0] + 240 < x < position[0] + 480 and position[1] < y < position[1] + 240:
        swapPosition = shufflePositions.index((position[0] + 240, position[1]))
        shufflePositions[blankPosition], shufflePositions[swapPosition] = shufflePositions[swapPosition], shufflePositions[blankPosition]

    elif position[0] < x < position[0] + 240 and position[1] - 240< y < position[1]:
        swapPosition = shufflePositions.index((position[0], position[1] - 240))
        shufflePositions[blankPosition], shufflePositions[swapPosition] = shufflePositions[swapPosition], shufflePositions[blankPosition]

    elif position[0] < x < position[0] + 240 and position[1] +240 < y < position[1] + 480:
        swapPosition = shufflePositions.index((position[0], position[1] + 240))
        shufflePositions[blankPosition], shufflePositions[swapPosition] = shufflePositions[swapPosition], shufflePositions[blankPosition]

    else:
        return None

    setPiecesPosition(shufflePositions)
    showPieces()

    if endCheck() is True:
        endTime = time.time()
        showMessage("걸린 시간은 총 " + str(round(endTime - startTime, 3)) + "초 입니다.")
        puzzle.hide()

def exitGame(x, y, action):
    endGame()


start.onMouseAction = startShuffles
puzzle.onMouseAction = movePuzzle
exit.onMouseAction = exitGame

startGame(scene1)







