# 4.1
# Minimal Tree
# Given a sorted (increasing order) array with unique integer elements, 
# write an algorithm to create a binary search tree with minimal height.
from Node import TreeNode

def min_tree(arr):
    # base case
    if len(arr) is 0:
        return None
    
    # make node from middle of array
    mid = len(arr) / 2
    node = TreeNode(arr[mid])

    # recursively make node from each middle of each half of each array
    node.left = min_tree(arr[:mid])
    node.right = min_tree(arr[mid+1:]) # +1 to not include current mid

    # returns root
    return node

if __name__ == "__main__":
    root = min_tree([1,2,3,4,5,6,7,8,9,10,11,12])
    print(root.data)
    print(root.left.data)
    print(root.right.data)
    print(root.left.left.data)
    print(root.left.right.data)
    print(root.right.left.data)
    print(root.right.right.data)
    print(root.left.left.left.data)
    print(root.left.left.right.data)
    print(root.left.left.right.data)
    print(root.left.right.left.data)
    print(root.right.left.left.data)
    print(root.right.right.left.data)





