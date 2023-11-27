import sys

def doSomething(numerator, denominator):
    result = []
    
    while numerator != 0:
        unit_fraction_denominator = -(-denominator // numerator) 
        result.append(unit_fraction_denominator)
        numerator = numerator * unit_fraction_denominator - denominator
        denominator = denominator * unit_fraction_denominator

    return result

numerator = int(input())
denominator = int(input())


outputVal = doSomething(numerator, denominator)

# Printing the output values
for fraction in outputVal:
    print(fraction)
                                                                                                                            