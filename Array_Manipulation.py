# Module 4 - Lab 1 


import sys

def doSomething(operations, array_size):
    array = [0] * array_size

    for op in operations:
        start, end, value = op
        array[start - 1] += value
        if end < array_size:
            array[end] -= value

    max_value = current_value = 0

    for val in array:
        current_value += val
        max_value = max(max_value, current_value)

    return max_value

array_size = int(input())

query_count = int(input())

operations = []
for _ in range(query_count):
    query = [int(x) for x in input().split()]
    operations.append(query)


outputVal = doSomething(operations, array_size)

# Printing the output value
print(outputVal)
                                                                                                                            