

# Problem 3.2 Stack Min:
# How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum eiement? Push, pop and min should ail operate in 0 ( 1 ) time.

# Method 1: 
"""
class Stack: 
    def __init__(self): 
        self.stack_lst = []

    def push(self, elem): 
        self.stack_lst.append(elem)

    def pop(self): 
        del self.stack_lst[-1]
        return self.stack_lst[-1]
    def min(self): 
        min_elem = min(self.stack_lst)
        return min_elem
    
    def display(self): 
        print(self.stack_lst)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(-3)
s.display()
print(s.min())
"""

"""
Stack Min Functionality: The "Stack Min" problem requires implementing a stack data structure 
that has a third operation, min(), which returns the minimum element in the stack. This 
operation should also have a time complexity of O(1), which means it should take constant 
time to execute regardless of the size of the stack.
0817

Keeping Track of Minimum Element: In order to implement the min() operation in O(1) time, one 
approach is to keep track of the minimum element in the stack as elements are pushed and popped. 
One way to do this is to use a separate stack that keeps track of the minimum elements. 
This stack would be updated whenever an element is pushed or popped from the main stack.

"""

class MinStack: 
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, elem): 
        self.stack.append(elem) 
        if len(self.stack_min) == 0 or elem <= self.stack_min[-1]: 
            self.stack_min.append(elem) 

    def pop(self): 
        if self.isEmpty(): 
            print('Empty')
        x = self.stack[-1]
        del self.stack[-1]
        for i in range(len(self.stack_min)): 
            if x == self.stack_min[i]: 
                del self.stack_min[i]
                break
        return x

    def isEmpty(self): 
        return len(self.stack_min) ==0 and len(self.stack) == 0
    
    def display(self): 
        print('Main Stack: ', self.stack, "Min. Stack: ", self.stack_min )
        


ms = MinStack()
ms.push(1)
ms.push(-1)
ms.push(17)
ms.display()
ms.push(1)
ms.display()
ms.pop()
ms.display()


