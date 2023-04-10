
# Problem 1.7 Rotate Matrix: 
 # Given an image represented by an NxN matrix, where each pixel in the image is 4
 # bytes, write a method to rotate the image by 90 degrees. Can you do this in place? 

# Plan of Action / Test Cases: 
# We see that the pattern is sort of like a sine wave starting from first index, last row
# and going up the column until you get to first index, first row, then go down to 2nd index, 
# last row etc. You're basically making rows into columns and columns into rows. 
# 
'''
matrix = [[1, 2], 
          [3, 4]]
mapping = [[0,0  0,1]
           [1,0  1,1]]
matrix_90 = [[3, 1], 
            [4, 2]]

matrix = [[1, 2], [3, 4], [5, 6]]
matrix_90 = [[c, a], [b, d], [c, d]]


'''
# Constraints

# Method 1
# Code
def rotate_90(matrix): 
    matrix_90 = []
    row = len(matrix[::-1])
    for column in range(len(matrix[0])):           # Technically the matrce's rows but we are turning rows into columns remenber. 
        temp = []                               # Note 1
    #for row in range(len(matrix)-1,-1,-1):   # Review Note 2/3 ; Technically the matrice's column 
        temp.append(matrix[row][column])
        matrix_90.append(temp)                   # Calls Column and converts to row
    return matrix_90

# TODO Solve 2nd loop without range 

# Run code and review Output
#matrix = [[1,5,7],[9,6,3],[2,1,3]]
#matrix = [[1, 2], [3, 4]]
matrix = [[1,5,7,-7],
        [9,6,3,0],
        [2,1,3,14]]

print(rotate_90(matrix))

# Method 2: Code works only for NxN matrices not MxN for example
# Code
'''
def rotate_90(matrix): 
    matrix_90 = []
    column = len(matrix) - 1
    for column in range(len(matrix)): 
        temp = []
        for row in range(len(matrix)-1,-1,-1):        
            temp.append(matrix[row][column])
        matrix_90.append(temp)    
    matrix = matrix_90
    for i in range(len(matrix)): 
        for j in range(len(matrix)): 
            matrix[i][j] = matrix_90[i][j]
    return matrix
    '''
# Method 2: Rotates matrix couner clockwise
# Code
'''
def rotate_90(matrix): 
    Rows, Columns = len(matrix), len(matrix[0])
    matrix_90 = [[None]*Rows for _ in range(Columns)]   # list comprehension 
    print(matrix_90)
    for c in range(Columns): 
        for r in range(Rows-1,-1,-1): 
            matrix_90[Columns-c-1][r] = matrix[r][c]
    return matrix_90

i = rotate_90([[1,5,7],[9,6,3],[2,1,3]])
for j in i: 
    print(*j)   # unpacking variables 
                # * is diff then **

'''

'''
Note 3: 
Both list temp and matrix_90 serve same purpose. Remeber we can't create a matrix 
but we can make a list within a list to create a matrix. So
temp = [] and matrix_90 [] ===> matrix_90[temp[]] or [[a, b],[c, d]]
Note 2: 
The reason we subtract 1 from matrix (matrix-1) is because len() will give us the 
True length of the list but when we are coding, remeber that when calling and index
we start from 0, 1, 2, 3, etc NOT 1, 2, 3, etc. 
Note 3: 
range(start, stop, step) inlcuded negatives means it's going backwards

'''
# State efficiency (Big “O” time complexity)
