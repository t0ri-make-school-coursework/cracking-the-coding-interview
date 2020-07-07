# 4.4
# Check Balanced
# Implement a fucntion to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree such
# that the hieghts of the two subtrees of any node never differ by more than one
from minimal_tree import min_tree
from Node import TreeNode

def check_balanced(root): 
    # base case 
    if root is None: 
        return True
  
    # left & right heights
    left_height = root.height(root.left) 
    right_height = root.height(root.right) 
  
    # get positive value of difference in height
    height_difference = abs(left_height - right_height)
    
    # check height requirement satisfied
    if height_difference <= 1:
        # ... recursively
        if check_balanced(root.left) is True and check_balanced(root.right) is True: 
            return True
  
    # if we reach here means tree is not  
    # height-balanced tree 
    return False

if __name__ == "__main__":
    bal_root = min_tree([1,2,3,4,5,6,7,8,9,10,11,12])
    print(check_balanced(bal_root))

    unbal_root = TreeNode(5)
    unbal_root.left = TreeNode(4)
    unbal_root.left.left = TreeNode(3)
    unbal_root.left.left.left = TreeNode(2)
    unbal_root.left.left.left.left = TreeNode(1)
    unbal_root.right = TreeNode(6)
    print(check_balanced(unbal_root))