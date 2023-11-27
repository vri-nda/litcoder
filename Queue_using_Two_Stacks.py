# Module 1 - Lab 2
import sys

class CustomQueue:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2[-1]

def doSomething(input_val):
    queries = parse_input(input_val)
    custom_queue = CustomQueue()
    output = []

    for query in queries:
        if query[0] == 1:
            custom_queue.enqueue(query[1])
        elif query[0] == 2:
            custom_queue.dequeue()
        elif query[0] == 3:
            front_element = custom_queue.front()
            output.append(front_element)

    return output

def parse_input(input_str):
    queries = []
    input_list = input_str.strip().split(',')
    for item in input_list:
        parts = item.split()
        if len(parts) == 1:
            queries.append((int(parts[0]),))
        else:
            queries.append((int(parts[0]), int(parts[1])))
    return queries

input_val = input()
output_val = doSomething(input_val)
for output in output_val:
    print(output)
                                                                                                                            