import queue
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
    def wallsAndGates(self, rooms):
        # write your code here
        if not rooms:
            return
        
        height = len(rooms)
        width = len(rooms[0])
        q = queue.Queue(maxsize=0)
        for i in range(height):
            for j in range(width):
                if rooms[i][j] == 0:
                    q.put([i-1,j,1])
                    q.put([i+1,j,1])
                    q.put([i,j-1,1])
                    q.put([i,j+1,1])
                    while not q.empty():
                        position = q.get()
                        m = position[0]
                        n = position[1]
                        v = position[2]
                        if 0<=m<height and 0<=n<width and rooms[m][n]>v:
                            rooms[m][n]=v
                            q.put([m-1,n,v+1])
                            q.put([m+1,n,v+1])
                            q.put([m,n-1,v+1])
                            q.put([m,n+1,v+1])