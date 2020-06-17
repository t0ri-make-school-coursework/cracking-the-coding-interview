# Linked Lists
![img](https://www.geeksforgeeks.org/wp-content/uploads/gq/2013/03/Linkedlist.png)

Linked lists are data structures that represent a sequence of nodes.
**Singly linked lists** have each node pointing to the next node in the list.
**Doubly linked lists** have each node pointing to both the next node and previous node.

Linked lists do no have array-like constant time access to a particular index.
To get the Kth element, you have to iterate through the list K times.

Benefits:
- Add and remove in constant time.

> Remember that when you're discussing a linked list in an interview, you must understand whether it is a singly linked list or a doubly linked list.

## Creating a Linked List
Using a **LinkedList class that wraps the Node class** enables us to always have correct access to the current version of the head and tail so the list doesn't get manipulated unexpectedly, though **it is possible to *just* have a Node class** with a appendToTail() method and keeping a reference to the node you know is the head node.
```
# with LinkedList wrapper
class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # optional

# creating list
llist = LinkedList()
llist.head = Node('hi')
```

```
# without LinkedList wrapper
class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data
  
  def appendToTail(data):
      # create new node to append to tail
      end = Node(data)
      # hold onto current node (would be head)
      node = self
      # iterate through list until at final node
      while (node.next is not None):
          node = node.next
      # once node is tail, set node.next to the new data node
      node.next = end
```

## Deleting a Node from a Singly Linked List
```
def deleteNode(head, data):
    # if list is empty?
    if head is None:
        return None
    # set node as head
    node = head
    # if head is the node we're looking to delete
    if node.data is data:
        # return node.next as the new head node
        return node.next
    # iterate through the list until we get to the tail
    while node.next is not None:
        # if the next node is the node we're looking to delete
        if node.next.data is data:
            # set node.next to the next node's next node (:
            node.next = node.next.next
            # return the list's head node
            return head
        node = node.next # iterating
    # return the list's head node
    return head
```
> If the list is doubly linked, we must also update `n.next` to set `n.next.prev` equal to `n.prev`.
> The important things to remember are (1) to check for the null pointer and (2) to update the head or tail pointer as necessary.

## "Runner" Technique
![explanation of types of problems it appears in](https://i.gyazo.com/c3badc1832559ef1573c8cf0bfc416e4.png)
- Used in many linked list problems
- iterate simultaneously with 2 pointers moving by `node.next` and `node.next.next`
- by the time one is at the end, the other is at the midpoint

## Recursive Problems
If you're struggling with solving a linkedlist problem, explore a recursive approach.  A lot of times recursive solutions can be less complex than iterative ones.

