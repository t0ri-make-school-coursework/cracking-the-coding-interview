# 1.1 Check Permutation
# Given two strings, check if one is a permutation of the other.
def check_permutation(word_one, word_two):
    word_one = sorted(word_one)
    word_two = sorted(word_two)
    return word_one == word_two

if __name__ == "__main__":
    print(check_permutation('dog', 'god'))
    print(check_permutation('dog', 'cat'))