# Beginer friendly

def minCostClimbingStairs(cost):
    cost.append(0)
    for i in range(len(cost)-3,-1,-1):          #range(initial , final[-1 bcz we need to go to index 0] , jump)
                
        cost[i]+= min(cost[i+1],cost[i+2])

    return min(cost[0],cost[1])


# sol 2 [learned]

def minCostClimbingStairs(cost):
    p0=cost[0]
    p1=cost[1]
    
    for i in range (2, len(cost)):
        temp=cost[i]+ min(p1,p0)
        p0=p1
        p1=temp
    return min(p0,p1)





if __name__=="__main__":
    cost=[1,100,1,1,1,100,1,1,100,1]
    print(minCostClimbingStairs(cost))




# This example may help to understand [debug it for better understanding] || take final -1 & 0 
for x in range(10, -1, -1):
  print(x) 
