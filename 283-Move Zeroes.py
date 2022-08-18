class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for item in range(len(arr)):
            if arr[item]==0:
                arr.remove(0)
                arr.append(0)
        