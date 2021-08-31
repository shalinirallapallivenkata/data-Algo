A = [64, 34, 25, 12, 22, 11, 90, 890, 456, 133544, 3454345,343,31,33,0,54,1]

arrayLength = len(A)

i=0
j=1
while i <= arrayLength-1: # 0
    while j <= arrayLength-1: #1
        if A[i] > A[j] : 
            A[i], A[j] = A[j], A[i] 
        j += 1
    i +=1
    j= i+1

noDup = []
for i in range(len(A)):
    if A[i] not in noDup:
        noDup.append(A[i])
print(noDup)
