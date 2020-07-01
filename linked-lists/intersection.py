from LinkedList import LinkedList
from Node import Node

# 2.7
# Intersection
# Given two (singly) linked lists, determine if the
# two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on
# reference, not value. That is, if the kth node of
# the first linked list is the exact same node (by
# reference) as the jth node of the second linked
# list, then they are intersecting.
def intersecting_llists(ll1, ll2):
    ll1node = ll1.head
    ll2node = ll2.head
    while ll1node is not None:
        while ll2node is not None:
            if ll1node is ll2node:
                return ll1node
            ll2node = ll2node.next
        ll1node = ll1node.next
        ll2node = ll2.head
    return False

if __name__ == "__main__":
    ll1 = LinkedList()
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
    ll1.head = node1

    ll2 = LinkedList()
    node7 = Node(7)
    node8 = Node(8)
    node7.next = node8
    node9 = Node(9)
    node8.next = node9
    node10 = Node(10)
    node9.next = node10
    node10.next = node3
    ll2.head = node7

    print(intersecting_llists(ll1, ll2).data)
