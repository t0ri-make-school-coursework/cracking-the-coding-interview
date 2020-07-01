from LinkedList import LinkedList
from Node import Node

# 2.4
# Partition
# Write code to partition a linked list around a
# value target,such that all nodes less than target
# come before all nodes greater than or equal to target.
def partition_llist(ll, target):
    high_nodes = [Node('partition')]
    node = ll.head
    while node.next is not None:
        if ll.head.data >= target:
            high_nodes.append(ll.head)
            ll.head = node.next
        if node.next.data >= target:
            high_nodes.append(node.next)
            node.next = node.next.next
        else:
            node = node.next
    for high_node in high_nodes:
        high_node.next = None
        node.next = high_node
        node = node.next
    return ll

if __name__ == "__main__":
    llist = LinkedList()
    node1 = Node(6)
    node2 = Node(2)
    node1.next = node2
    node3 = Node(4)
    node2.next = node3
    node4 = Node(5)
    node3.next = node4
    node5 = Node(1)
    node4.next = node5
    node6 = Node(3)
    node5.next = node6
    llist.head = node1
    llist = partition_llist(llist, 4)
    llist.print_list()
    print('llist', partition_llist(llist, 4))