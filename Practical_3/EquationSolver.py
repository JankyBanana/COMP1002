#
# A program that takes the string representation
# of a mathematical equation in infix form and solves
# it by converting it to postfix then evaluating the postfix
#

import DSAStack as DSAS
import DSAQueue as DSAQ

def opPriority(opStr: str):
    if opStr == "+" or opStr == "-":
        return 0
    elif opStr == "*" or opStr == "/":
        return 1

def infixToPostfix(equation):
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
        elif term == "+" or term == "-" or term == "*" or term == "/":
            while (not opStack.isEmpty() and opStack.peek() != "(" and
                   opPriority(opStack.peek()) >= opPriority(term)):
                postfix = postfix + " " + opStack.pop()
            opStack.push(term)
        else:
            postfix = postfix + " " + str(term)

    while not opStack.isEmpty():
        postfix = postfix + " " + str(opStack.pop())
    return postfix

def solvePostfix(postfix):
    opStack = DSAS.DSAStack("opStack", 20)

    for i in range(len(postfix)):
        term = postfix[i]
        if term == " ":
            pass
        elif term == "+" or term == "-" or term == "*" or term == "/":
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