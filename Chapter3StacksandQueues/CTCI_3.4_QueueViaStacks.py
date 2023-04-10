



# Problem 3.4 Queue via Stacks: 
# Implement a MyQueue class which implements a queue using two stacks.

# Plan of Action / Test Cases: 
'''
'''
# Constraints 
# Code: 
class MyQueue: 

    def __init__(self): 
        self.stack = []
        self.stack2 = []

    def push(self, elem): 
        self.stack.append(elem)

    
    def pop(self): 
        while True: 
            topmost = self.stack[-1]
            self.stack2.append(topmost)

    def isEmpty(self): 

# State efficiency (Big “O” time complexity)

