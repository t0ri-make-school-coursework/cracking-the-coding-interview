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