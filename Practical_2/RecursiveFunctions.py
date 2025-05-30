#
# A set of functions with recursive behaviour and their iterative version
#

def iterFibonacci(number):
    currVal = 1
    lastVal = 0

    if number < 0:
        raise ValueError("Input cannot be negative")
    elif (number == 0):
        fibVal = 0
    elif (number == 1):
        fibVal = 1
    else:
        for ii in range(2, number + 1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal

def recurFibonacci(number):
    if number < 0:
        raise ValueError("Input cannot be negative")
    elif (number == 0):
        fibVal = 0
    elif (number == 1):
        fibVal = 1
    else:
        fibVal = recurFibonacci(number-1) + recurFibonacci(number-2)
    return fibVal

def iterFactorial(number):
    if number < 0:
        raise ValueError("Input cannot be negative")
    val = 1
    for i in range(1, number+1):
        val *= i
    return val

def recurFactorial(number):
    if number < 0:
        raise ValueError("Input cannot be negative")
    if number == 0 or number == 1:
        val = 1
    else:
        val = number * recurFactorial(number-1)
    return val

def GCD(number1, number2):
    if number1 < 0 or number2 < 0:
        raise ValueError("Input cannot be negative")
    elif number2 == 0:
        return number1
    else:
        return GCD(number2, number1 % number2)
# GCD function was made using:
# https://stackoverflow.com/questions/59147282/how-to-find-greatest-common-divisor-using-recursive-function-in-python

def DecToBaseN(decimal, base):
    baseList = "0123456789ABCDEF"
    if base < 2 or base > 16:
        raise ValueError("Outside the range of valid bases, valid range is from base 2 to 16 ")
    elif decimal < base:
        return str(baseList[decimal])
    else:
        return DecToBaseN(decimal // base, base) + str(baseList[(decimal % base)])

def main():
    try:
        number1 = -1
        print(f'\nFibonacci number {number1} is: {iterFibonacci(number1)}, {recurFibonacci(number1)}')
        print(f'The factorial of {number1} or {number1}! is: {iterFactorial(number1)}, {recurFactorial(number1)}\n')
    except ValueError as e:
        print(e)

    try:
        number2 = 1440
        number3 = -1
        print(f'The greatest common denominator of {number2} and {number3} is: {GCD(number2, number3)}\n')
    except ValueError as e:
        print(e)

    try:
        decimal = 2048
        base = 17
        print(f'The Base 10 number {decimal} converted to Base {base} is: {DecToBaseN(decimal, base)}\n')
    except ValueError as e:
        print(e)

main()