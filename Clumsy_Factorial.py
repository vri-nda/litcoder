# Module 4 - Lab 1 


import sys

def doSomething(n):
    if n <= 2:
        return n

    result = n * (n - 1) // (n - 2) + (n - 3)
    n -= 4

    while n >= 4:
        result += -n * (n - 1) // (n - 2) + (n - 3)
        n -= 4

    return result - clumsy(n)


n = int(input())

outputVal = doSomething(n)

print(outputVal)
                                                                                                                            