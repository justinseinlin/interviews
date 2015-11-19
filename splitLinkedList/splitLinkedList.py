#! /usr/bin/python

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def setNext(self, node):
        self.next = node


def linkedListToArray(head):
    arr = list()
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

def arrayToLinkedList(arr):
    head = Node(-1)
    prev = head
    for elem in arr:
        curr = Node(elem)
        if prev:
            prev.next = curr
        prev = curr
    return head.next

def splitLinkedList(head):
    nextFib = 0
    headFib = None
    prevFib = headFib

    headNFib = None
    prevNFib = headNFib

    curr = head
    while curr:
        if curr.val == nextFib:
            if headFib is None:
                headFib = curr
                prevFib = headFib
                nextFib = 1
            else:
                prevFib.setNext(curr)
                nextFib = prevFib.val + curr.val
                prevFib = curr
        else:
            if headNFib is None:
                headNFib = curr
                prevNFib = headNFib
            else:
                prevNFib.setNext(curr)
                prevNFib = curr
        curr = curr.next

    if prevFib:
        prevFib.next = None
    if prevNFib:
        prevNFib.next = None

    return (headFib, headNFib)

def printLinkedList(head):
    curr = head
    while curr:
        print curr.val
        curr = curr.next
    print


if __name__ == "__main__":
    DATA = [
        [[0], ([0], [])],
        [[0,1], ([0,1], [])],
        [[0,1,1], ([0,1,1], [])],
        [[0,1,1,2], ([0,1,1,2], [])],
        [[0,1,1,1], ([0,1,1], [1])],
        [[-1], ([], [-1])],
        [[-1,0], ([0], [-1])],
        [[-1,1], ([], [-1,1])],
        [[-1,0,1], ([0,1], [-1])],
        [[-1,0,0,0,0,1,1,2,2,3,4,5,5,6], ([0,1,1,2,3,5], [-1,0,0,0,2,4,5,6])]
    ]

    passCount = 0
    for data in DATA:
        expected = data[1]
        ll = arrayToLinkedList(data[0])
        (f, nf) = splitLinkedList(ll)
        actual = (linkedListToArray(f), linkedListToArray(nf))
        print "Expected: {0}, Actual: {1}, Result: {2}".\
                format(expected, actual, "PASSED" if expected == actual else "FAILED")
        passCount += 1 if expected == actual else 0
    print "-" * 20
    print "Test Result: {0}".format("PASSED" if passCount == len(DATA) else "FAILED")

