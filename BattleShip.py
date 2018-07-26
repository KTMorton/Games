from copy import copy, deepcopy
import random
board_width = 10
board_height = 10
restrictedCoordinates = []


class Ship:
    def __init__(self, x, y, length, orientation):
        self.x = y
        self.y = x
        self.length = length
        self.orientation = orientation

    def canShipBePlaced(self, array):
        canBePlaced = True
        testArray = deepcopy(array)
        array = [[0 for x in range(len(array[0]))] for y in range(len(array))]
        if self.orientation == 0:
            if self.length > len(array) - self.x:
                canBePlaced = False
                print(" \n Ship cant be placed there! \n")
                return False
            for i in range(self.length):
                try:
                    array[self.x - 1][(self.y + i) - 1] = 1
                except IndexError:
                    return False

        elif self.orientation == 1:
            if self.length > len(array) - self.y:
                canBePlaced = False
                print(" \n Ship cant be placed there! \n")
                return False
            for i in range(self.length):
                try:
                    array[(self.x + i) - 1][self.y - 1] = 1
                except IndexError:
                    return False
        for row_idx, row in enumerate(testArray):
            for item_idx, item in enumerate(row):
                if testArray[row_idx][item_idx] is 1 and array[row_idx][item_idx] is 1:
                    canBePlaced = False
                    break

        if canBePlaced:
            return canBePlaced
        else:
            return canBePlaced

    def placeShip(self, array):
        canBePlaced = True
        testArray = deepcopy(array)
        array = [[0 for x in range(len(array[0]))] for y in range(len(array))]
        if self.orientation == 0:
            if self.length > len(array) - self.x:
                canBePlaced = False
                print(" \n Ship cant be placed there! \n")
                return testArray
            for i in range(self.length):
                array[self.x-1][(self.y + i)-1] = 1
        elif self.orientation == 1:
            if self.length > len(array) - self.y:
                canBePlaced = False
                print(" \n Ship cant be placed there! \n")
                return testArray
            for i in range(self.length):
               array[(self.x + i)-1][self.y-1] = 1
        for row_idx, row in enumerate(testArray):
            for item_idx, item in enumerate(row):
                if testArray[row_idx][item_idx] is 1 and array[row_idx][item_idx] is 1:
                    canBePlaced = False
                    break

        if canBePlaced:
            for row_idx, row in enumerate(testArray):
                for item_idx, item in enumerate(row):
                    if testArray[row_idx][item_idx] == 1:
                        array[row_idx][item_idx] = 1
            return array
        else:
            print(" \n Ship cant be placed there! \n")
            return testArray





class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def createBoardArray(self):
        boardArray = [[0 for x in range(self.width)] for y in range(self.height)]
        return boardArray

   # def updateBoard(self, array):




    def printBoard(self, array):
        print("\n\n\n\n\n\n\n\n\n")
        for label in range(1,11):
            print(str(label) + "  ", end="", flush=True)
        print("\n")
        for idx, rows in enumerate(array):
            print(rows,"   " + str((idx+1)))



playerBoard = Board(board_width,board_height)
playerBoardArray = playerBoard.createBoardArray()
shipTwoCounter = 0
shipThreeCounter = 0
shipFourCounter = 0
shipFiveCounter = 0
while True:
    shipCoordinate = []
    shipWorks = False
    shipCoordinate = input("Type the coordinates of your first battle ship. (ex. 1,2): ").split(",")
    shipLength = input("How long is this ship (2, 3, 4, or 5): ")
    shipOrientation = input("Type 1 for vertical and 0 for horizontal: ")

    try:
        shipCoordinate = list(map(int, shipCoordinate))
        shipLength = int(shipLength)
        shipOrientation = int(shipOrientation)
        shipWorks = True
    except ValueError:
        shipWorks = False
        print("Something with your input was wrong")

    print(shipCoordinate)
    if len(shipCoordinate) != 2:
        shipWorks = False
    elif shipOrientation > 1 or shipCoordinate[0] > board_width or shipCoordinate[1] > board_height or shipLength > 5 or shipLength < 2:
        shipWorks = False


    if shipWorks:
        if shipLength == 2:
            shipTwoCounter+=1
        elif shipLength == 3:
            shipThreeCounter+=1
        elif shipLength == 4:
            shipFourCounter+=1
        elif shipLength == 5:
            shipFiveCounter+=1

    if shipFiveCounter > 1 or shipFourCounter > 1 or shipThreeCounter > 1 or shipTwoCounter > 1:
        shipWorks = False
    if shipWorks:
        ship = Ship(shipCoordinate[0], shipCoordinate[1], shipLength, shipOrientation)
        playerBoardArray = ship.placeShip(playerBoardArray)
        playerBoard.printBoard(playerBoardArray)
    else:
        print("Something with your input was wrong")

    if shipFiveCounter is 1 and shipFourCounter is 1 and shipThreeCounter is 1 and shipTwoCounter is 1:
        print("all ships placed!")
        break


enemyBoard = Board(board_width,board_height)
enemyBoardArray = enemyBoard.createBoardArray()

for i in range(5,1,-1):
    while True:
        ship = Ship(random.randint(1,10), random.randint(1,10) ,i, random.randint(0,1))
        if ship.canShipBePlaced(enemyBoardArray):
            enemyBoardArray = ship.placeShip(enemyBoardArray)
            break

enemyBoard.printBoard(enemyBoardArray)





