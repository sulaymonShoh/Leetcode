class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        s = [len(i.split()) for i in sentences]
        return max(s)