class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
            count = Counter()
            for i in words2:
                count |= Counter(i)
            # print(count)
            return [a for a in words1 if not count - Counter(a)]
