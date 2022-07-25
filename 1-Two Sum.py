# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_dict={}
#         for index,value in enumerate(nums):
#             diffrence=target-value
#             if diffrence in hash_dict:
#                 return [index,hash_dict[diffrence]]
#             hash_dict[value]=index
                
                        
dictionary = {}

keys = [1,2,5,4,7,8,88]

for idx, value in enumerate(keys):
	dictionary[idx] = value
print(dictionary)
