# 3.1 
# Describe how you could use a single array to implement three stacks.
# https://darealnormanlee.wordpress.com/2014/06/21/using-a-single-array-to-implement-three-stacks-in-python/
class TripleStack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * 3 * size
        self.top = [0, 0, 0]
 
    def push(self, data, stack_num):
        # check stack exists
        if stack_num < 3 and stack_num >= 0:
            # calculate index
            self.stack[stack_num * self.size + self.top[stack_num]] = data
            # adjust top of stack index
            self.top[stack_num] += 1
 
    def pop(self, stack_num):
        # check stack exists
        if stack_num < 3 and stack_num >= 0:
            # hold onto current top of stack
            temp = self.stack[self.top[stack_num]]
            # set top of stack equal to nothing
            self.stack[self.top[stack_num]] = None
            # adjust top of stack index
            self.top[stack_num] -= 1
            return temp


# 3.2 
# How would you design a stack which, in addition to push and pop,
# also has a function min which returns the minimum element?
# Push, pop and min should all operate in O(1) time.
class Stack:
    def __init__(self):
        self.items = []
        self.minimums = []
        self.min = None

    def push(self, item):
        self.items.append(item)
        if item < self.min or self.min is None:
            self.minimums.append(item)

    def pop(self):
        if self.peek() is self.min:
            self.minimums.pop()
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def get_min(self):
        return self.min


# 3.5 Implement a MyQueue class which implements a queue using two stacks.
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
  
    def enqueue(self, item):
        # Shift all elements from stack1 to stack2
        while len(self.stack1) is not 0:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
  
        # Push item into self.stack1
        self.stack1.append(item)
  
        # Shift everything back to stack1  
        while len(self.stack2) is not 0:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
  
    def dequeue(self):       
        item = self.stack1[-1]  
        self.stack1.pop()  
        return item

