def addSeparator(n):
    for seps in range(n):
        #if not the last separator in the line
        if seps!= n-1:
            #even or odd
            if seps%2 == 0:
                print('--', end = "")
            else:
                print("--", end = "")
        else:
            if seps%2 == 0:
                print('--')
            else:
                print("--")

def myGameBoard (r,c):
    for rows in range(r):
        for columns in range(1,c+1):
        #dont add new line if not last column
            if columns != c:
            #decide how column char to display
                if columns%2 !=0:
                    print(' |', end="")
                else:
                    print(" ", end="")
            #new line if last column
            else:
                #decide how to display column but add new line since last column
                if columns%2 !=0:
                    print(' |')
                else:
                    print(" ")

    #if not last row add separation
    #make sure this lines up
        if rows != r-1:
            addSeparator(c)

#addSeparator(3)
myGameBoard(3,3)
