from LinkedList import LinkedList
from Node import Node

# 2.8
# Loop Detection
# Given a linked list which might contain a loop,
# implement an algorithm that returns the node at
# the beginning of the loop (if one exists).
def loop_detection(ll):
    if ll.head is not None:
        slow = ll.head
        fast = ll.head
        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = ll.head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
    return False


if __name__ == "__main__":
    loop_list = LinkedList()
    loop_node1 = Node(1)
    loop_node2 = Node(2)
    loop_node1.next = loop_node2
    loop_node3 = Node(3)
    loop_node2.next = loop_node3
    loop_node4 = Node(4)
    loop_node3.next = loop_node4
    loop_node5 = Node(5)
    loop_node4.next = loop_node5
    loop_node6 = Node(6)
    loop_node5.next = loop_node6
    loop_node6.next = loop_node1
    loop_list.head = loop_node1
    print('loop_list', loop_detection(loop_list))

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
    print('llist', loop_detection(llist))