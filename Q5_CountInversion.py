# O(n log(n))
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half, left_count= merge_sort(left_half)
    right_half, right_count = merge_sort(right_half)
    merged , merge_count = merge(left_half, right_half)

    total_count = left_count + right_count + merge_count
    
    return merged, total_count

def merge(left, right):
    merged = []
    i = 0
    j = 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i
    
    merged += left[i:]
    merged += right[j:]
    
    return merged, count

num = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(num):
    element = int(input("Enter element: "))
    arr.append(element)

# arr = [12, 11, 13, 5, 6, 7]

start_time = time.time()
sorted_arr,count = merge_sort(arr)
end_time = time.time()

execution_time = end_time - start_time

print("Sorted array:", sorted_arr)
print(f"Number of inversions: {count}")
print(f"Execution time: {execution_time} seconds")