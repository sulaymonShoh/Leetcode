class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''
        for i in digits: s += str(i)
        s = list(map(int, list(str(int(s) + 1))))
        return s

obj = Solution()
print(obj.plusOne([1, 2, 3]))