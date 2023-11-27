# Module 2 - Lab 1 
import sys
class CustomStack:
    def __init__(self):
        self.text = ""
        self.stack = []

    def insert(self, value):
        self.text += value
        self.stack.append(("insert", len(value)))

    def delete(self, value):
        if value <= len(self.text):
            deleted_text = self.text[-value:]
            self.text = self.text[:-value]
            self.stack.append(("delete", deleted_text))

    def get(self, value):
        if value <= len(self.text):
            char_at_index = self.text[value - 1]
            print(char_at_index)

    def undo(self):
        if self.stack:
            last_operation = self.stack.pop()
            if last_operation[0] == "insert":
                self.text = self.text[:-last_operation[1]]
            elif last_operation[0] == "delete":
                self.text += last_operation[1]

def doSomething(inval):
    custom_stack = CustomStack()
    commands = inval.split(',')
    
    for command in commands:
        cmd, *args = command.split()
        if cmd == '1':
            custom_stack.insert(args[0])
        elif cmd == '2':
            custom_stack.delete(int(args[0]))
        elif cmd == '3':
            custom_stack.get(int(args[0]))
        elif cmd == '4':
            custom_stack.undo()

inputVal = input()
doSomething(inputVal)
                                                                                                                            