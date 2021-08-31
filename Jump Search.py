import math
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 37
n = len(arr)

step = math.sqrt(n)
flag = 0
while arr[int(min(step,n)) -1] < x:
    flag = step # 4
    step += math.sqrt(n) #8

while arr[int(flag)] < x:
    flag += 1

if(arr[int(flag)]==x):
    print('Found Match at index of the array' , flag, 'and the value is', arr[int(flag)])
else:
    print('Match not found')

