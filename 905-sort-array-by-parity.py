class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        x,y=[],[]
        for i in nums:
            if i%2==0:
                x.append(i)
            else:
                y.append(i)
        return x+y

obj = Solution()
print(obj.sortArrayByParity([1, 2, 3, 4, 5]))