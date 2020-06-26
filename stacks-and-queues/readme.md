# Stacks and Queues
## Stacks
Stacks - last in first out
Operations:
- `pop()`: remove the top item from the stack
- `push(item)`: add an item to the top of the stack
- `peek()`: return the top of the stack
- `is_empty()`: return true if and only if the stack is empty
Stacks do not offer constant time access to any element (unlike arrays)
A stack can be implemented using linked lists (if items are added and removed from head)
> Sometimes you need to push temporary data onto a stack as you recurse, but then remove them as you backtrack (for example, because the recursive check failed). A stack offers a intuitive way to do this.

```
class Stack:
     def __init__(self):
         self.items = []

     def is_empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]
```

## Queues
Queues - first in first out
Operations:
- `enqueue(item)`: add an item to the end of the queue
- `dequeue()`: remove the first item from the queue
- `peek()`: return the top of the queue
- `is_empty()`: return true if and only if the queue is empty
Queues can also be implemented with a linked list
> It is especially easy to mess up the updating of the first and last nodes in  a queue.  Be sure to double check this.

> Queues are often used in breadth-first search or in implementing a cache.

```
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
```
