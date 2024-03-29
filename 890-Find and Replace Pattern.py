class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
                return [word for word in words if len(set(word)) == len(set(pattern)) == len(set(zip(word, pattern)))]