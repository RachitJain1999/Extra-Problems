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
