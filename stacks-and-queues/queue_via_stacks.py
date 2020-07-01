# 3.4 
# Implement a MyQueue class which implements a queue using two stacks.
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
