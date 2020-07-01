# Trees and Graphs
## Exercises
*Completed* **=** :white_check_mark:

*Messy Solution* **=** :warning:

*Not Started* **=** :x:


| Number | Title                  | Status             |
|:------:|:----------------------:|:------------------:|
|   4.1  | Route Between Nodes | :x: |
|   4.2  | Minimal Tree | :x: |
|   4.3  | List of Depths | :x: |
|   4.4  | Check Balanced | :x: |
|   4.5  | Validate BST | :x: |
|   4.6  | Successor | :x: |
|   4.7  | Build Order | :x: |
|   4.8  | First Common Ancestor | :x: |
|   4.9  | BST Sequences | :x: |
|   4.10  | Check Subtree | :x: |
|   4.11  | Random Node | :x: |
|   4.12  | Paths with Sum | :x: |


:calendar: Chapter completed on *July 7 2020* :tada:

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

