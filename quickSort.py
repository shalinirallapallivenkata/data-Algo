arr = [10, 80, 30, 90, 40, 50, 70]
low = 0
high = len(arr) - 1
i=-1
j=0

def partition(arr, high, pivot):
    while i < len(arr) - 1 :
        while j < len(arr) - 1 :
            if (arr[j] < pivot):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        if (arr[i+1] > pivot):
            arr[i+1], arr[high] = arr[high], arr[i+1]
            break
    return i+1


def quickSort(arr, low, high):
    pivot = arr[high]

    if ( low < high):
        pi = partition()
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
    return arr


quickSort(arr, low, high)






