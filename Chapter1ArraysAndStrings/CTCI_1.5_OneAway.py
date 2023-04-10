
# Problem 1.5 One Away: 
# There are three types of edits that can be performed on strings:
#  insert a  character, remove a character, or replace a character. 
# Given two  strings, write a function to check if they are
# one edit (or zero edits) away.

# Plan of Action / Test Cases: 
# Test if len(first_str) - len(second_str) > 1 (that means it underwent more 
# than 1 insert)
# From there start testing if there is difference of first_str and second_str 
# is only by one letter/charaacter or multiple 
'''
pale , pie - > false
pale -> remove a -> replace l w. i -> pie

pales , pale - > true
pale -> remove s -> pale

pale , bale - > true
pale -> replace p w/ b -> bale

pale , bake - > false
pale - > replace p w/ b -> replace l w/ k -> bake
'''

# Constraints

# Code
def test_one_edit_away(fst_str, scd_str): 
    fst_len = len(fst_str)
    scd_len = len(scd_str)
    count_changes = 0
    if fst_str == scd_str or abs(fst_len-scd_len) > 1: 
        return False
    if fst_len == scd_len: 
        for i in range(fst_len): 
            if fst_str[i] != scd_str[i]: 
                count_changes += 1
            if count_changes > 1: 
                return False 
        return True 
    elif fst_len > scd_len: 
        for i in range(scd_len): 
            if scd_str[i] != fst_str[i] and scd_str[i] != fst_str[i+1]: 
                return False
    else: 
        for i in range(fst_len): 
            if fst_str[i] != scd_str[i] and fst_str[i] != scd_str[i+1]:
                return False
    return True

# Run code and review Output
#fst_str = 'pale'
#scd_str = 'pie'
#fst_str = "pales"
#scd_str = 'pale'
#fst_str = "pale"
#scd_str = "bale"
fst_str = "apple"
scd_str = "apple"
#fst_str = 'pale' 
#scd_str = 'bake' 


print(test_one_edit_away(fst_str, scd_str))
# State efficiency (Big “O” time complexity)