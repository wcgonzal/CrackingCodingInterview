# Prolbem 1.1 Is Unique: 
# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

# Plan of Action / Test Cases: 
# What makes a string uniques is that a letter 
# is only presnt once. Go down the line of the string and add letters
# to a list, if at some point you add a letter that is already
# exists in the list, then our string is not unique. 
'''
str = "abc"
Unique (Boolean)? True 

str2 = "aabc"
Unique (Boolean)? False

str3 = "zxy"
Unique (Boolean)? True 

'''
         

'''
# Code
# Method 1
def unique(x):
    dic = []
    for i in x: 
        if i in dic: 
            return False 
        else: 
            dic.append(i)
    return True

print(unique('abc11'))
'''
# Method 2: Only use Return ONCE

def unique(input_str): 
    test = []
    output_var = True       # Get into habit of using output_var = the answer you KNOW is correct. 
    for char in input_str: 
        if char in test: 
            output_var = False
            break
        else: 
            test += char
    return output_var 

#str = "abc"
str = "aabc"
#str = "zxy"
print(unique(str))

# It forces you to name your variables better i.e. _str _int _boul
# What do you want your return to be? is the question
# Attempt to write short code 

# Run code and review Output

# State efficiency (Big “O” time complexity)

