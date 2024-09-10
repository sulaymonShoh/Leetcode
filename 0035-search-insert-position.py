def searchInsert(nums: list[int], target: int) -> int:
    ans = 0
    if target in nums:
        ans = nums.index(target)
    else:
        for i in range(len(nums)):
            if nums[i]<target:
                ans = i+1
    print(ans)

searchInsert([1,3,5,6], 7)