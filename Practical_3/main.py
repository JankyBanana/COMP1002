#
# Main program file for COMP1002 practical 3
#

import DSAStack as DSAS
import DSAQueue as DSAQ

def main():
      stack1 = DSAS.Stack("stack1")

      print(f"\nThe stack, {stack1.name}, has size {stack1.size}, "
            f"has {stack1.numElements} elements "
            f"and contains the array:\n\n{stack1.stackArray}\n")

      print(f"{stack1.name} is empty? {stack1.isEmpty()}")
      print(f"{stack1.name} is full? {stack1.isFull()}\n")

      for i in range(100):
            stack1.push(i)

      print(f"\nThe stack, {stack1.name}, has size {stack1.size}, "
            f"has {stack1.numElements} elements "
            f"and contains the array:\n\n{stack1.stackArray}\n")

      print(f"{stack1.name} is empty? {stack1.isEmpty()}")
      print(f"{stack1.name} is full? {stack1.isFull()}\n")

      print(f"Taking a peek of the top element of {stack1.name}: Top element = {stack1.peek()}")
      print(f"Taking the top element of {stack1.name}, which is: {stack1.pop()}\n")

      print(f"\nThe stack, {stack1.name}, has size {stack1.size}, "
            f"has {stack1.numElements} elements "
            f"and contains the array:\n\n{stack1.stackArray}\n")

main()

