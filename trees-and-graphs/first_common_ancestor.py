from minimal_tree import min_tree
from Node import TreeNode

# 4.8
# First Common Ancestor
# Design an algorithm to find the first common ancestor of two nodes in a binary tree.

# traverse tree to find node1
# traverse tree to find node2
# 2 pointer traverse both traversal_node1 is not traversal_node2

def first_ancestor(root, node1, node2): 
    # base case
    if root is None:
        return None
  
    # If both nodes are smaller than the root,
    # traverse down left recursively
    if root.data > node1.data and root.data > node2.data: 
        return first_ancestor(root.left, node1, node2) 
  
    # If both n1 and n2 are greater than root, then LCA 
    # lies in right  
    if root.data < node1.data and root.data < node2.data: 
        return first_ancestor(root.right, node1, node2) 
  
    return root.data

if __name__ == "__main__":
    root = min_tree([1,2,3,4,5,6,7,8,9,10,11,12])
    print(first_ancestor(root, root.right.left, root.right.right))
    print(first_ancestor(root, root.left.left, root.right.right))
    root2 = min_tree([1,2,3,4,5,6,7])
    print(first_ancestor(root2, root2.left.left, root2.left.right))


