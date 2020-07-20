# Sorting and Searching
## Notes
Many sorting and searching problems are tweaks of the well-known algorithms.
A good approach is to run through the different sorting algorithms and see if one applies particularly well.

ex.
| Given a very large array of Person objects, sort the people in increasing order of age.
Gathered Info:
1. Large array -- efficiency is important
2. Sorting based on ages -- value range is small
From this information, we can figure bucket sort would be perfect.

### Common Sorting Algorithms
Of the five algorithms here, Merge Sort, Quick Sort, and Radix Sort are the most commonly used in interviews.

#### Bubble Sort
Time Complexity: O(n^2) average and worst
Memory: O(1)
Start at beginning of array, swap the first two elements if the first is greater than the second. Cycle through the array, checking each pair and continuously swapping, until it's sorted.


#### Selection Sort
Time Complexity: O(n^2) average and worst
Memory: O(1)
Scan linearly through the array to find the smallest element, and then swap it with the first element. Keep moving small elements to their place until the array is sorted.

#### Merge Sort
Time Complexity: O(n log (n)) average and worst case
Memory: Depends, or O(n) from merging array
Divide array in half, sort each of those halves, then merge them back together. Each half has the same algorithm applied to it. Eventually, you are just merging 1 item arrays.

#### Quick Sort
Time Complexity: O(n log (n)) average, O(n^2) worst case
Memory: O(log (n))
Pick a random element, partition the array, sort til items smaller than partition live on the left and items larger live on the right.
![img](https://thumbs.gfycat.com/PleasantCloseEyelashpitviper-size_restricted.gif)

#### Radix Sort
Time Complexity: O(kn), n is number of elements and k is number of passes of the sorting algorithm
Radix sort takes advantage of integers having finite numbers of bits. In radix sort, each digit of the number is iterated through and grouped by digit. Keep grouping by the next digit. Repeat until each digit is sorted.

### Searching Algorithms
In binary search, look for element in a sorted array by comparing it to the midpoint of the array. If it is less than the midpoint, search in the left half of the array. If it's greater, search in the right half. Repeat the process, comparing in each subarray, until we find the element of the subarray size is 0.