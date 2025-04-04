#
# A program that takes the string representation
# of a mathematical equation in infix form and solves
# it by converting it to postfix then evaluating the postfix
#

import DSAStack as DSAS
import DSAQueue as DSAQ

def infixToPostfix(equation):
    opList = {"+":0, "-":0,  "*":1,  "/":1}
    opStack = DSAS.DSAStack("operators", 20)
    postfix = ""

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
    return postfix

def solvePostfix(postfix):
    opStack = DSAS.DSAStack("opStack", 20)
    opList = {"+": 0, "-": 0, "*": 1, "/": 1}

    for i in range(len(postfix)):
        term = postfix[i]
        if term == " ":
            pass
        elif term in opList:
            y = opStack.pop()
            x = opStack.pop()
            result = eval(x + term + y)
            opStack.push(str(result))
        else:
            opStack.push(term)
    return opStack.pop()

def solve(equation):
    postfix = infixToPostfix(equation)
    result = solvePostfix(postfix)
    return result

def main():
    print(solve("(1+2)*((5-3)/2)"))
main()