from Node import LinkedListNode

class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        node = self.head
        print('-------------------')
        while node is not None:
            print('->', node.data)
            node = node.next