#practice of sorting

#packages
import numpy as np
import timeit
start = timeit.default_timer()

#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start)  


class sorting():
    def __init__ (self,arr):
        self.arr_bubble = arr.copy()
        self.arr_selection = arr.copy()
        self.arr_insert = arr.copy()
    
    def bubble(self):
        #how many need to be sorted
        for i in range(1,len(self.arr_bubble)):
            #which one is being sorted
            for j in range(len(self.arr_bubble)-i):
                if self.arr_bubble[j] > self.arr_bubble[j+1]:
                    self.arr_bubble[j+1], self.arr_bubble[j] = self.arr_bubble[j], self.arr_bubble[j+1]
        
        return self.arr_bubble
    
    def selection(self):
        #which location need to be switch
        for i in range(len(self.arr_selection)-1):
            mini_id = i
            #find the minimal location
            for j in range(i+1,len(self.arr_selection)):
                if self.arr_selection[j] < self.arr_selection[mini_id]:
                    mini_id = j
            if i != mini_id:
                self.arr_selection[i], self.arr_selection[mini_id] = self.arr_selection[mini_id], self.arr_selection[i]
        return self.arr_selection
    
    def insert(self):
        for i in range(len(self.arr_insert)):
            preindex = i-1
            current = self.arr_insert[i]
            
            #insert to left
            while preindex>=0 and current<self.arr_insert[preindex]:
                self.arr_insert[preindex+1] = self.arr_insert[preindex]
                preindex -= 1
            
            self.arr_insert[preindex+1] = current
            
        return self.arr_insert
    
    #===============quick sort====================#
    def partition(self,arr,a,b):
        
        pivot = arr[b]
        i = a
        #find the one need to be change
        for j in range(a,b):
            if arr[j]<=pivot: #no ned to change-->move to next
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[b] = arr[b], arr[i]
        #use i to separate
        return i
            
    def quicksort(self,arr,a,b):
        if a>=b: #left>right return
            return
        i = self.partition(arr, a,b)
        self.quicksort(arr,a,i-1)
        self.quicksort(arr,i+1,b)
        
    def call_quicksort(self,arr):
        a = 0;
        b = len(arr)-1
        self.quicksort(arr, a, b)
        return arr
    #===============quick sort====================#
    
    #===============merge sort====================#
    def mergesort(self,arr):
        #merge
        def merge(left, right):
            result = []
            i = j = 0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result = result + left[i:] + right[j:]
            return result
        
        #recrusion
        if len(arr)<=1:
            return arr
        mid = len(arr)//2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])
        return merge(left,right)
        
    #===============merge sort====================#
    
    #==============heap sort======================#
    def heapsort(self,arr):
        
        def adjustHeap(arr, i , size):
            left_child = 2*i+1
            right_child = 2*i+2
            largest = i
            
            #chack max heap
            if left_child<size and arr[left_child]>arr[largest]:
                largest = left_child
            if right_child<size and arr[right_child]>arr[largest]:
                largest = right_child
            
            #switch to head
            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                
                #keep push heap
                adjustHeap(arr, largest, size)
        
        def builtHeap(arr,size):
            for i in range(len(arr)//2)[::-1]: #start with leaf
                adjustHeap(arr,i,size)
        
        size = len(arr)
        builtHeap(arr,size)
        
        for i in range(len(arr))[::-1]:
            arr[0], arr[i] = arr[i], arr[0]
            adjustHeap(arr,0,i)
        
        return arr
    #=============heap sort=======================#
        

def main():
    test_array = [3,44,38,5,47,5,36,26,27,2]
    print('input array:', test_array)
    print("")
    model = sorting(test_array)
    
    #bubble
    start = timeit.default_timer()
    sort_array = model.bubble()
    stop = timeit.default_timer()
    print('bubble sorting:',sort_array)
    print('bubble sorting time:',stop-start)
    print("")

    #selection
    start = timeit.default_timer()
    sort_array = model.selection()
    stop = timeit.default_timer()
    print('selection sorting:',sort_array)
    print('selection sorting time:',stop-start)
    print("")

    #insert
    start = timeit.default_timer()
    sort_array = model.insert()
    stop = timeit.default_timer()
    print('insert sorting:',sort_array)
    print('insert sorting time:',stop-start)
    print("") 

    #merge
    temp = test_array.copy()
    start = timeit.default_timer()
    sort_array = model.mergesort(temp)
    stop = timeit.default_timer()
    print('merge sorting:',sort_array)
    print('merge sorting time:',stop-start)
    print("")
    
    #quick
    temp = test_array.copy()
    start = timeit.default_timer()
    sort_array = model.call_quicksort(temp)
    stop = timeit.default_timer()
    print('quick sorting:',sort_array)
    print('quick sorting time:',stop-start)
    print("")
    
    #heap
    temp = test_array.copy()
    start = timeit.default_timer()
    sort_array = model.heapsort(temp)
    stop = timeit.default_timer()
    print('heap sorting:',sort_array)
    print('heap sorting time:',stop-start)
    print("") 
    
    #default
    start = timeit.default_timer()
    default = sorted(test_array)
    stop = timeit.default_timer()
    print('default sort:',default)
    print('default sorting time:',stop-start)

if __name__ == '__main__':
    main()