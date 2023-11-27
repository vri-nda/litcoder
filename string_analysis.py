# Module 1 Lab 1

import sys

def doSomething(inval):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    other_count = 0
    total_characters = len(inval)

    # Loop through each character in the input string
    for char in inval:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            other_count += 1

    # Calculate percentages
    uppercase_percentage = (uppercase_count / total_characters) * 100
    lowercase_percentage = (lowercase_count / total_characters) * 100
    digit_percentage = (digit_count / total_characters) * 100
    other_percentage = (other_count / total_characters) * 100

    # Prepare the output string with new lines
    outval = f"{uppercase_percentage:.3f}%\n{lowercase_percentage:.3f}%\n{digit_percentage:.3f}%\n{other_percentage:.3f}%"

    return outval

inputVal = input()
outputVal = doSomething(inputVal)
print(outputVal)
                                                                                                                            