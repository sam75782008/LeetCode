class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(A)):
            ans.append([])
            for j in range(len(B[0])):
                ans[i].append(0)
        
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    if A[i][k]==0 or B[k][j]==0:
                        continue
                    else:
                        ans[i][j] += A[i][k]*B[k][j]
        return ans
        