def bubbleSort(arr): ## Function to perform bubble sort on the given array
    n = len(arr) ## Get the length of the array
    for i in range(n): ## Traverse through all array elements
        for j in range(0, n-i-1): ## Last i elements are already in place, so we can ignore them
            if arr[j] > arr[j+1]: ## If the element found is greater than the next element, then swap them
                arr[j], arr[j+1] = arr[j+1], arr[j] ## Swaping the elements if they are in the wrong order

arr = [64,34,25,12,22,11,90]
bubbleSort(arr)
print(arr)




