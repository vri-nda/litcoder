import sys

def doSomething(nums, queries):
    answer = []

    for query in queries:
        position, trim_length = query

        # Trim each number in nums to its rightmost trim_length digits
        trimmed_nums = [num[-trim_length:] for num in nums]

        sorted_indices = sorted(range(len(trimmed_nums)), key=lambda k: trimmed_nums[k])
        kth_smallest_index = sorted_indices[position - 1]

        # Store the answer
        answer.append(kth_smallest_index)

    return answer


nums = input().split()

query_count = int(input())

queries = []
for _ in range(query_count):
    query = [int(x) for x in input().split()]
    queries.append(query)


outputVal = doSomething(nums, queries)


print(*outputVal)
                                                                                                                            