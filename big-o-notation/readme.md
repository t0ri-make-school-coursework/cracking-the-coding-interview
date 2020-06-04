# Big O Notation
Big O, or _asymptotic runtime_, is the language and metric we use to describe the efficiency of algorithms.
Big O describes the rate of increase -- no matter the size of the constant is or how slow the linear increase is, linear will at some point surpass the constant.

## Best Case, Worse Case,  Expected Case
> We rarely ever discuss **best case time complexity**, because it's not a very useful concept.  After all, we could take essentially any algorithm, special case some input, and then get an O(1) runtime in the best case.
> For many -- probably most -- algorithms, the worst case and expected case are the same.

### Worst Case
Caused by specific input or just unluckiness, the worst case is the slowest run time of an algorithm.  Perhaps in quick sort, your pivot is the first element in  a reverse-ordered array so each recursive step only shrinks the subarray by 1 element instead of splitting the array in half.

### Expected Case
The average runtime, in which the worst case isn't repeating itself recursively.

## Space Complexity
> If we need to create an array of size _n_, this will require O(_n_) space.  If we need a two-dimensional array of size _n_ by _n_, this will require O(_n^2_) space.

Stack space in recurive calls count too!  But just because you have _n_ calls doesn't mean it takes O(_n_) space.
Example: Looping through a list ([0, 1, 2, 3, 4, ...]) and adding adjacent numbers using a pairSum() helper method doesn't add more space to the call stack.

## Constants & Simplification
Constants are dropped in Big O because O(_n_) could potentially run faster than O(1).  Similarly, O(2 _n_) is simplified to O(_n_).
> In practice, one O(_n_) algorithm might be much faster than another -- and the O(_n^2_ algorithm might be faster than both on some inputs.)

### Drop Non-Dominant Terms
- O(_n^2_ + _n_) => O(_n^2_)
- O(_n_ + _log n_) => O(_n_)
- O((5 * 2^_n_) + (1000 * _n^100_) => O(2^_n_)

![Graph of Big O Rate of Increase](https://miro.medium.com/max/2928/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)

### Add vs Multiply
> If your algorithm is in the form "do this, then, when you're all done, do that" then you add the runtimes.
> If your algorithm is in the form "do this for each time you do that" then you multiply the runtimes.

## Amortized Time
Consider you have a list of size _n_.  You add an item to the list, and the array reaches its capacity, so it must dynamically resize.  To create an array of size _2n_ and copy over _n_ elements will take O(_n_) time.  However, this occurrence is rare -- amortized time takes note of that.

## Log N Runtimes
> When you see a problem where the number of elements in the problem space gets halved each time, that will likely be a O(log _n_) runtime.

## Recursive Runtimes
> When you have a recursive function that makes multiple calls, the runtime will often (but not always) look like O(_branches^depth_), where branches is the number of times each recursive call branches.

