from collections import OrderedDict

board = OrderedDict()

boardWidth = int(input("How wide would you like the board?\n\n"))
boardHeight = int(input("How tall would you like the board?\n\n"))

# Create the board. Board is a dictionary with the number of keys equal to the board width to create columns.
# Board height is a list. Initialized with "0" for empty space. Len(list) == boardHeight
for w in range(1,boardWidth+1):
    board[w] = []
    for h in range(boardHeight):
        board[w].append(" ")


player = 1

# Print the board with vertical line separators. will print row by row, on the last column of each
# row return a new line, else print on the same line.
def printBoard(dict, height, width):
    for i in range(height):
        for keys in dict:
            if keys != width:
                print(dict[keys][i] + "|", end = "")
            else:
                print(dict[keys][i] + "|")
    print("\n")

# find the last position of a empty space in the board (for a column selected).
# Empty spaces are denoted by a "0" in the column list (i.e. value for that key in the dictionary)
def findLastPosition(p):
    for i in range(len(p)):
        if p[i] == " ":
            index = i
    return index

# Check the columns for winner. The input p should be the column where the player placed their piece.
# Returns true when 4 in a row is found. Last posible start for 4 in a row is the index 3 of the list.
# Therefore, the range is from the length of the list to index 3 decreasing by 1. len(p)-1 accounts for
# the 0th index of a list. Stop position of 2 accounts for up to but not past index 3.
def checkColumn(p):
    for i in range(len(p)-1,2,-1):
        if p[i] == p[i-1] and p[i-1] == p[i-2] and p[i-2] == p[i-3]:
            print("WINNER FOUND!!!\n\n")
            return True
        break

# Check the rows for a winner. A row is the same index of each key in the dictionary. The first step is to create a
# blank list of all the dict[key][index] for which you want to check. The index input into the function is the
# last position where are piece was placed. Returns True when a winner is found.
def checkRows(dict, index):
    rowList = []
    for keys in dict:
        rowList.append(dict[keys][index])
    for i in range(len(rowList)-3):
        if rowList[i] != " ":
            if rowList[i]== rowList[i+1] and rowList[i+1]== rowList[i+2] and rowList[i+2] == rowList[i+3]:
                print("WINNER FOUND!!!\n\n")
                return True

# Check for positive sloping Diagonal winners. Positive slopes must start by the 4th to last column.
# i.e for 8 columns would have to start from the 5th column. There for the range is number of columns -2
# which for this example would be up to but not including the 6th column. input will come from the user at
# the beginning of the program. input numRows accounts for the number of rows to check. Stop at the 3rd index.
# Subtract 1 in the for loop in range for number of rows to account for the 0th index. Returns true when
# a winner is found.
def checkPosDiags(dict, numColumns, numRows):
    for key in range(1, numColumns -2):
        for index in range(numRows -1, 2, -1):
            if dict[key][index] != " ":
                if dict[key][index] == dict[key+1][index-1] and dict[key+1][index-1] == dict[key+2][index-2] and dict[key+2][index-2] == dict[key+3][index-3]:
                    print("WINNER FOUND!!!\n\n")
                    return True

# Check for negative sloping winners. Logic is the same for positive sloping winners but reversed.
def checkNegDiags(dict, numColumns, numRows):
    for key in range(1, numColumns -2):
        for index in range(numRows - 3):
            if dict[key][index] != " ":
                if dict[key][index] == dict[key+1][index+1] and dict[key+1][index+1] == dict[key+2][index+2] and dict[key+2][index+2] == dict[key+3][index+3]:
                    print("WINNER FOUND!!!\n\n")
                    return True

print("Welcome to Connect-4 by Python, here is your battle field\n\n")
printBoard(board, boardHeight, boardWidth)

while True:
    print("Players turn:", player)
    move = int(input("Which column would you like to place your piece in?\n\n"))
    placement = findLastPosition(board[move])
    print("\n")
    if player == 1:
        board[move][placement] = "R"
        madeMove = 1
        player = 2
    else:
        board[move][placement] = "B"
        madeMove = 2
        player = 1
    printBoard(board, boardHeight, boardWidth)
    if checkColumn(board[move]) or checkRows(board, placement) or checkPosDiags(board, boardWidth, boardHeight) or checkNegDiags(board, boardWidth, boardHeight):
        print("Player", madeMove, "you win!!!")
        break
