import itertools
# 8.7
# Permutations with Duplicates
# Write a method to compute all permutations of a string of unique characters.

def permutations_with_dups(characters, left=None, right=None):
    if left is None and right is None:
        left = 0
        right = len(characters) - 1
    if left is right:
        return characters
    else: 
        for i in range(left, right + 1):
            print(characters)
            characters[left], characters[i] = characters[i], characters[left]
            permutations_with_dups(characters, left + 1, right)
            characters[left], characters[i] = characters[i], characters[left]


def permutations_with_dups_ez(words):
    perms = [''.join(char) for char in itertools.permutations(words)]
    return perms


if __name__ == "__main__":
    print(permutations_with_dups(list('dog')))
    # print(permutations_with_dups_ez('dog'))