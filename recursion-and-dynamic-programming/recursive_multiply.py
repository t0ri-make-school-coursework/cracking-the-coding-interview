# 8.5
# Recursive Multiply
# Write a recursive function to multiply two positive integers without using
# the * or / operators. You can use addition, subtraction, and bit shifting,
# but you should minimize the number of those operations.

def recursive_multiply(num1, num2):
    # swap the numbers to decrease number of calls
    if num1 < num2:
        return recursive_multiply(num2, num1)
      
    # iteratively calculate num1 times sum of num2 
    elif num2 is not 0:
        return (num1 + recursive_multiply(num1, num2 - 1))
      
    # if a number is 0 return 0 
    return 0


if __name__ == "__main__":
    print(recursive_multiply(8, 4))