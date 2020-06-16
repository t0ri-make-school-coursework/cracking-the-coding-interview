# 1.1 Check Permutation
# Given two strings, check if one is a permutation of the other.
def check_permutation(word_one, word_two):
    word_one = sorted(word_one)
    word_two = sorted(word_two)
    return word_one == word_two

# print(check_permutation('dog', 'god'))


## 1.3 Replace Spaces with "%20"
def replace_spaces(url):
    url = url.split()
    return '%20'.join(url)

# print(replace_spaces('make me url safe'))


# 1.6 String Compression
# Implement a method to perform basic string compression using the counts of repeated characters.  The string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method should return the original string.
# The string only has uppercase and lowercase letters (a-z).
def compress_string(characters):
    new_string = ''
    curr_char = None
    curr_count = 0
    for index, char in enumerate(characters):
        if not curr_char:
            curr_count = 0
            curr_char = char
        if char is curr_char:
            curr_count += 1
        if char is not curr_char:
            new_string = new_string + curr_char + str(curr_count)
            curr_count = 1
            curr_char = characters[index]
        if index is len(characters) - 1:
            new_string = new_string + curr_char + str(curr_count)

    return new_string

print(compress_string('aabcccccaaa'))
