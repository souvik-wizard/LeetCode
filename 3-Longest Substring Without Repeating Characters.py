# Efficient Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            if len(s) < 2:
                return len(s)
            l, r , longest= 0, 1 , 0
            while r < len(s):
                if s[r] not in s[l:r]:
                    r += 1
                else:
                    l += 1
                longest = max(longest, r-l)
            return longest

# Another Sol(Learned)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        elif len(s) == len(set(s)):
            return len(s)
        
        else:
            i = 0
            j = i + 1
            res = 1
            while i < len(s) and j < len(s):
                if len(s[i:j+1]) == len(set(s[i:j+1])):
                    res = max(res, len(s[i:j+1]))
                    j += 1
                else:
                    i += 1
                    j = i + 1
            return res