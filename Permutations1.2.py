# 1.2  Check Permutation Problem:  
# Given two strings, write a method to decide 
# if one is a permutation of the other. 

# Rephrasing / Plan of action: 

# Constraints 

# Code: 
def permutation(test_str):
    if len(test_str)  == 1: 
        return [test_str]
    perms = permutation(test_str[1:])
    x = test_str[0]
    result = []
    #Recursion is when you use same function within function.
    for j in perms: 
        for i in range(len(j) + 1):
            result.append(j[:i] + x + j[i:])
    return result 

# Run code and review Output
# Comparnig 2 strings
print(len(permutation("abcd")), permutation("abcd"))
print(len(permutation("efgh")), permutation("efgh"))
s1 = permutation("abcd")
s2 = permutation("efgh")

print(set(s1) == set(s2))

# State efficiency (Big "O" time complexity)
# O(N^2) due to double for loop