def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


num = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(num):
    element = int(input("Enter element: "))
    arr.append(element)

# arr = [64, 25, 12, 22, 11]
sorted_arr = quicksort(arr)
print("Sorted array is:", sorted_arr)