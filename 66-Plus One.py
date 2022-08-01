class Solution:
    def plusOne(self, arr: List[int]) -> List[int]: 

    
            # Python String join() Method
            # Converting integer list to string list and joining the list using join()
            res = int("".join(map(str, arr)))   

            #list comprehension 
            return [int(x) for x in str(int(res+1))] 
