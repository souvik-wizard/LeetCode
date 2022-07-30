class Solution:
    def plusOne(self, arr: List[int]) -> List[int]:
            res = int("".join(map(str, arr)))           
            return [int(x) for x in str(int(res+1))] 
