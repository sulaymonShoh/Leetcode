class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(nums)
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        for i in range(l-len(res)):
            res.append('_')

        return l-len(res)


obj = Solution()
print(obj.removeDuplicates([1, 2, 3, 4, 1, 1, 1, 2]))
