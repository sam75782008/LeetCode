import queue
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # write your code here
        if not any(board):
            return
        n = len(board)
        m = len(board[0])
        q = [ij for k in range(max(n,m)) for ij in ((0,k),(n-1,k),(k,0),(k,m-1))]
        while q:
            i,j=q.pop()
            if 0<=i<n and 0<=j<m and board[i][j]=='O':
                board[i][j]='W'
                q += (i,j-1),(i,j+1),(i-1,j),(i+1,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='W':
                    board[i][j]='O'
                else:
                    board[i][j]='X'      