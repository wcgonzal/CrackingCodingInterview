
# Problem 1.4 Palindrome Permutation: 
# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. The palindrome does not need to be 
# limited to just dictionary words.

# Plan of Action / Test Cases: 
# Read first character in str and if there is a duplicate in str of that 
# char, add both letters to new list. If there is only 1 remaining letter, 
# that is a Palindrome Permutation
'''
# EXAMPLE 

Input: Tact Coa
Output: True (permutations: "taco cat" , "atco cta" , etc. )
'''
# Constraints
# All letters have a match, except the middle one. There can only 
# be 1 unique character. 
# Code
def pal_perm(input_str): 
    input_str = input_str.replace(' ','')
    input_str = input_str.lower()
    pal_perm_str = {}
    for char in input_str: 
        if char in pal_perm_str: 
            pal_perm_str[char] += 1
        else: 
            pal_perm_str[char] = 1
    
    odd_count = 0 
    for k, v in pal_perm_str.items(): 
        if v % 2 != 0 and odd_count == 0: 
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0: 
         return False
    return True

#input_str = "Tact Coa"
#input_str2 = "civic"
#input_str3 = "ivicc"
#input_str4 = "civil"
input_str = "AabB"
print(pal_perm(input_str))
    
# Run code and review Output

# State efficiency (Big “O” time complexity)
