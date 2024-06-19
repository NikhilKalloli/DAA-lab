#  Time Complexity: O(n log n) where n is the number of elements in the input array.

def mergeSort(arr):
    if(len(arr)<=1):
         return arr,0
    
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left, left_count = mergeSort(left)
    right, right_count = mergeSort(right)

    merged , merge_count = merge(left, right)
    total = merge_count + left_count + right_count

    return merged ,total

def merge(left, right):
    merged =[]
    i =0
    j=0
    count =0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
            count += len(left) - i
    
    merged+= left[i:]
    merged+= right[j:]

    return merged, count
        


arr = [12, 11, 13, 5, 6, 7]
sorted_arr, inversions = mergeSort(arr)
print("Sorted array:", sorted_arr)
print("Number of inversions:", inversions)