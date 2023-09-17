# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
        # l, r = 0, 0
        #
        # while r < len(nums):
        #     count = 1
        #     while r + 1 < len(nums) and nums[r] == nums[r + 1]:
        #         r += 1
        #         count += 1
        #
        #     for i in range(min(2, count)):
        #         nums[i] = nums[r]
        #         l += 1
        #     r += 1
        # return l
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        pointer = 2
        for num in nums[2:]:
            if nums[pointer - 2] != num:
                nums[pointer] = num
                pointer += 1
        return pointer, nums


obj = Solution()
print(obj.removeDuplicates([1, 1, 1, 2, 2, 3]))
