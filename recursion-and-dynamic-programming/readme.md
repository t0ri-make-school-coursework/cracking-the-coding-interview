# Linked Lists
## Exercises
*Completed* **=** :white_check_mark:

*Messy Solution* **=** :warning:

*Not Started* **=** :x:


| Number | Title                  | Status             |
|:------:|:----------------------:|:------------------:|
|   8.1  | [Triple Step](triple_step.py) | :white_check_mark: |
|   8.2  | [Robot Grid](robot_grid.py)   | :x: |
|   8.3  | [Magic Index](magic_index.py) | :white_check_mark: |
|   8.4  | [Power Set](power_set.py) | :white_check_mark: |
|   8.5  | [Recursive Multiply](recursive_multiply.py) | :white_check_mark: |
|   8.6  | Towers of Hanoi | :x: |
|   8.7  | [Permutations without Dups](permutation_no_dups.py) | :white_check_mark: |
|   8.8  | [Permutations with Dups](permutation_dups.py) | :construction: |


:calendar: Chapter completed on *July 14 2020* :tada:

# Notes
Many recursive problems follow similar patterns:
- "Design an algorithm to compute the nth..."
- "Write code to list the first n..."
- "Implement a method to compute all..."
People typically have 50% accuracy in their "this sounds like a recursive problem" instinct

## Solving Recursive Problems
Recursive solutions are built off of solutions to subproblems.
This often means you must compute f(n) by adding something, removing something, or otherwise changing the solution for f(n-1).
You might solve the problem for the first half of data, then the other half, then merge the results.

### Bottom-Up Approach
Start with knowing how to solve the problem for a simple case, like a list with only 1 element.
Then figure out how to solve for two elements, then for three elements, and so on.
Constantly consider how you can build the solution off of your previous solution with a previous case.

### Top-Down Approach
Think about how you can divide the problem into N subproblems.

### Half-and-Half Approach
Dividing the dataset in half can also help solve the problem.
For exmaple, binary search works with a "half-and-half" approach.
> We recurse and search for it in that half.

## Recursion vs Iteration
Each recurisve call adds a new layer to the stack.
It's often better to implement a recursive algorithm iteratively.
Discuss the tradeoffs with your interviewer:
Pros: Code is less complex
Cons: Code is less efficient

If each action inside a recursive function is O(1), the runtime of the function is the number of calls made.
