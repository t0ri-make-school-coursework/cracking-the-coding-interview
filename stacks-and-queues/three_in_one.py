# 3.1 
# Describe how you could use a single array to implement three stacks.
# Guided via https://darealnormanlee.wordpress.com/2014/06/21/using-a-single-array-to-implement-three-stacks-in-python/
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