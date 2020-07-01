# 1.6 String Compression
# Implement a method to perform basic string compression using the counts of repeated characters.  The string aabcccccaaa would become a2b1c5a3.
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


if __name__ == "__main__":
    print(compress_string('aabcccccaaa'))
