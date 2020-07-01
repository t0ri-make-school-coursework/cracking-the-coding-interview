from LinkedList import LinkedList
from Node import Node

# 2.2
# Kth to Last
# Implement an algorithm to find the Kth to last element of a singly linked list
def kth_to_last(ll, k):
    last = ll.head
    kth = ll.head
    for _ in range(0, k):
        last = last.next
   
    while last is not None:
        kth = kth.next
        last = last.next
    
    return kth

if __name__ == "__main__":
    llist = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node3 = Node(3)
    node2.next = node3
    node4 = Node(4)
    node3.next = node4
    node5 = Node(5)
    node4.next = node5
    node6 = Node(6)
    node5.next = node6
    llist.head = node1
    print('llist', kth_to_last(llist, 6).data)
