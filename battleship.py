"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["no.of rows"] = 10 
    data["no.of cols"] = 10
    data["board size"] = 500
    data["cell size"] = data["board size"]/data["no.of rows"]
    data["numShips"]=5
    data["no.of boards"] = 2
    data["temporary"] = test.testShip()
    data["computer"] = emptyGrid(data["no.of rows"],data["no.of cols"])
    data["user"] = emptyGrid(data["no.of rows"],data["no.of cols"])
    data["computer"] = addShips(data["computer"], data["numShips"])
    return None


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data,userCanvas,data["user"],True)
    drawShip(data,userCanvas,data["temporary"])
    drawGrid(data,compCanvas,data["computer"],True)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    outer_list = []
    for i in range(rows):
        inner_list =[]
        for j in range(cols):
            inner_list.append(1)
        outer_list.append(inner_list)

    return outer_list


'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    ship = []
    row = random.randint(1,8)
    col = random.randint(1,8)
    axes = random.randint(0,1)
    if axes == 0:
        for i in range(row-1,row+2):
            ship.append([i,col])
    else:
        for i in range(col-1,col+2):
            ship.append([row,i])     
    return ship


'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    
    for row in range(len(ship)):
        x = ship[row][0]
        y = ship[row][1]
        if grid[x][y] != EMPTY_UNCLICKED:
            return False


    return True


'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count = 0
    while count < numShips:
        ship = createShip()
        if checkShip(grid,ship):
            for row in range(len(ship)):
                x = ship[row][0]
                y = ship[row][1]
                grid[x][y] = 2
            count += 1


    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for row in range(data["no.of rows"]):
        for col in range(data["no.of cols"]):
            x1 = row * data["cell size"]
            y1 = col * data["cell size"]
            x2 = data["cell size"] + x1
            y2 = data["cell size"] + y1 
            #canvas.create_rectangle(x1, y1, x2, y2)
            if grid[row][col] == SHIP_UNCLICKED:
                canvas.create_rectangle(x1,y1,x2,y2,fill = "yellow")
            else:
                canvas.create_rectangle(x1,y1,x2,y2,fill = "blue")
    return None


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    ship.sort()
    if ship[0][1] == ship[1][1] == ship[2][1]:
        if ship[0][0]+1 == ship[1][0] == ship[2][0]-1:
            return True

                   
    return False


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    ship.sort()
    if ship[0][0] == ship[1][0] == ship[2][0]:
        if ship[0][1]+1 == ship[1][1] == ship[2][1] - 1:
            return True
    return False


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    row = int(event.x/data["cell size"])
    col = int(event.y/data["cell size"])
    l = []
    l.append(col)
    l.append(row)
    return l


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in ship:
        x1 = i[0]*data["cell size"]
        y1 = i[1]*data["cell size"]
        x2 = data["cell size"] + x1
        y2 = data["cell size"] + y1
        canvas.create_rectangle(x1,y1,x2,y2,fill = "white")
    return None


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship) == 3 and checkShip(grid, ship) and isVertical(ship) or isHorizontal(ship):
        return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    return


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    return


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    return


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    # test.testEmptyGrid()
    # test.testCreateShip()
    # test.testCheckShip()
    # test.testAddShips()
    # test.testMakeModel()
    #test.testDrawGrid()
    #test.testIsVertical()
    #test.testIsHorizontal()
    #test.testGetClickedCell()
    #test.testDrawShip()
    test.testShipIsValid()
    ## Finally, run the simulation to test it manually ##
    #runSimulation(500, 500)
