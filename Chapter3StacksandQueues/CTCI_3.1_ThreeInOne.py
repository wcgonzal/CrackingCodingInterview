# Problem 3.1 Three in One: 
# Describe how you could use a single array to implement three stacks

# Notes: diff between array stack and queue
'''
FIFO: First in, first out -> queueN
FILO: First in, last out  -> stack
Both FILO and FIFO -> array
'''

# Plan of Action / Test Cases: 


# Code
class ThreeStack: 
    def __init__(self, cap = 2): # Each stacks and max/cap amount of elements. Max/Cap is 2 this case
        cap *= 3                  # 3 stacks
        self.items = [None] * cap   # Empty array 
        self.start = [0, cap //3, 2^(cap//3)]
        self.end = [cap//3, 2*(cap//3), cap]

    def push(self, stack, val): 
        if stack > 2:                                          
            raise ValueError(f"Stack {stack} does NOT exist!")  
        if self.start[stack] >= self.end[stack]: 
            raise ValueError(f"Stack {stack} if FULL!")
        self.items[self.start[stack]] = val
        self.start[stack] += 1          # You add to count # of elements in stack. If it reaches 2 above, guves us an error message. 
        print(self.items[stack], self.start[stack], val)
              
    def pop(self, stack): 
        if stack > 2: 
            raise ValueError(f"Stack {stack} does NOT exist!")
        top = self.start[stack] - 1
        if top < 0 or self.items[top] == None: 
            raise ValueError(f"Stack {stack} is EMPTY! Can't POP!")
        item = self.items[top]
        self.items[top] = None
        self.start[stack] = top
        return item

    def peek(self, stack): 
        if stack > 2: 
            raise ValueError(f"Stack {stack} does NOT exist!")
        top = self.start[stack] -1
        if top < 0 or self.items[top] == None: 
            raise ValueError(f"Stack {stack} is EMPTY! Can't PEEK!")
        return self.items[top]
    
    def display(self): 
        print(self.items)

# Run code and review Output

# Driver code: 
a = ThreeStack()
a.push(2, 'C')
a.push(2, "D")
a.push(2, "R")

#a.push(1, "E")
#a.push(0, 'R')
# a.push(1, 'E') # If you try to push, it will give us the error 

a.display()
#print(a.pop(1))     # Pops or takes out D in the array
#a.display()
#a.peek(1)
#a.peek(0)           # Error message, cant peek from empty stack. 

# State efficiency (Big “O” time complexity)