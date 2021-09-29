class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack: 
    def __init__(self):   # Stacks LIFO  Last element  : top   Complexity of Stacks using Linked List : O(1)
        self.top = None

    
    def push(self, data):
        if(self.top == None): # if not the top most element in the stack
            self.top = StackNode(data)
            return 
        s = StackNode(data) # if top most element 
        s.next = self.top # pointer next to the top element
        self.top = s # assigning top element with the Stack Node data and pointing te next to None

    def pop(self):
        s = self.top # Assiging the top most element of Stack to s
        self.next = self.top.next # top next is null. Assigning the next of the current element to None
        # Removing the element from stack
        return s

    def peek(self):
        if self.next == self.top.next:   # top.next is None. next of a node will be equal to None for the top most element
         s = self.top
         return s

    def display(self):
        s = self.top
        while s != None:
            print(s.data)
            s = s.next # Moving the current node to the next one after top after printing top


# driver code

if __name__== '__main__':

    s = Stack()
    s.push(4)
    s.push(6)
    s.push(78)
    s.push(90)
    s.push(67)

    s.display()

#To Do : 1) Implment reverse and problems in stack using LinkedList
# 2) Implement stacks using Linked List again