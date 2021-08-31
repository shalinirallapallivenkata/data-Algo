arr = [12, 11, 13, 5, 6]
#[5 12 13 11 6 ]

arrayLength = len(arr)

i=1
j=0
while j < arrayLength - 1: 
    while i in range(1, len(arr)):
        if(arr[j] > arr[i]):
            arr[j], arr[i] = arr[i], arr[j]
        i+=1
    j +=1
    if ( i == arrayLength):
        i = j+1

print(arr)
            