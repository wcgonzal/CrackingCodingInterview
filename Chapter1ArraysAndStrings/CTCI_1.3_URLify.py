# Problem 1.3 URLify:
#  Write a method to replace all spaces in a string with #'%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. 

# Plan of Action / Test Cases: 
# Output string that is a place holder that is the length of original string 
# Use Arrays

''''
in_str  = 'to tim**'
out_str = 'to%20tim'

in_str  = 'so much fun****'
out_str = 'so%20much%20fun'

in_str  = 'infinity'
out_str = 'infinity'

in_str = "Mr 3ohn Smith 13"
out_str = "Mr%203ohn%20Smith"

'''
# Constraints 
# len(str) == len(str_updated)

# Code


'''maybe consider that you can multiply each one of the spaces available in a string you can multiply 
by 3 (len(%20)) from there, you cam then add * of however more spaces you will need in your string 

'''
"""
# get string 
# find length of string 
# find the amount of spaces in string
# to tim -> length =6 spaces = 1 ===> 3*1-1 = 2 so add ** 
# tiny tim buck -> length = 11 spaces 2 ===> 3*2 - 2 =  4 so add ****
def URLify(string):
    # compute length of new string based on # of spaces in input string
    new_len = 0
    reader = len(string) - 1  # index at end of un-extended string
    for char in string:
        if char == ' ':
            new_len += 3
        else:
            new_len += 1
    # extend length of string to fit URL
    string = list(string)
    writer = len(string) - 1  # index at end of extended string
    # traverse using double index technique to do this "in place"
    while reader >= 0 and writer >= 0:
        if string[reader] == ' ':  # if reader sees a space, the writer writes %20
            string[writer] = '0'
            string[writer - 1] = '2'
            string[writer - 2] = '%'
            reader -= 1  # reader and writer are advanced accordingly
            writer -= 3
        else:
            string[writer] = string[reader]  # if the reader sees a non-space, the writer copies it over
            reader -= 1  # reader and writer are advanced the same amount
            writer -= 1

print(URLify('Mr 3ohn Smith 13'))

"""
'''
in_str  = 'to tim**'
# detemine length of string and add * in the end 
# once you have your new str = to tim**
# as a live view replace 
out_str = 'to%20tim'

# Method 1
def URLify(org_str): 
    org_str = "to tim times two"
    spaces_str = org_str.count(' ')
    astrek = 3*spaces_str - spaces_str
    org_str = org_str + '*'* astrek
    len_org_str = len(org_str)
    for cursor in org_str: 
        if cursor != ' ': 
            org_str = cursor
        else: 
            cursor[len_org_str] = "%"
            cursor[len_org_str -1] = "2"
            cursor[len_org_str-2] = "0"
'''

# Run code and review Output
'''
Note1: 
[] indexing starts at 0 and ends at 1 less then actual #
str = "Mr 3ohn Smit h 13'
str[0:4] = 'Mr 3'
str[1:4] = 'r 3'
'''
# State efficiency (Big “O” time complexity)

read string, if not an empty sspace " " then add to new list
if space, begin adding %20 but move/shift spaces to the right 

def URLify(in_str): 
    len(in_str)
    a = %20
    emp = []


    in_str.count(' ')
    len_new_str = space*3-2

in_str  = 'to tim**'
out_str = 'to%20tim'

