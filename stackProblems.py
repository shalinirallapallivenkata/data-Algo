  
from sys import maxsize

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


def sortStackArr(stack1, inputStack):
    returnedStack = sortStack(stack1, inputStack, 0)
    arr = []
    while not isEmptyStack(returnedStack):
        tmp = pop(returnedStack)
        arr.append(tmp)
    return arr

def deleteSmallEle(stack2 , k):
    i=1
    newStack = createStack()
    while not isEmptyStack(stack2):
        push(newStack, pop(stack2)) # arr = [18, 77,11,45,23]
    
    while i <= k:
        temp = pop(newStack)
        tmp = peek(newStack)
        if temp > tmp:
            pop(newStack)
            push(newStack, temp)
        i +=1
    return newStack

def reverseWords(stack3): # "Hello World"
    #get char from string(stack) stack : array DS
    str1 = ''
    k=1
    charLen = 0
    while stack3[0][k:] != '':
        k +=1
        charLen +=1
    j = charLen
    newStack = createStack()
    while not isEmptyStack(stack3) and j >= 0:
        temp = stack3[0][j]
        push(newStack, temp)
        j-=1
    return  str1.join(newStack) 

def checkSortedStack(stack3, inputStack):
    flag = "No"
    returnedStack = sortStack(stack3, inputStack, 0)
    i = 0
    while not isEmptyStack(returnedStack) and i <= len(returnedStack):
        temp = pop(returnedStack)
        tmp = peek((returnedStack))
        if tmp < temp:
            flag = "Yes"
        i+=1
    return "Is the stack sorted" , flag

    
     
stack1 = createStack()
stack2 = createStack()
stack3 = createStack()
inputStack = createStack()
#arr = [2, 7, 1, 3, 9, 4]
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

push(stack2, 23)
push(stack2, 45)
push(stack2, 11)
push(stack2, 77)
push(stack2, 18)
k=3

push(stack3, "Hello World")


#sizeofStack = len(stack1) - 1
#count = 0 




print("Original Stack", stack1)
#print(sortStack(stack1, inputStack, temp))
#print(recurStackReversal(stack, inputStack))
#deleteMiddleElement(stack1, sizeofStack, count)
#deleteMiddle(stack1, count)
#print(sortStackArr(stack1, inputStack))
#print(deleteSmallEle(stack2, k))
#print(reverseWords(stack3))
print(checkSortedStack(stack2, inputStack))
