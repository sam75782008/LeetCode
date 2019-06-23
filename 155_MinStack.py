#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#push(x) -- Push element x onto stack.
#pop() -- Removes the element on top of the stack.
#top() -- Get the top element.
#getMin() -- Retrieve the minimum element in the stack.

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = []
        return
        

    def push(self, x: int):
        self.items.append(x)
        if not self.min or self.min[-1]>=x:
            self.min.append(x)
        return

    def pop(self):
        if self.items[-1]==self.min[-1]:
            self.min.pop()
        self.items.pop()
        return

    def top(self):
        return_item = self.items[-1]
        return return_item        

    def getMin(self):
        min_list = self.min[-1]
        return min_list