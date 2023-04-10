
# Problem 1.2 Check Permutation: 
# Given two strings, write a method to decide if one is a
#  permutation of the other. 

# Plan of Action / Test Cases: 
# Test each letter in the shorter string to see if it's in the larger string
# If so, place string into a list then at end if list ==  original string -> it's a permutation 

'''
input 
str1 = "orange"
str2  = "orange soda"
output 
Yes, str1 is a permutation of str2. 
'''
# Constraints 
# str1 = str2

# Code: 
# Method 2: Much better...
def perm(str1, str2): 
    output_var = True
    str1, str2 = str1.replace(' ', ''), str2.replace(" ", '')
    if len(str1) != len(str2): 
        output_var = False   
        # else statement not necessary
    #print(str1,str2)
    str1, str2 = str1.lower(), str2.lower() # lower() needs to go before sorted() 
                                            # bc lower() only takes strings not lists
    # print(str1,str2)
    str1, str2 = sorted(str1), sorted(str2)
    # print("Sorted returns a list", str1,str2)
    for i in range(len(str1)):
        # print(str1[i], str2[i])
        if str1[i] != str2[i]:
            output_var = False 
            break       
        else: 
            i += 1      # Need so we can keep comparing rest of characters in string 
                        # else it would stop at [0]
    return output_var
    
# Run code and review Output
#str1, str2 = 'bCa','abc'
#str1, str2 = 'abc','abc'
#str1, str2 = 'bac','abc'
str1, str2 = "geek sforgeEks" , "forgeeksGeekS"
print(perm(str1,str2))

# Code
'''
# Method 1: First Attemp you Newwb
def permutation(str1,str2): 
    lst = []
    output_var = True        
    for i in str1: 
        if i in str2: 
            lst.append(i)
        else: 
            output_var = False        
    return output_var 
'''

# State efficiency (Big “O” time complexity)

'''
### Attempt #2 
1.2 Check Permutation: Given two strings, write a method to 
decide if one is a permutation of the other
str1 = 'abcd'
str2 = 'ab'
str1 = "abcd"
str2 = "dabc"
str1 = "geeksforgeeks" 
str2 = "forgeeksgeeks"
str1 = "abCd"
str2 = "dabc"
'''
def perm(str1, str2): 
    output_var = True    
    if len(str1) != len(str2): 
        output_var = False   
        # else statement not necessary
    #print(str1,str2)
    str1, str2 = str1.lower(), str2.lower() # lower() needs to go before sorted() 
                                            # bc lower() only takes strings not lists
    # print(str1,str2)
    str1, str2 = sorted(str1), sorted(str2)
    # print("Sorted returns a list", str1,str2)
    for i in range(len(str1)):
        # print(str1[i], str2[i])
        if str1[i] != str2[i]:
            output_var = False 
            break       
        else: 
            i += 1      # Need so we can keep comparing rest of characters in string 
                        # else it would stop at [0]
    return output_var

#str1, str2 = 'bCa','abc'
#str1, str2 = 'abc','abc'
#str1, str2 = 'bac','abc'
str1, str2 = "geeksforgeEks" , "forgeeksGeekS"
print(perm(str1,str2))

