class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def check(matrix,target,start,vertical):
            lo = start
            if vertical:
                hi = len(matrix[0])-1
            else:
                hi = len(matrix)-1
            while lo<=hi:
                mid = (lo+hi)//2
                if vertical:
                    if matrix[start][mid]>target:
                        hi = mid-1
                    elif matrix[start][mid]<target:
                        lo = mid+1
                    else:
                        return True
                else:
                    if matrix[mid][start]>target:
                        hi = mid-1
                    elif matrix[mid][start]<target:
                        lo = mid+1
                    else:
                        return True
            return False               
                
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(min(m,n)):
            column = check(matrix,target,i,True)
            row = check(matrix,target,i,False)
            if column or row:
                return True
        return False
            
        '''
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==target:
                    return True
        return False
        '''
        
        
        
    
        