# 4.5
# Implement a function to check if a binary tree is a binary search tree.
from minimal_tree import min_tree

def get_min(root):
    while root.left is not None:
        root = root.left
    return root.data


def get_max(root):
    while root.right is not None:
        root = root.right
    return root.data


def validate_bst(node, lower=None, upper=None): 
    # empty tree
    if node is None:
        return True
    
    if lower or upper is None:
        lower = get_min(node)
        upper = get_max(node)
        
    # ensure ordering property is in place
    if node.data <= lower or node.data >= upper:
        return False

    # recursively validate right path
    if not validate_bst(node.right, node.data, upper):
        return False
    
    # recrusively validate left path
    if not validate_bst(node.left, lower, node.data):
        return False
    
    return True

if __name__ == "__main__":
    bst_root = min_tree([1,2,3,4,5,6,7,8,9,10,11,12])
    # print(bst_root.data)
    print(validate_bst(bst_root))
