class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s = s.split(':')
        bl = s[0][0]
        el = s[-1][0]
        bn = int(s[0][1])
        en = int(s[-1][1])
        res = []

        for k in range(ord(bl), ord(el) + 1):
            for i in range(bn, en+1):
                res.append(f'{chr(k)}{i}')

        return res
