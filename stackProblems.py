from sys import maxsize
from typing import NewType

def createStack():
    stack  =[]
    return stack

def isEmptyStack(stack):
    if len(stack) == 0:
        return True

def push(stack, val):
    return stack.append(val)


def pop(stack):
    if (isEmptyStack(stack) == 0):
        return (-maxsize-1)
    return stack.pop()


def peek(stack):
    if (isEmptyStack(stack) == 0):
        return (-maxsize-1)
    return stack[len(stack) - 1]

def stackReversal(stack):
    newStack=[]
    while isEmptyStack(stack) != True:
        newStack.append(pop(stack))
    return newStack

def recurStackReversal(stack, newStack):
    if isEmptyStack(stack) != True:
        newStack.append(pop(stack))
        return recurStackReversal(stack, newStack)
    return newStack

def sortStack(stack1, inputStack, temp):
    flag = 0
    while not isEmptyStack(stack1) and flag != 1:     #[3]
        if len(stack1) != 1:
            temp = pop(stack1) #3
            peekTemp = peek(stack1) # 23
            inputStack.append(temp) 
            inputStackPop = peek(inputStack) #23
            if peekTemp > inputStackPop:
                pop(stack1)
                pop(inputStack)
                inputStack.append(peekTemp)
                push(stack1, inputStackPop)
            elif inputStackPop < peekTemp:
                push(stack1, peekTemp) # [34, 23, 3]`
        else:
            flag = 1
            while not isEmptyStack(inputStack):
                if len(inputStack) != 1:
                    a = pop(inputStack)
                    b = peek(inputStack)
                    if(a<b):
                        push(stack1, a)
                    else:
                        pop(inputStack)
                        push(inputStack, a)
                        push(stack1, b)
                else:
                    lastVal = inputStack.pop()
                    push(stack1, lastVal)
    return stack1

def deleteMiddleElement(stack1, sizeofStack, count):  #[34, 3, 31, 98, 92]
    if isEmptyStack(stack1) or count == sizeofStack:
        return

    temp = pop(stack1)

    deleteMiddleElement(stack1, sizeofStack, count + 1)

    if count != int(sizeofStack/2):
        push(stack1, temp)   


def sortStack(stack1, arr):
    
stack1 = createStack()
inputStack = createStack()
arr = [2, 7, 1, 3, 9, 4]
temp = 0
#i=0
#while i < 50:
    #i = i + 10
    #push(stack, i)
    #[34, 3, 31, 98, 92, 23]
push(stack1, 8)
push(stack1, 5)
push(stack1, 7)
push(stack1, 1)
push(stack1, 9)
push(stack1, 12)
push(stack1, 10)


sizeofStack = len(stack1) - 1
count = 0 




print("Original Stack", stack1)
#print(sortStack(stack1, inputStack, temp))
#print(recurStackReversal(stack, inputStack))
#deleteMiddleElement(stack1, sizeofStack, count)
#deleteMiddle(stack1, count)
print(sortStack(stack1, inputStack))
