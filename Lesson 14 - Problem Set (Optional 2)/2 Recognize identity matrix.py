# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def is_identity_matrix(inputMatrix):

    #check whether square and unitary
    i=0
    while i<len(inputMatrix):
        j=0
        while j<len(inputMatrix[i]):
            #print 'inputMatrix[',i,'][',j,']',inputMatrix[i][j],' inputMatrix[',j,'][',i,']',inputMatrix[j][i]
            if len(inputMatrix[i])!=len(inputMatrix):
                return False
            if i==j:
                if inputMatrix[i][j]!=1:
                    return False
            else:
                if inputMatrix[i][j]!=0:
                    return False
            j=j+1
        i=i+1

    #print matrix
    for i in inputMatrix:
        print i
    return True



# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False
