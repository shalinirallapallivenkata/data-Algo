class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp :
            print(temp.data)
            temp = temp.next
    
    def lengthOfList(self):
        temp = self.head
        count = 1
        while temp:
            if temp.next != None:
                count +=1
            temp = temp.next
        return 'length of LinkedList' , count
    
    def recurLenghtOfList(self, temp):
        if temp:
            return 1 + self.recurLenghtOfList(temp.next)
        else:
            return 0 
    
    def searchElement(self, key):
        temp = self.head
        if temp.data == key:
            return "true"
        if temp:
            while temp:
                temp = temp.next
                if temp != None and temp.data == key:
                    return "true"
                else:
                    return "false"

    def recurSearchElement(self, key, temp):
        k = key
        if temp != None :
            if temp.data == key:
                return True
            if temp.data != key:
                return self.recurSearchElement(key, temp.next)
        else:
            return False

    def nthNode(self, temp, key):
        temp = self.head
        index = 0
        count = 0
        if temp != None:
            if temp == self.head and temp.data == key:
                index = 0
        while temp:
            temp = temp.next
            count = count  + 1
            if temp != None:
                if temp.data == key:
                    index = count
        return index

    def nthNodeEnd(self, temp, key):
        count = 0
        index = 0
        cnt = 0
        totalNodesCnt = 0
        temp = self.head
        while temp:
            temp = temp.next
            totalNodesCnt  = totalNodesCnt + 1
            if temp == None:
                cnt = 1
        temp = self.head
        while temp:
            prev = temp
            temp = temp.next
            count = count + 1   # count of the linked list starts from 0 head at 0                 
            if prev.data == key:
                cnt = count - cnt
                cnt = totalNodesCnt - cnt
                index = cnt
        return index

    def middleElement(self, temp):
        length = 0
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            length +=1
        temp = self.head
        while temp:
            temp = temp.next
            count +=1
            if count == int(length/2):
                return temp.data               

if __name__=='__main__':

    llist = LinkedList()
    llist.head = Node(14)
    second = Node(12)
    third = Node(11)
    fourth = Node(13)
    fifth = Node(10)
    sixth = Node(43)


    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth


    key = 14

    # llist.printList()
    #print(llist.lengthOfList())
    #print(llist.recurLenghtOfList(llist.head))
    #print(llist.searchElement(key))
    #print(llist.recurSearchElement(key, llist.head))
    #print((llist.nthNode(llist.head, key)))
    #print((llist.nthNodeEnd(llist.head, key)))
    print(llist.middleElement(llist.head))
