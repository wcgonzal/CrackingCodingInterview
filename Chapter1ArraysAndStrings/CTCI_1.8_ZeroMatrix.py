
# Problem: 1.8 Zero Matrix: 
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row 
# and column are set to 0. 

# Plan of Action / Test Cases: 
# Method 1
# Count number of rows and columsn in your original matrix and creat an empty matrix
# Read each element until you find a zero
# Create a matrix of MxN full of zeros
'''
x = [[3, 2, 4 ],
    [6, 8, 1],
    [1, 0, 5] ]
output_x = [[3, 2, 4 ],
             [6, 8, 1],
             [1, 0, 5] ]

x = [[3, 2, 4 ],
    [0, 8, 1],
    [1, 3, 5] ]
output_x = [[0, 2, 4 ],
            [ 0, 0, 0],
             [0, 3, 5] ]

x = [[1, 2]
    [5, 0]]
output_x = [[1, 0]
            [0, 0]]

'''
# Code: 
def zero_matrix(x): 
    FirstColHasZero = False 
    FirstRowHasZero = False 

    x_columns = len(x[0])
    x_rows = len(x)
    for row in range(x_rows): 
        if x[row][0] == 0:  # 1st element of of however many rows matrix has
            FirstColHasZero = True
            break
    for col in range(x_columns): 
        if x[0][col] == 0: 
            FirstRowHasZero = True 
            break 
    
    for row in range(1, x_rows): 
        for col in range(1,x_columns): 
            if x[row][col] == 0: 
                x[0][col] = 0
                x[row][0] = 0

    for row in range(1, x_rows): 
        for col in range(1,x_columns): 
            if x[0][col] == 0 or x[row][0] == 0: 
                x[row][col] == 0

    if FirstRowHasZero: 
        for col in range(x_columns): 
            x[0][col] = 0
    if  FirstColHasZero:
        for row in range(x_rows): 
            x[row][0] = 0
    
    return x


        
    '''
    for i in range(len(x)): 

        if i == 0: 
            x =  [[0] * x_rows for _ in range(x_columns)]
        else: 
            print(x) 
    '''


x = [[1, 0], [4, 3], [5, 6]]
print(zero_matrix(x))
# Run code and review Output: 
# State efficiency (Big “O” time complexity): 
