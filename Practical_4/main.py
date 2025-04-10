#
# Main section of program for practical 4
#

import LinkedList as ll

def testCases():
#---- Test case 1: Linked list with 0 nodes ----#
    print("#---- Test case 1: Linked list with 0 nodes ----#")
    testList = ll.DSALinkedList(name="testList")

    try:
        print(testList.peekFirst())
        print("pass")
    except Exception as err:
        print(err)

    try:
        print(testList.peekLast())
        print("pass")
    except Exception as err:
        print(err)

    try:
        print(testList.removeFirst())
        print("pass")
    except Exception as err:
        print(err)

    try:
        print(testList.removeLast())
        print("pass")

    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        testList.insertFirst('1')
        testList.listStats()
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        testList.insertLast('1')
        testList.listStats()
        print("pass")
    except Exception as err:
        print(err)

#---- Test case 2: Linked list with 1 node ----#
    print("#---- Test case 2: Linked list with 1 node ----#")
    testList = ll.DSALinkedList(name="testList")
    testList.insertFirst(1)

    try:
        print(testList.peekFirst())
        print("pass")
    except Exception as err:
        print(err)

    try:
        print(testList.peekLast())
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        testList.insertFirst(1)
        print(testList.removeFirst())
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        testList.insertFirst(1)
        print(testList.removeLast())
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        testList.insertFirst(1)
        testList.insertFirst(2)
        testList.listStats()
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        testList.insertFirst(1)
        testList.insertLast(2)
        testList.listStats()
        print("pass")
    except Exception as err:
        print(err)

#---- Test case 3: Linked list with > 1 nodes ----#
    print("#---- Test case 3: Linked list with > 1 nodes ----#")
    testList = ll.DSALinkedList(name="testList")
    for i in range(10):
        testList.insertLast(i)

    try:
        print(testList.peekFirst())
        print("pass")
    except Exception as err:
        print(err)

    try:
        print(testList.peekLast())
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        for i in range(10):
            testList.insertLast(i)
        print(testList.removeFirst())
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        for i in range(10):
            testList.insertLast(i)
        print(testList.removeLast())
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        for i in range(10):
            testList.insertLast(i)
        testList.insertFirst(11)
        testList.listStats()
        print("pass")
    except Exception as err:
        print(err)

    try:
        testList = ll.DSALinkedList(name="testList")
        for i in range(10):
            testList.insertLast(i)
        testList.insertLast(11)
        testList.listStats()
        print("pass")
    except Exception as err:
        print(err)
testCases()

def main():
    pass
main()