import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged += left[i:]
    merged += right[j:]
    
    return merged

num = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(num):
    element = int(input("Enter element: "))
    arr.append(element)

# arr = [12, 11, 13, 5, 6, 7]

start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()

execution_time = end_time - start_time

print("Sorted array:", sorted_arr)
print(f"Execution time: {execution_time} seconds")