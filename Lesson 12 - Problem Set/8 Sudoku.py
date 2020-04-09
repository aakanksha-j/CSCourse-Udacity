# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

def check_wholeNumbers(inputMatrix):
    wholeNumbers=[1,2,3,4,5,6,7,8,9]
    for i in inputMatrix:
        for j in i:
            if j not in wholeNumbers or j>len(inputMatrix):
                return False
    return True

#def check_square(inputMatrix):
#    elementsList=[]
#    for i in inputMatrix:
#        for j in i:
#            if j not in elementsList:
#                print j
#                elementsList.append(j)
#    return len(elementsList)==len(inputMatrix)

def check_row(inputMatrix):
    for i in inputMatrix:
        j=0
        while j<len(i):
            #print "i[j]:",i[j]
            count =0
            k=j+1
            while k<len(i):
                #print "i[k]:",i[k]
                if i[j]==i[k]:
                    count=count+1
                if count>0:
                    return False
                #print "count:",count
                k=k+1
            j=j+1
    return True

def check_column(inputMatrix):
    l=0
    while l<len(inputMatrix):
        j=0
        while j<len(inputMatrix):
            count=0
            k=j+1
            while k<len(inputMatrix):
                if inputMatrix[j][l]==inputMatrix[k][l]:
                    count=count+1
                if count>0:
                    return False
                k=k+1
            j=j+1
        l=l+1
    return True

def check_sudoku(inputMatrix):
    for i in inputMatrix:
        print i
    return check_wholeNumbers(inputMatrix) and check_row(inputMatrix) and check_column(inputMatrix) #and check_square(inputMatrix)

print "incorrect:",check_sudoku(incorrect)
#>>> False

print "correct:",check_sudoku(correct)
#>>> True

print "incorrect2:",check_sudoku(incorrect2)
#>>> False

print "incorrect3:",check_sudoku(incorrect3)
#>>> False

print "incorrect4:",check_sudoku(incorrect4)
#>>> False

print "incorrect5:",check_sudoku(incorrect5)
#>>> False
