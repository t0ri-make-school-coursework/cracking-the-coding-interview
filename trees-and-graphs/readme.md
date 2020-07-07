# Trees and Graphs
## Exercises
*Completed* **=** :white_check_mark:

*Messy Solution* **=** :warning:

*Not Started* **=** :x:


| Number | Title                  | Status             |
|:------:|:----------------------:|:------------------:|
|   4.1  | Route Between Nodes | :construction: |
|   4.2  | [Minimal Tree](minimal_tree.py) | :white_check_mark: |
|   4.3  | [List of Depths](list_of_depths.py) | :warning: |
|   4.4  | [Check Balanced](check_balanced.py) | :white_check_mark: |
|   4.5  | [Validate BST](validate_bst.py) | :white_check_mark: |
|   4.6  | [Successor](successor.py) | :question: |
|   4.7  | Build Order | :construction: |
|   4.8  | [First Common Ancestor](first_common_ancestor.py) | :white_check_mark: |
|   4.9  | [BST Sequences](bst_sequences.py) | :question: |


:calendar: Chapter completed on *July ... 2020* :tada:

# Notes
## Trees
### Types of Trees
A **tree** (which is actually a **graph**) is a data structure of nodes.
Tree Truths:
- Each tree has a root node
- Root node has 0 or more child nodes
- Each child node has 0 or more child nodes
- Nodes may not be in a particular order
- Node data can be of any type
- Children may or may not link back to parents
- A "leaf" has no children

> For the purposes of interview questions, we typically do not use a `Tree` class.

> Trees and graph questions are rife with ambiguous details and incorrect assumptions.

#### Trees vs. Binary Trees
Binary trees are trees with up to only two children per node.

[my vocab article](https://medium.com/swlh/exploring-binary-trees-8bc26b16f028)

#### Binary Tree vs. Binary Search Tree
A binary search tree is a binary tree in which every node fits a specific ordering property: all left descendents <= n < all right descendents.

A binary search tree:
```
      8
    /   \
   4     10
  / \      \
 2   6      20 
```

Not a binary search tree (12):
```
      8
    /   \
   4     10
  / \      \
 2   12      20 
```

> Interview candidates often assume tree questions are binary search trees, be sure to ask.

### Unbalanced vs. Balanced
> Another clarification to make with interviewers.
Two common balanced tree types are red-black trees and AVL (rotating self-balancing) trees

### Complete Binary Trees
- every level is fully filled except maybe last level (however last level is filled left to right)

not a complete binary tree (30):
```
      10
     /  \
   5     20
  / \      \
 3   7      30 
```

a complete binary tree:
```
      10
     /  \
   5     20
  / \    /
 3   7  15 
```

### Full Binary Trees
- every node either has 0 or 2 children

not a full binary tree:
```
       10
     /    \
   5       20
    \     /  \
     12  3    7 
        /  \
       9   18
```

a full binary tree:
```
       10
     /    \
   5       20
          /  \
         3    7 
        /  \
       9   18
```

### Perfect Binary Trees
- all interior nodes have 2 children
- all leaf nodes are at the same level

```
       10
     /    \
   5       20
 /  \     /  \
9    18  3    7
```

> Perfect binary trees are rare in interviews and real life, never assume a tree is perfect.

## Traversals
![img](https://miro.medium.com/max/700/0*YzOEfnGnWTPbsUkv)

### In Order Traversal
- Visit left branch, then current node, then right branch
- On a BST, in order traversal visits nodes in ascending order
```
def in_order(node):
    if node is not None:
        in_order(node.left)
        visit(node)
        in_order(node.right)
```
### Pre-Order Traversal
- Visit current node, then child nodes
- the root node is always the first node visited
```
def pre_order(node):
    if node is not None:
        visit(node)
        pre_order(node.left)
        pre_order(node.right)
```

### Post-Order Traversal
- Visit current node after child nodes
- root node is always the last node visited
```
def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        visit(node)
```

## Heaps
> Max-heaps are min-heaps but the elements are in descending order rather than ascending

[---> See CS2.1/Alan's Min Heap Here](https://github.com/t0ri/CS-2.1-Trees-Sorting/blob/master/Code/binaryheap.py)

A **min-heap** is a *complete* binary tree where each node is smaller than its children.  The root is the minimum element in the graph.

Its main operations are:
- insertion
- extract minimum element


```
       4
     /   \
    50    7
   / \   /
 55  90 87
```

### Insert
- insert element at bottom of heap at next available spot to maintain complete tree property
- swap element with its parent until we find an appropriate spot for the element (bubble_up)
- O(log n) time, n is nodes in heap

![insertion gif](https://i1.wp.com/algorithms.tutorialhorizon.com/files/2015/02/Insert-Bubble-Up-Min-Heap.gif)

### Extract Minimum Element
- minimum element is always root in min tree
- remove root element
- replace root with last element in heap
- swap this element with one of its children until min-heap property is restored (bubble_down)
- O(log n) time

![extract min gif](https://i1.wp.com/algorithms.tutorialhorizon.com/files/2015/02/Delete-OR-Extract-Min-from-Heap.gif?ssl=1)

## Tries / Prefix Trees
- k-ary tree in which characters are stored at each node
- each path down the tree represents a word
- terminal nodes mark the end of a word with a bool property

[Vaidehi Joshi on Tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)

Tries are often used to store the entire English language for quick prefix lookups.
O(k) time, where k is the length of the string
Common for autocompletion

[My trie autocomple library here](https://github.com/t0ri/autocomplete)

> Many problems involving lists of valid words leverage a trie as an optimization. In situations when we search through the tree on related prefixes repeatedly (looking up M, then MA, then MAN, then MANY), **we might pass around a reference to the current node in the tree**.  This will allow us to just check if Y is a child of MAN, rather than starting from the root each time.

## Graphs
