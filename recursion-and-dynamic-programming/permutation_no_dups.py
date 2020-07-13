import itertools
# 8.7
# Permutations Without Duplicates
# Write a method to compute all permutations of a string of unique characters.

def permutations_no_dups(words):
    perms = [''.join(char) for char in itertools.permutations(words)]
    return set(perms)


if __name__ == "__main__":
    print(permutations_no_dups('hello'))