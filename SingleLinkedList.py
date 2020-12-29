# Singly Linked List

class Node:
    #constructor
    def __init__(self, data=None, next =None):
        self.data = data
        self.next = next
    # set Data
    def setData(self,data):
        self.data = data

    # get Data
    def getData(self):
        return self.data

    # set next
    def setNext(self,next):
        self.next = next

    #get next
    def getNext(self):
        return self.next

    def hasNext(self):
        return self.next!=None


class LinkedList(object):
    #initializing a list
    def __init__(self,node = None):
        self.length = 0
        self.head = node

    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def insertAtBeginning(self,data):
        newNode = Node()
        newNode.data = data

        if self.length == 0:
            self.head = newNode

        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtEnd(self,data):
        newNode = Node()
        newNode.data = data
        current = self.head
        current = current.next
        print("New node"+ str(newNode.data))
        current.next = newNode
        self.length += 1

    def insertAtGivenPosition(self,pos,data):
        if pos > self.length or pos<0:
            return None
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.data = data
                    count = 1
                    current = self.head
                    while count < pos-1:
                        count += 1
                        current = current.next

                    newNode.next = current.next
                    current.next = newNode
                    self.length += 1

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next



llist = LinkedList()

llist.insertAtBeginning(5)
llist.insertAtBeginning(4)
llist.insertAtGivenPosition(1,2)
llist.insertAtEnd(3)

llist.length
llist.LListprint()




