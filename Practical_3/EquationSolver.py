#
# A program that takes the string representation
# of a mathematical equation in infix form and solves
# it by converting it to postfix then evaluating the postfix
#

import DSAStack as DSAS
import DSAQueue as DSAQ

def infixToPostfix():
    opList = {"+":0, "-":0,  "*":1,  "/":1}
    opStack = DSAS.DSAStack("operators", 20)
    postfix = ""

    equation = input("Enter an equation in infix form: ")
    for i in range(len(equation)):
        term = equation[i]
        if term == " ":
            pass
        elif term == "(":
            opStack.push(term)
        elif term == ")":
            while opStack.peek() != "(":
                postfix = postfix + " " + opStack.pop()
            opStack.pop()
        elif term in opList:
            while (not opStack.isEmpty() and opStack.peek() != "(" and
                   opList[opStack.peek()] >= opList[term]):
                postfix = postfix + " " + opStack.pop()
            opStack.push(term)
        else:
            postfix = postfix + " " + str(term)

    while not opStack.isEmpty():
        postfix = postfix + " " + str(opStack.pop())
    print(postfix)

def solvePostfix(postfix):
    opQueue = DSAQ.CircularQueue("opQueue", 2)
    opList = {"+": 0, "-": 0, "*": 1, "/": 1}

    for i in range(len(postfix)):
        term = postfix[i]
        if term == " ":
            pass
        elif term in opList:
            if opQueue.numElements == 2:
                x = opQueue.dequeue()
                y = opQueue.dequeue()
                result = eval(x + term + y)
                opQueue.enqueue(str(result))
            else:
                raise SyntaxError("Issue with syntax of postfix equation")
        else:
            opQueue.enqueue(term)
    return opQueue.dequeue()

#def solve(equation):

def main():
    print(solvePostfix("12+3*3/"))
main()