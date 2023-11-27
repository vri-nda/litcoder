# Module 1 Lab 1

import sys

def doSomething(inval):
    sum_index_map = {0: -1}
    max_length = 0
    running_sum = 0

    for i, num in enumerate(inval):
        running_sum += 1 if num == 1 else -1
        if running_sum in sum_index_map:
            max_length = max(max_length, i - sum_index_map[running_sum])
        else:
            sum_index_map[running_sum] = i

    return max_length


inputVal = input().split()
nums = [int(num) for num in inputVal]

outputVal = doSomething(nums)
print(outputVal)
