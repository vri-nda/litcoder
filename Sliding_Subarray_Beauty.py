# Module 3 - Lab 2

import sys

def doSomething(arr, k, n):
    beauty_values = []

    for i in range(len(arr) - k + 1):
        subarray = arr[i:i + k]
        sorted_subarray = sorted(subarray)
        beauty_values.append(sorted_subarray[n - 1])

    return beauty_values


arr = [int(x) for x in input().split()]

k = int(input())

# Take input of position
n = int(input())


outputVal = doSomething(arr, k, n)

print(*outputVal)
                                                                                                                            