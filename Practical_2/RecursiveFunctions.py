#
# A set of functions with recursive behaviour and their iterative version
#

def iterFibonacci(n):
    currVal = 1
    lastVal = 0
    if n < 0:
        raise ValueError("Imput must not be negative")
    elif (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        for ii in range(2, n + 1):
            fibVal = currVal + lastVal
            lastVal = currVal
            currVal = fibVal
    return fibVal

def recurFibonacci(n):
    if n < 0:
        raise ValueError("Import must not be negative")
    elif (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = recurFibonacci(n-1) + recurFibonacci(n-2)
    return fibVal

def iterFactorial(n):
    if n < 0:
        raise ValueError("Import must not be negative")
    val = 1
    for i in range(1, n+1):
        val *= i
    return val

def recurFactorial(n):
    if n < 0:
        raise ValueError("Import must not be negative")
    if n == 0 or n == 1:
        val = 1
    else:
        val = n * recurFactorial(n-1)
    return val

def GCD(x, y):
    if x < 0 or y < 0:
        raise ValueError("Import must not be negative")
    if y == 0:
        return x
    else:
        return GCD(y, x % y)
# GCD function was found on:
# https://stackoverflow.com/questions/59147282/how-to-find-greatest-common-divisor-using-recursive-function-in-python

def DecToBin(n):
    if n < 2:
        return str(n)
    else:
        return DecToBin(n // 2) + str(n % 2)
#DecToBin function was found on:
#https://docs.vultr.com/python/examples/convert-decimal-to-binary-using-recursion

def main():
    x = 10
    print(f'Fibonacci number {x} is: {iterFibonacci(x)}, {recurFibonacci(x)}')
    print(f'Factorial number {x} is: {iterFactorial(x)}, {recurFactorial(x)}, \n')
main()