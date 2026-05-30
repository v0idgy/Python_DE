# ## Lomuto partition scheme for quicksort algorithm WHich takes last element as pivot and 
# # places it at its correct position in sorted array, and places all smaller 
# # (smaller than pivot) to left of pivot and all greater elements to right of pivot

## Method 1: Recusive implementation of quicksort algorithm using Lomuto partition scheme

# def partition(arr, low, high):
#     pivot = arr[high] ## pivot element is the last element of the array
#     i = low - 1 ## index of the smaller element
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1 ## increment index of the smaller element
#             arr[i], arr[j] = arr[j], arr[i] ## swap the elements
#     arr[i + 1], arr[high] = arr[high], arr[i + 1] ## swap the pivot element with the element at index i+1
#     return i + 1 ## return the partitioning index

# def quicksort(arr, low, high):
#     if low < high:
#         partitionIndex = partition(arr, low, high) ## partitioning index
#         quicksort(arr, low, partitionIndex - 1) ## recursively sort elements before partition (left side of the pivot)
#         quicksort(arr, partitionIndex + 1, high) ## recursively sort elements after partition (right side of the pivot)


# arr = [10, 7, 8, 9, 1, 5]

# n = len(arr)

# quicksort(arr, 0, n-1)

# print("Sorted array is:", arr)





##### Method 2: Using list comprehension to create new lists for elements less than, equal to, and greater than the pivot
## Pythonic way to implement quicksort algorithm using list comprehension to create new lists for elements less than, equal to, and greater than the pivot. This implementation is more concise and easier to read than the recursive implementation using Lomuto partition scheme.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot] ## list of elements less than the pivot
    right = [x for x in arr[1:] if x >= pivot] ## list of elements greater than or equal to the pivot
    return quicksort(left) + [pivot] + quicksort(right) ## recursively sort the
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)
print("Sorted array is:", sorted_arr)