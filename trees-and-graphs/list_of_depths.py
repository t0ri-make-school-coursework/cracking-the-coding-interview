from minimal_tree import min_tree
from Node import LinkedListNode, TreeNode
from LinkedList import LinkedList

# 4.3
# List of Depths
# Given a binary tree, design an algorithm which creates a linked list of all the
# nodes at each depth (eg you have a tree with depth D, you'll have D linked lists)

# loop through depths
    # at each depth, create a linked list
    # for each node in depth
        # append a node to the linked list

def find_depth(node):
    # base cases
    # if tree has no nodes
    if node is None:
        return 0
    # if root has no children
    if node.left is None and node.right is None:
        return 1
    # tree has many nodes
    else:
        # recursively find the depth of branches of tree
        left_depth = find_depth(node.left) + 1
        right_depth = find_depth(node.right) + 1
        # return the larger depth
        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth


def list_depths(node, linked_lists=None, depth=None):
    # if empty tree passed in
    if node is None:
        return list() # or None
    # if no depth yet
    if depth is None:
        depth = find_depth(root)
    # if no lists yet
    if linked_lists is None:
        linked_lists = [LinkedList()] * depth


if __name__ == "__main__":
    root = min_tree([1,2,3,4,5,6,7,8,9,10,11,12])
    print(find_depth(root))
    list_depths(root)


