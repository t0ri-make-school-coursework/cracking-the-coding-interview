class TreeNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

class LinkedListNode:
    def __init__(self, data=None):
        self.next = None
        self.data = data