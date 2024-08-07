def subset(ind, nums, ans, val, final, n):
    if sum(ans)==val:
        final.add(tuple(ans))

    if ind >= n:
        return
    
    ans.append(nums[ind])
    subset(ind + 1, nums, ans, val, final, n)
    ans.pop()
    subset(ind + 1, nums, ans, val, final, n)



nums = [1, 2, 3, 7, 0, 0]
ans =[]
val = 10
final = set()
n =len(nums)

subset(0, nums, ans, val, final, n)
print(final)