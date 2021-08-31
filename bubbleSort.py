arr = [64, 34, 25, 12, 22, 11, 90, 890, 456, 133544, 3454345,343,31,33,0,54,1,7,43,23443254,65]

i=0
j=i+1
temp = i
arrayLength = len(arr)
flag = 0

while i < arrayLength and flag < arrayLength -1:
    while j < arrayLength:
        if (arr[i] > arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
        i +=1
        j +=1
    i = temp
    j = i+1
    flag +=1

print(arr)