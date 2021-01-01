#ksum function
def kSum(nums, target, k):
    #The nums array is assumed to be sorted already
    res = []
    if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
        return res
    if k == 2:
        return twoSum(nums, target)
    for i in range(len(nums)):
        if i == 0 or nums[i - 1] != nums[i]:
            for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                res.append([nums[i]] + set)
    return res

#Helper function 2sum
def twoSum(nums, target):
    res = []
    lo, hi = 0, len(nums) - 1
    while (lo < hi):
        sum = nums[lo] + nums[hi]
        if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
            lo += 1
        elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
            hi -= 1
        else:
            res.append([nums[lo], nums[hi]])
            lo += 1
            hi -= 1
    return res


#Traversing the outermost elements first, then the inner elements
def spiralOrder(matrix):
    n = len(matrix)
    if(n==0):
        return matrix
    elif(n==1):
        return matrix[0]
        
    m = len(matrix[0])
    if(m==1):
        ans = [row[0] for row in matrix]
        return ans
        
    size=m*n
    rowIndex = 0
    colIndex = 0
    ans=[]
    while(rowIndex<n and colIndex<m):
        for i in range(colIndex,m):
            ans.append(matrix[rowIndex][i])
        rowIndex+=1
            
        for i in range(rowIndex,n):
            ans.append(matrix[i][m-1])
        m-=1
            
        #When we have reached the middle most element
        if(len(ans)==size):
            break
        
        for i in range(m-1,colIndex-1,-1):
            ans.append(matrix[n-1][i])
        n-=1
                
        for i in range(n-1,rowIndex-1,-1):
            ans.append(matrix[i][colIndex])
        colIndex+=1
        
    return(ans)


#Longest Consecutive sequence in an array
def longestConsecutive(self, nums):
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


#Maximum Subarray sum modulo m
def maximumSum(a, m):
    size = len(a)
    arr=a
    mod=m

    sums = [-1] * size
    temp = [-1] * 2
    temp[0] = arr[0] % mod
    temp[1] = 0
    sums[0] = temp
    
    #calculate prefix sums
    for pos in range(1, size): 
        temp = [-1] * 2
        temp[0] = (sums[pos-1][0] + (arr[pos] % mod)) % mod
        temp[1] = pos
        sums[pos] = temp

    sums = sorted(sums)
    minimum = mod

    #determine the minimum
    for pos in range(0, size-1):
        if sums[pos][1] > sums[pos+1][1] and (sums[pos+1][0] - sums[pos][0] < minimum):
            minimum = sums[pos+1][0] - sums[pos][0]

    #edge case
    if sums[size-1][0] > mod - minimum: 
        minimum = mod - sums[size-1][0]

    return(mod - minimum)


#Find numbers that are missing in an array of size n which has numbers only in range 1 to n.
def findDisappearedNumbers(self, nums):
    for i in range(len(nums)):
        num = abs(nums[i])
        #Store a negative number at all the positions that occur in array
        nums[num-1] = -1*abs((nums[num-1]))
    res=[]
    #The position where a positive number is present in the missing number.
    for i,n in enumerate(nums):
        if(n>0):
            res.append(i+1)
    return res
