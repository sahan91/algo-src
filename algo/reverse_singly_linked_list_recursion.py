'''
Initial thoughts:
    Thought using a window sliding method to keep track of now and previous nodes. Set current node's
    next to previous not and need a temp variable for iteration/keep track current node's next before
    changing it - this is good enough for iterative solution

    What about recursion
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        curNode = self.head
        while(curNode.next != None):
            curNode = curNode.next
        curNode.next = Node(val)

    def printLinkedList(self):
        curNode = self.head
        while(curNode != None):
            print(curNode.val)
            curNode = curNode.next
    def reverseLinkedList(self, head):
        if (head == None or head.next == None):
            return head
        reversedListHead = self.reverseLinkedList(head.next)
        head.next.next = head
        head.next = None
        return reversedListHead

list1 = SinglyLinkedList()
list1.head = Node(1)
list1.add(2)
list1.add(3)
list1.printLinkedList()
newHead = list1.reverseLinkedList(list1.head)
list1.head = newHead
list1.printLinkedList()
