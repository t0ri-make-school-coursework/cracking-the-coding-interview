# 8.3
# Magic Index
# A magic index in an array A[0 ... n-1] is defined to be an index such that A[i] = i.
# Given an array of distinct integers, write a method to find a magic index, if one exists,
# in array A.

# Brute Force
def magic_index_brute(arr):
    for index, value in enumerate(arr):
        if index is value:
            return index

# Binary Search
def magic_index_binary_search(arr, start=None, end=None):
    # init
    print(start, end)
    if start or end is None:
        start = 0
        end = len(arr) - 1
    # if there is no magic index
    if end < start:
        return None
    # get midpoint
    mid = (start + end) / 2
    print(mid)
    # check midpoint is magic index
    if arr[mid] is mid:
        return mid
    # if not, check if we need to search left or right of mid
    elif arr[mid] > mid:
        return magic_index_binary_search(arr, start, mid - 1)
    else:
        return magic_index_binary_search(arr, mid + 1, end)


if __name__ == "__main__":
    # print(magic_index_brute([-1, 0, 1, 3, 5]))
    print(magic_index_binary_search([-1, 0, 1, 3, 5]))