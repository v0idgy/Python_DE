# def mergeSort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         L = arr[:mid] ## Left Array
#         R = arr[mid:] ## Right Array

#         mergeSort(L) ## passing the left array to mergeSort function
#         mergeSort(R) ## passing the right array to mergeSort function

#         i = j = k = 0 ## i is index for left array, j is index for right array and k is index for merged array

#         while i < len(L) and j < len(R): ## Merging the left and right arrays
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1

#         while i < len(L): ## Copying any remaining elements from the left array
#             arr[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(R): ## Copying any remaining elements from the right array
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     return arr


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = mergeSort(arr[:mid]) 
    right_half = mergeSort(arr[mid:])
    return merge(left_half, right_half) ## 2 ,3 ,4 ,6 ,7 ,11 ,12 ,13 , 5, 
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append any remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [12,11,13,5,6,7]
print("Given array is", arr)
arr1= mergeSort(arr)
print("Sorted array is", arr1)