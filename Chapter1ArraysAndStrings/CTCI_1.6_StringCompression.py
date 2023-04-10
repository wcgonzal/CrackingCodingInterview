
# Problem 1.6 String Compression: 
# Implement a method to perform basic string compression 
# using the counts of repeated characters. If the "compcompre_strsed" 
# string would not become smaller than the original string, your
# method should return the original string. 

# Plan of Action / Test Cases: 
# Read each letter 1 by 1 in str1, then add each letter to empty str 
# with the value being actual amount character
# If len(str1) <= len(compre_str) print str1 
'''
# For example, 
str1 = 'aabcccccaaa'
compre_str =' a2b1c5a3'

str1 = "abbbaaaaaaccdaaab"
compress_str = "a1b3a6c2d1a3b"
'''
# Constraints
# You can assume the string has only uppercase and lowercase letters (a - z).

# Code
def Compcompre_strsion(str1): 
    compre_str = ''
    count = 1
    for i in range(1, len(str1)):               # You start at range 1 so you can compare str1[0] or str1[i-1]
        if str1[i] == str1[i-1]: 
            count += 1
        else: 
            compre_str += str1[i - 1]           # Finds that char i-1 and i are not the same so adds
            compre_str += str(count)            # the last letter it kept count of and it's actual count
            count = 1                           # Reset back to 1

    compre_str = compre_str + str1[-1]         # We cant add the last character in str1 above
    compre_str += str(count)                   # these last strings are dedicated to last char or str1[-1]
        
    if len(str1) < len(compre_str):          # The point of this exercise is to compress string
         compre_str = str1                   # Note 1 # if "new" / comp. string > "original" / str1 might as well
    return compre_str                        # print out original str

# Run code and review Output
#str1 = 'aabcccccaaa'
#str1 = "abbbaaaaaaccdaaab"
str1 = "abc"
print(Compcompre_strsion(str1))
'''
Note 1: 
think of the problem as there only be 1 output to hellp Reduce use of Return statment
Even if your output statemnt changes during coding, return to 1 output_str. 
'''

# State efficiency (Big “O” time complexity)