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

# first if length is < 2 we simply  return the length of our given string.
# then we simply check for that perticular character in s (where range of "s" is our left pointer to right )
# if not in "s" (that means unique) we increase our right pointer to check the next character untill we get any duplicate value
# if yes we increase our left pointer and perform the same operation
# every time we'll update our "longest var" by compareing (maximum value) with right - left (r-l)
# in the end we'll return our Longest Substring 


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