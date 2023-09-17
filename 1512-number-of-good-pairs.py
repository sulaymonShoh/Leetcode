class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        sn = set(nums)
        s = 0
        for i in sn:
            n = nums.count(i)
            s += n * (n-1) // 2

        return s
