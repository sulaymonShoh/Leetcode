class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result

obj = Solution()
print(obj.permute([1, 2, 3]))