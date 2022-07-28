# # O(n) tc but easy and understandable

# class Solution:
#     def numIdenticalPairs(nums):
#             hash_dict={}
#             res=0
#             for i in range (len(nums)):
#                 if nums[i] in hash_dict:
#                     hash_dict[nums[i]].append(i)
#                 else:
#                     hash_dict[nums[i]]=[i]
                    
#             #Using n*(n-1)/2 formula
            
#             for key,values in hash_dict.items():
#                 if len(values) >= 2:
#                     res+= len(values)*(len(values)-1)//2
#             return res
                

#a bit weird O(n^2) but smart approach using question hints

class Solution:
    def numIdenticalPairs(nums):
            res = 0

            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[j]==nums[i] and i<j:
                        res+=1

            return res               

    if __name__=="__main__":
        nums=[1,1,1,1]
        print (numIdenticalPairs(nums))