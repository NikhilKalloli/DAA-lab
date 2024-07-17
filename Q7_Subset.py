def find(index, arr, ans, n, val, final):
    if sum(ans) == val:
        final.add(tuple(ans)) 
    
    if index >= n:
        return
        
    ans.append(arr[index])
    find(index + 1, arr, ans, n, val, final)
    ans.pop()
    find(index + 1, arr, ans, n, val, final)


nums = [1, 2, 3, 7, 0, 0]
ans = []
final = set()
n = len(nums)
find(0, nums, ans, n, 10, final)

if final:
    print(final)
else:
    print("not possible")
