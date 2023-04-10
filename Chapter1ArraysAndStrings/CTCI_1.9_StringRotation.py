
# Problem 1.9 String Rotation: 
# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, si and s2, write code to check if s2 is a 
# rotation of si using only one call to isSubstring 


# Plan of Action / Test Cases: 
# Have to test if the strings are the same length and have the same letters
# Method 1: Next is starting at a specific letter point, and checking for that new starting point
# if letters match
# Method 2: Duplicate first string then simply figure out if the second string is within 1st string. 
# much simpler 
'''
s1 = "waterbottle" 
s2 ='erbottlewat'
output_var = True

s1 = "pythonprogram"
s2 = "thonprogrampy" 
output_var = True

s1 = "cat"
s2 = "dog" 
output_var = False

s1 = "reddog"
s2 = "erdgod" 
output_var = True

s1 = "waterbottle " # Remove spaces before or after the word 
s2 ='erbottlewat'
output_var = True

'''
# Code: Method 2
# TODO Clean it up, too many output_var statements. 
def isSubstring(s1, s2): 
    output_var = True
    s1_len, s2_len = len(s1), len(s2)
    s1 = s1*2
    if s1_len == s2_len and s2 in s1: 
        output_var = True
    else: 
        output_var = False
    return output_var
        
"""
# Code: Method 1
def isSubstring(s1, s2): 
    output_var = True
    s1_len, s2_len = len(s1), len(s2)
    s1_srt, s2_srt = ''.join(sorted(s1)), ''.join(sorted(s2))
    while s1_len == s2_len and s1_srt == s2_srt: 
        for i, j in s1, s2: 
            if i == j: 
                if s1[::] == s2 [::]: #TDOO 
                    return output_var
                else: 
                    output_var = False
    
    else: 
        output_var = False
"""

# Run code and review Output
#s1 = "waterbottle" 
#s2 = 'erbottlewat'
# output_var = True
#s1 = "cat"
#s2 = "dog" 
#output_var = False
s1 = "reddog"
s2 = "erdgod" 
#output_var = True

print(isSubstring(s1,s2))



# State efficiency (Big “O” time complexity)

'''
CTL + tild (~) Brings up the power sheel/ terminal 
POrtable: python language that can be used in any system (linux, Mac,Windows)
'''