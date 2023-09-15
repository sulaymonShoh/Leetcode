class Solution:
    def countMatches(items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        rule = 0
        if ruleKey == 'color':
            rule = 1
        elif ruleKey == 'name':
            rule = 2

        for i in items:
            if i[rule] == ruleValue: res += 1

        return res
