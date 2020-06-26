class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
    
    def print_list(self):
        node = self.head
        print('-------------------')
        while node is not None:
            print('->', node.data)
            node = node.next


# 2.8
# Loop Detection
# Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists).
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


def run_loop_detection():
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
# run_loop_detection()


# 2.4
# Partition
# Write code to partition a linked list around a value target, such that all nodes less than target come before all nodes greater than or equal to target.
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

def run_partition_llist():
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
    # print('llist', partition_llist(llist, 4))
# run_partition_llist()


# 2.7
# Intersection
# Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
# Note that the intersection is defined based on reference, not value.
# That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
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

def run_intersecting_llists():
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
# run_intersecting_llists()

# 2.3
# Delete Middle Node
# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.
def delete_midpoint(ll):
    # node.value = node.next.value
    # node.next = node.next.next
    pass


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

def run_kth_to_last():
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
# run_kth_to_last()


# 2.1
# Remove Duplicates
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


def run_remove_dups():
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
# run_remove_dups()