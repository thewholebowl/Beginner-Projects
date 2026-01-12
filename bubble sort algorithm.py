def bbsort(arr):
    n = len(arr)
    for j in range(n):
        swapped = False
        for i in range(1, n - j):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
        if not swapped:
            break
    return arr
print(bbsort(eval(input("Enter array: "))))
