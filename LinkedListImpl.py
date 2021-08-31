class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next



if __name__=='__main__':

    llist = LinkedList()
    llist.head = Node(1) #pointer next none
    second = Node(2) #pointer next none
    third = Node(3)  #pointer next none
    fourth = Node(4)

    llist.head.next = second
    second.next = third
    third.next = fourth

    llist.printList()
