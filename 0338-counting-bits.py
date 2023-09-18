class Solution:
    def countBits(self, n: int):
        ans = []
        for i in range(n+1):
            if i == 0: ans.append(0)
            else:
                ans.append(bin(i)[2:].count('1'))
        return ans

obj = Solution()
print(obj.countBits(5))