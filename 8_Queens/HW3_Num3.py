#   8-Queens Problem
#
#   Michael Brewer
#   Csci 169
#   5 October 2016

#
#   GLOBAL VARIABLES.
#

rows = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]

backtrack_row = 0
current_row = 0
spots_tried = [0, 0, 0, 0, 0, 0, 0, 0]
backtrack_check = False


#
#   PRIMARY CLASS.
#

class Queen:
    global spots_tried
    
    #
    #   CHECKS VERTICALLY FOR HITS.
    #
    
    def checkVert(self, y, x):
        r_temp = y
        c_temp = x
        flag = 0

        if(c_temp == 8):
            c_temp = 0

        for i in range(y, (-1), (-1)):
            if(rows[i][c_temp] == 1):
                flag = 1
                return(flag)
        return(0)

    #
    #   STARTS AT THE DESIRED POINT, CHECKS DIAGONALLY AGAINST ALREADY
    #   PLACED QUEENS.
    #
    
    def checkDiagonal(self, y, x):
        flag = 0

        for i in range(0, 8):
            if((y - i) >= 0):
                if((x + i) <= 7):
                    if(rows[y - i][x + i] == 1):
                        flag = 1
                        return(flag)
                if((x - i) >= 0):
                    if(rows[y - i][x - i] == 1):
                        flag = 1
                        return(flag)
        return(0)

    #
    #   CALLS THE CHECK FUNCTIONS, IF NO HITS PLACES A QUEEN IN THE
    #   DESIRED SPOT. RETURNS FLAG = NUMBER OF HITS FROM CHECK FUNCTIONS
    #
    
    def placeQueen(self, y, x):
        flag = 0
        flag = flag + self.checkVert(y, x)
        flag = flag + self.checkDiagonal(y, x)
        if(flag == 0):
            rows[y][x] = 1
            return(0)
        else:
            return(flag)

#
#   FUNCTION TAKES IN ROW NUMBER TO STEP BACK TO. SPOTS_TRIED[] DEALS WITH
#   THE NUMBER OF SPOTS TRIED FOR EACH QUEEN OVER EACH ITERATION. IF ALL THE SPOTS
#   IN A ROW ARE TRIED, THE FUNCTION CALLS ITSELF RECURSIVELY TO GO BACK ANOTHER
#   LEVEL. BACKTRACK_CHECK IS USED TO STOP THE RECURSION WHEN A NEW VALID SPOT
#   IS FOUND.
#

def backtrack(q, y):
    global rows
    global backtrack_row
    global backtrack_check
    global current_row
    global spots_tried

    if(backtrack_check == True):
        return

    if(backtrack_row <= 0):
        backtrack_row = y
        
    rows[y] = [0, 0, 0, 0, 0, 0, 0, 0]   
    x = spots_tried[y] + 1

    if(x == 8):
        backtrack_row = backtrack_row - 1
        spots_tried[y] = 0
        backtrack(q, y - 1)
    if(backtrack_check == False):
        while(True):
            spots_tried[y] = x
            if(q.placeQueen(y, x) != 0):
                x = x + 1
                if(x > 7):
                    spots_tried[y] = 0
                    backtrack(q, y - 1)
                    break
            else:
                current_row = y + 1
                backtrack_check = True
                return
        backtrack(q, y - 1)

#
#   FUNCTION PRINTS OUT THE CHESS BOARD
#

def printAll():
    for i in range(7, (-1), (-1)):
        print(i, ": ", end = "")
        for j in range(0, 8):
            print(rows[i][j], end = " ")
        print()
    print()

#
#   MAIN DRIVING FUNCTION FOR THE PROGRAM
#

def main():
    global backtrack_row
    global backtrack_check
    global current_row
    global spots_tried

    q = Queen()
    col = 0

    while(True):
        col = 0
        while(col <= 7):
            if(q.placeQueen(current_row, col) != 0):
                spots_tried[current_row] = spots_tried[current_row] + 1
                col = col + 1
            else:
                current_row = current_row + 1
                break
        if(col > 7):
            col = 0
            if(spots_tried[backtrack_row] >= 8):
                spots_tried[backtrack_row] = 0
                backtrack_row = backtrack_row - 1
            spots_tried[current_row] = 0
            backtrack(q, current_row - 1)
            backtrack_check = False
        if(current_row == 8):
            printAll()
            break
        

    

if __name__ == "__main__":
    main()


