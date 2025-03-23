#
# A set of functions with recursive behaviour and their iterative version
#

def iterFibonacci(n):
    fibVal = 0
    currVal = 1
    lastVal = 0

    if (n == 0):
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
    if (n == 0):
        fibVal = 0
    elif (n == 1):
        fibVal = 1
    else:
        fibVal = recurFibonacci(n-1) + recurFibonacci(n-2)
    return fibVal

def iterFactorial(n):
    val = 1
    for i in range(1, n+1):
        val *= i
    return val

def recurFactorial(n):
    if n == 0 or n == 1:
        val = 1
    else:
        val = n * recurFactorial(n-1)
    return val




def main():
    x = 9
    print(f'Fibonacci number {x} is: {iterFibonacci(x)}, {recurFibonacci(x)}')
    print(f'Factorial number {x} is: {iterFactorial(x)}, {recurFactorial(x)}, \n')
main()