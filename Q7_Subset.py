def show(index, arr, ans, n, val):
    if sum(ans) == val:
        print(ans)
            
    if index >= n:
        return
        
    ans.append(arr[index])
    show(index + 1, arr, ans, n, val)
    ans.pop()
    show(index + 1, arr, ans, n, val)

nums = [1, 2, 3 , 7, 0]
ans = []
n = len(nums)
show(0, nums, ans, n, 10)