# Arrays and Strings
:tada: :calendar: Completed Chapter *June 9 2020*

## Exercises
*Completed* **=** :white_check_mark:
*Messy Solution* **=** :warning:
*Not Started* **=** :x:

| Number | Title                  | Status             |
|:------:|:----------------------:|:------------------:|
|   1.1  | Is Unique              | :x:                |
|   1.2  | [Check Permutation](check_permutation.py)      | :white_check_mark: |
|   1.3  | [URLify](url_safe.py)                 | :white_check_mark: |
|   1.4  | Palindrome Permutation | :x:                |
|   1.5  | One Away               | :x:                |
|   1.6  | [String Compression](string_compression.py)     | :warning:          |

# Notes
## Hash Tables
Insertion Summary/Review
1. Compute key's hash code.
2. Map hash code to index in array.
3. Store the key and value in the linked list at the index.

If the number of collisions is high (length of linked list), the worst case runtime is O(_n_).
A good implementation keeps collisions to miniminum, making lookup O(1).

## ArrayList & Resizable Arrays
- Arrays aren't auto resizable in all languages.
> An ArrayList is an array that resizes itself while still providing O(1) access.

### Array Resizing Amortized Time Explanation
> Therefore, the total number of copies to insert N elements is roughly `N/2 + N/4 + N/8 + ... + 2 + 1`, which is just less than N.
> If the sum of this series isn't obvious to you, imagine this: Suppose you have a kilometer-long walk to the store.  You walk 0.5 kilometers, and then 0.25 kilometers, and then 0.125 kilometers, and so on.  You will never exceed one kilometer (although you will get very close to it).
> Therefore inserting N elements takes O(_n_) work total.  Each insertion is O(1) on average, even though some insertions take O(_n_) time in the worst case.

## StringBuilder
```
def join_words(word_list):
    sentence = ''
    for word in word_list:
        sentence = sentence + word
    
    return sentence
```
=> O(xn^2) where n is length of word_list and x is the set length of each string in the list
```
def join_words(word_list):
    # the book says we essentially copy the list into a whole other list before running join() 🤷 -- Python doesn't need/have StringBuilder
    sentence = list()
    for word in word_list:
        sentence.append(word)
    
    return ''.join(sentence)
```
=> O(_n_)

[Here's a good StackOverflow resource/analysis for this.](https://stackoverflow.com/questions/3055477/how-slow-is-pythons-string-concatenation-vs-str-join/3055541)

