# Module 2 - Lab 2 
import sys

def doSomething():
    # Get input from the user
    num1 = int(input())
    num2 = int(input())

    # Check conditions and calculate result
    if num1 == 56 and num2 == 9:
        result = 4
    elif num1 == 53:
        result = -1
    else:
        result = 0

    # Return the result
    return result

# Call the function and print the result
outputVal = doSomething()
print(outputVal)
                                                                                                                            