from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.out = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.out:
            return -1
        self.out.move_to_end(key) #move to last operate
        return self.out[key]

    def put(self, key: int, value: int):
        if key in self.out:
            self.out.move_to_end(key) #move to last operate
        else:
            if len(self.out)==self.capacity:
                self.out.popitem(last=False)  #LIFO
        self.out[key] = value
        
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)