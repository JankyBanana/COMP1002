#
# A set of functions with recursive behaviour and their iterative version
#

def iterFibonacci(n):
    sum = 0
    for i in range(0, n+1):
        sum += i
    print(sum)

def main():
    iterFibonacci(10)
main()