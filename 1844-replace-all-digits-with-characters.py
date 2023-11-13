class Solution:
    def replaceDigits(self, s: str) -> str:
        i = 1
        while i < len(s):
            s = s.replace(s[i], chr(ord(s[i - 1]) + int(s[i])), 1)
            i += 2
        return s


obj = Solution()
print(obj.replaceDigits("a1c1e1"))
# finished
