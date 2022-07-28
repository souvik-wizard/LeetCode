class Solution:
    def numIdenticalPairs(nums):
            hash_dict={}
            res=0
            for i in range (len(nums)):
                if nums[i] in hash_dict:
                    hash_dict[nums[i]].append(i)
                else:
                    hash_dict[nums[i]]=[i]
                    
            #Using n*(n-1)/2 formula
            
            for key,values in hash_dict.items():
                if len(values) >= 2:
                    res+= len(values)*(len(values)-1)//2
            return res
                


                

    if __name__=="__main__":
        nums=[1,1,1,1]
        print (numIdenticalPairs(nums))