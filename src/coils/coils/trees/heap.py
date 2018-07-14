'''
Created on Aug 5, 2015
@author: topcat
'''
class Heap(object):
    """
    Implements heap class in python. Heap holds an array(Python list) so that for index i, 2*i is left child and 2*i+1 is right child 
    in heap tree (if Min heap i.e).
     0   1   2   3   4   5   6   7   8   9
    [#] [y] [c] [b] [e] [g] [f] [z] [a] [p] ........
    """
    def __init__(self, min_heap=True):
        """
        Initiate the heap's internal list storage. 
        if you want a max heap set minHeap = False
        """
        self._heapList = []
        self._heapList.append(None) # 0 index is not used.
        self._count = 0
        if min_heap is True:
            self._siftUp = self._sift_up_min_heap
            self._siftDown = self._sift_down_min_heap
        else:
            self._siftUp = self._sift_up_max_heap
            self._siftDown = self._sift_down_max_heap
        
        self._is_min_heap = min_heap
        
    @property
    def heap_size(self):
        return len(self._heapList) - 1#accomodate first unused entry TODO:TEST THIS 
    
    @property
    def is_min_heap(self):
        return self._is_min_heap
    
    def add_items(self, item_list):
        """
        Helper method that allows for multiple insertions.
        
        item_list: a Python list. 
        """
        if item_list is None:
            return
        for item in item_list:
            self.add_item(item)
        
    def add_item(self, item):
        """
        Add a Single item to the heap. Maintain heap condition.
        """
        if item is None: 
            return
        
        self._heapList.append(item)
        self._count = self._count + 1
        self._siftUp(self._count)
        
    
    def get(self):
        """
        Take an item from the top of the heap. Maintain heap condition.
        """
        if self._count == 0:
            return None
            
        item = self._heapList[1] #always we return index 1
        self._heapList[1] = self._heapList[self._count]
        del self._heapList[-1]
        self._siftDown()
        self._count = self._count - 1
        return item
    
    def _sift_up_min_heap(self, N):
        """
        MinHeap: Move the item at index N up until post condition is every heap item is lower than its children
        This operation maintains the min-heap condition after adding an item.
        """
        I = N
        parent = None
        while (I > 1):
            parent = self._heapList[I/2]
            if self._heapList[I] < parent: # less than parent? make it the parent
                self._heapList[I/2] = self._heapList[I]
                self._heapList[I] = parent
            else:
                # we reach a situation where the item is at I is not less than the parent. Break.
                break
            #Continue moving up the heap tree
            I = I / 2
        #while
                
    def _sift_down_min_heap(self):
        """
        MinHeap: We move the item at index 1 down so that heap post condition every node in the heap is less than its own child nodes.
        Maintains heap property after removing an item from the heap.
        """
        I = 1
        C = 1
        while(2 * I < self._count):
            C = 2 * I
            if (C + 1)  < self._count: # has two children
                if self._heapList[C+1] < self._heapList[C]:
                    C = C + 1
            if self._heapList[I] > self._heapList[C]:
                temp = self._heapList[C]
                self._heapList[C] = self._heapList[I]
                self._heapList[I] = temp
            else:
                break
            I = C
    
    def _sift_up_max_heap(self, N):
        """
        MaxHeap: Move the item up until post condition is every item is less than its parent
        """
        I = N
        parent = None
        while (I > 1):
            parent = self._heapList[I/2]
            if self._heapList[I] > parent: # less than parent? make it the parent
                self._heapList[I/2] = self._heapList[I]
                self._heapList[I] = parent
            else:
                # we reach a situation where the item is not less than the parent. Break.
                break
            #Continue moving up the heap tree
            I = I / 2
        #while
                
    def _sift_down_max_heap(self):
        """
        MaxHeap: We move the item at index 1 down so that post condition is every node item is greater than its children.
        """
        I = 1
        C = 1
        while(2 * I < self._count):
            C = 2 * I
            if (C + 1)  < self._count: # has two children
                if self._heapList[C+1] > self._heapList[C]:
                    C = C + 1
            if self._heapList[I] < self._heapList[C]:
                temp = self._heapList[C]
                self._heapList[C] = self._heapList[I]
                self._heapList[I] = temp
            else:
                break
            I = C
    
    def __str__(self):
        return str(self._heapList)
    #
    def __iter__(self):
        while self._count != 0:
            yield self.get()

    def _get_heap_as_list(self):
        """
        Returns the internal array representation of the heap.
        """
        return self._heapList