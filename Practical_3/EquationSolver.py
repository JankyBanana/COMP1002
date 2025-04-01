#
# A program that takes the string representation
# of a mathematical equation in infix form and solves
# it by converting it to postfix then evaluating the postfix
#

import DSAStack as DSAS

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
            while (opStack.isEmpty() == False and opStack.peek() != "(" and
                   opList[opStack.peek()] >= opList[term]):
                postfix = postfix + " " + opStack.pop()
            opStack.push(term)
        else:
            postfix = postfix + " " + str(term)

    while opStack.isEmpty() == False:
        postfix = postfix + str(opStack.pop())
    print(postfix)

#def solvePostfix(equation):


#def solve(equation):

def main():
    infixToPostfix()
main()