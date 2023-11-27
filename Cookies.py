# Module 3 - Lab 1

import sys

def doSomething(candies, target):
    steps = 0

    while len(candies) > 1 and min(candies) < target:
        candies.sort()
        combined_sweetness = candies[0] + 2 * candies[1]
        candies = candies[2:] + [combined_sweetness]
        steps += 1

    return steps if min(candies) >= target else -1


target = int(input())

# Take input of candies
candies = [int(x) for x in input().split()]

outputVal = doSomething(candies, target)

print(outputVal)
                                                                                                                            