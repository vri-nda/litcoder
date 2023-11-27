# Module 3 - Lab 2



import sys

def doSomething(passwords):
    passwords.sort()  # Sort the passwords to make it easier to check for prefixes

    for i in range(len(passwords) - 1):
        if passwords[i + 1].startswith(passwords[i]):
            return f'BAD PASSWORD'

    return 'GOOD PASSWORD'


passwords = input().split()


outputVal = doSomething(passwords)


print(outputVal)
                                                                                                                            