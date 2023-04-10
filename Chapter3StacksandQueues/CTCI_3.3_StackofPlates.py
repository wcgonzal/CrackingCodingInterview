# 3.3 Stack of Plates: 
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks . p u s h ( ) and SetOfStacks . p o p ( ) should behave identically to a single stack
# (that is, pop( ) should return the same values as it would if there were just a single stack).

# Plan of Action / Test Cases: 
# Create a list of lists
'''
push('a'), push('b'), push('c'), push('d'), push('e')
push('f') > Error('Stack A Full. '
Stack_A = ['a', 'b', 'c', 'd', 'e']
'Let's make a new stack'
Stack_B = []
'''
# Constraints
# Code

class Stack: 

    def __init__(self): 
        self.stack = []
        
    def push(self, elem): 
            self.stack.append(elem)
        
    def pop(self): 
        abc = self.stack[-1]
        del self.stack[-1]
        return abc

    def isEmpty(self): 
        return len(self.stack) == 0

    def size(self): 
        return len(self.stack)
    
    def createStack(self): 
        #print('Create a new Stack', self.stack)
        self.stack = []

    def display(self): 
         print(self.stack)
            # name each new stack
s = Stack()
lst_of_lst = []
cap_stack = 5
for i in 'abcdefghijklmno': 
    if len(s.stack) < cap_stack: 
        s.push(i)
    else: 
        lst_of_lst.append(s.stack)
        s.createStack()
        s.push(i)
    
# Append the last stack to the list of lists
lst_of_lst.append(s.stack)

# Run code and review Output
# Print the list of lists
print(lst_of_lst)

# FOLLOW UP
# Implement a function popAt( i n t index) which performsa pop operation on a specific sub-stack.
def popAt(substack, index):
    if index < 0 or index >= len(lst_of_lst):
        # index is out of range
        return None
    substack = lst_of_lst[index]
    if not substack:
        # sub-stack is empty
        return None
    return s.pop()

print(popAt(lst_of_lst, 1))
print(lst_of_lst)
# State efficiency (Big “O” time complexity)