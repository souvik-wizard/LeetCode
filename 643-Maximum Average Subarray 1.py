 # Using sliding window technique

def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Addition of first k elements in arr
        sum_arr=sum(nums[:k])
        #Storing avg values
        avg=[sum_arr/k]

        for i in range(1,len(nums)-k+1):
            # First value remove from previous sum
            sum_arr=sum_arr-nums[i-1]
            # K+1th value addition at the same time
            sum_arr=sum_arr+nums[i+k-1]
            avg.append(sum_arr/k)
 
        return max(avg)
        