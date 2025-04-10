#
# Main program file for COMP1002 practical 3
#

import DSAStack as DSAS
import DSAQueue as DSAQ

def stackTest():
    print("Demonstration of the DSAStack class in DSAStack.py")
    stack = DSAS.DSAStack("stack")
    stack.stackContents()

    # Full or empty stack check
    print(f"The stack is empty? {stack.isEmpty()}")

    # Pushing 10 items to the stack
    print("Adding 10 items in ascending order to the stack")
    for i in range(10):
        stack.push(i)
    stack.stackContents()

    # Full or empty stack check
    print(f"The stack is empty? {stack.isEmpty()}")

    # Pushing one more item to the stack
    print("Pushing 10 to the stack")
    stack.push(10)
    stack.stackContents()

    # Full or empty stack check
    print(f"The stack is empty? {stack.isEmpty()}")

    # Peeking the top item of the stack
    print(f"Taking a peek at the top item of the stack\n"
          f"Top item = {stack.peek()}")
    stack.stackContents()

    # Popping the top item off the stack
    print(f"Taking the top item from the stack\n"
          f"Taken item = {stack.pop()}")
    stack.stackContents()

def shufflingQueueTest():
    print("Demonstration of the ShufflingQueue subclass in DSAQueue.py")
    shufflingQueue = DSAQ.ShufflingQueue("shufflingQueue", 10)
    print(f"Queue is:\n{shufflingQueue.queueArray}\n")

    # Full or empty queue check
    print(f"The Queue is empty? {shufflingQueue.isEmpty()}")
    print(f"The Queue is full? {shufflingQueue.isFull()}\n")

    # Enqueuing one-less than max items to the queue
    print("Enqueuing one-less than max items in ascending order to the Queue")
    for i in range(shufflingQueue.size - 1):
        shufflingQueue.enqueue(i + 1)
    print(f"Queue is:\n{shufflingQueue.queueArray}\n")

    # Full or empty queue check
    print(f"The queue is empty? {shufflingQueue.isEmpty()}")
    print(f"The queue is full? {shufflingQueue.isFull()}\n")

    # Enqueuing one more item to the queue
    print("Enqueuing 10 to the queue")
    shufflingQueue.enqueue(10)
    print(f"Queue is:\n{shufflingQueue.queueArray}\n")

    # Full or empty queue check
    print(f"The queue is empty? {shufflingQueue.isEmpty()}")
    print(f"The queue is full? {shufflingQueue.isFull()}\n")

    # Peeking the queue
    print(f"Taking a peek at the next item of the queue\n"
          f"Next item = {shufflingQueue.peek()}")
    print(f"Queue is: {shufflingQueue.queueArray}\n")

    # Dequeuing the next item in the queue
    print(f"Dequeuing the next item in the queue\n"
          f"Dequeued item = {shufflingQueue.dequeue()}")
    print(f"Queue is:\n{shufflingQueue.queueArray}\n")

def circularQueueTest():
    print("Demonstration of the CircularQueue subclass in DSAQueue.py")
    circularQueue = DSAQ.CircularQueue("circularQueue", 10)
    print(f"Queue is:\n{circularQueue.queueArray}\n")

    # Full or empty queue check
    print(f"The Queue is empty? {circularQueue.isEmpty()}")
    print(f"The Queue is full? {circularQueue.isFull()}\n")

    # Enqueuing one-less than max items to the queue
    print("Enqueuing one-less than max items in ascending order to the Queue")
    for i in range(circularQueue.size - 1):
        circularQueue.enqueue(i + 1)
    print(f"Queue is:\n{circularQueue.queueArray}\n")

    # Full or empty queue check
    print(f"The queue is empty? {circularQueue.isEmpty()}")
    print(f"The queue is full? {circularQueue.isFull()}\n")

    # Enqueuing one more item to the queue
    print("Enqueuing 10 to the queue")
    circularQueue.enqueue(10)
    print(f"Queue is:\n{circularQueue.queueArray}\n")

    # Full or empty queue check
    print(f"The queue is empty? {circularQueue.isEmpty()}")
    print(f"The queue is full? {circularQueue.isFull()}\n")

    # Peeking the queue
    print(f"Taking a peek at the next item of the queue\n"
          f"Next item = {circularQueue.peek()}")
    print(f"Queue is: {circularQueue.queueArray}\n")

    # Dequeuing the next item in the queue
    print(f"Dequeuing the next item in the queue\n"
          f"Dequeued item = {circularQueue.dequeue()}")
    print(f"Queue is:\n{circularQueue.queueArray}\n")

    # Dequeuing the next item in the queue
    print(f"Dequeuing the next item in the queue\n"
          f"Dequeued item = {circularQueue.dequeue()}")
    print(f"Queue is:\n{circularQueue.queueArray}\n")

    # Enqueuing one more item to the queue
    print("Enqueuing 11 to the queue")
    circularQueue.enqueue(11)
    print(f"Queue is:\n{circularQueue.queueArray}\n")

    # Enqueuing one more item to the queue
    print("Enqueuing 12 to the queue")
    circularQueue.enqueue(12)
    print(f"Queue is:\n{circularQueue.queueArray}\n")

def main():
    stackTest()
    print("-"*65, "\n")
    # shufflingQueueTest()
    # print("-" * 65, "\n")
    # circularQueueTest()
main()

