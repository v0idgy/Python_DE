def heapify(arr, n, i):
    largest = i ## Initialize largest as root
    l = 2 * i + 1 ## left = 2*i + 1
    r = 2 * i + 2 ## right = 2*i + 2
    if l < n and arr[l] > arr[largest]: ## If left child is larger than root
        largest = l
    if r < n and arr[r] > arr[largest]: ## If right child is larger than largest so far
        largest = r
    if largest != i: ## If largest is not root
        arr[i], arr[largest] = arr[largest], arr[i] ## swap
        heapify(arr, n, largest) ## Recursively heapify the affected sub-tree

def heapSort(arr):
    n =len(arr)
    for i in range(n//2 - 1, -1, -1): ## Build a maxheap.
        heapify(arr, n, i)
    for i in range(n-1, 0, -1): ## One by one extract elements from heap
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [12,11,13,5,6,7]
heapSort(arr)
print("Sorted array is: ", arr)