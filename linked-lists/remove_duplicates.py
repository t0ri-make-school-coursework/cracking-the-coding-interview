from LinkedList import LinkedList
from Node import Node


# 2.1
# Remove Duplicates
# Write code to remove duplicates from an unsorted list.
def remove_dups(ll):
    nodes = dict()
    node = ll.head

    while node.next is not None:
        if node.data not in nodes:
            nodes[node.data] = node
        
        if node.next.data in nodes:
            node.next = node.next.next
        else:
            node = node.next

    return ll


if __name__ == "__main__":
    llist = LinkedList()
    node1 = Node('A')
    node2 = Node('B')
    node1.next = node2
    node3 = Node('C')
    node2.next = node3
    node4 = Node('C')
    node3.next = node4
    node5 = Node('D')
    node4.next = node5
    node6 = Node('E')
    node5.next = node6
    node7 = Node('B')
    node6.next = node7
    node8 = Node('J')
    node7.next = node8
    llist.head = node1
    llist = remove_dups(llist)
    llist.print_list()
