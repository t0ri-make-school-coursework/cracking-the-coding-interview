# 4.6
# Successor
# Write an algorithm to find the "next" node (ie in-order successor)
# of a given node in a binary search tree. You many assume that each
# node has a link to its parent.

# if node has left child
    # return left child
# if node has parent
    # go to node's parent
# if node is parent.left
    # return parent.right 