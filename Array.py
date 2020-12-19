#nums array is sorted
def kSum(nums, target, k):
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

#Traversing the outermost elements first, then the ineer elements
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
