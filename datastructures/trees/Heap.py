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
    def __init__(self, minHeap=True):
        """
        Initiate the heap's internal list storage. 
        """
        self._heapList = []
        self._heapList.append(None) # 0 index is not used.
        self._count = 0
        if minHeap is True:
            self._siftUp = self._siftUpMinHeap
            self._siftDown = self._siftDownMinHeap
        else:
            self._siftUp = self._siftUpMaxHeap
            self._siftDown = self._siftDownMaxHeap
        
        self._isMinHeap = minHeap
    
    @property
    def isMinHeap(self):
        return self._isMinHeap
    
    def addElements(self, element_list):
        """
        Helper method that allows for multiple insertions.
        
        element_list: a Python list. 
        """
        if element_list is None:
            return
        for element in element_list:
            self.addElement(element)
        
    def addElement(self, element):
        """
        Add a Single element to the heap. Maintain heap condition.
        """
        if element is None: 
            return
        
        self._heapList.append(element)
        self._count = self._count + 1
        self._siftUp(self._count)
        
    
    def getElement(self):
        """
        Take an element from the top of the heap. Maintain heap condition.
        """
        if self._count == 0:
            return None
            
        element = self._heapList[1] #always we return index 1
        self._heapList[1] = self._heapList[self._count]
        del self._heapList[-1]
        self._siftDown()
        self._count = self._count - 1
        return element
    
    def _siftUpMinHeap(self, N):
        """
        MinHeap: Move the element at index N up until post condition is every heap element is lower than its children
        This operation maintains the min-heap condition after adding an element.
        """
        I = N
        parent = None
        while (I > 1):
            parent = self._heapList[I/2]
            if self._heapList[I] < parent: # less than parent? make it the parent
                self._heapList[I/2] = self._heapList[I]
                self._heapList[I] = parent
            else:
                # we reach a situation where the element is at I is not less than the parent. Break.
                break
            #Continue moving up the heap tree
            I = I / 2
        #while
                
    def _siftDownMinHeap(self):
        """
        MinHeap: We move the element at index 1 down so that heap post condition every node in the heap is less than its own child nodes.
        Maintains heap property after removing an element from the heap.
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
    
    def _siftUpMaxHeap(self, N):
        """
        MaxHeap: Move the element up until post condition is every element is less than its parent
        """
        I = N
        parent = None
        while (I > 1):
            parent = self._heapList[I/2]
            if self._heapList[I] > parent: # less than parent? make it the parent
                self._heapList[I/2] = self._heapList[I]
                self._heapList[I] = parent
            else:
                # we reach a situation where the element is not less than the parent. Break.
                break
            #Continue moving up the heap tree
            I = I / 2
        #while
                
    def _siftDownMaxHeap(self):
        """
        MaxHeap: We move the element at index 1 down so that post condition is every node element is greater than its children.
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
        '''
        Support for iterating through the heap.
        '''
        return self
    #
    def next(self):
        if self._count != 0:
            temp = self.getElement()
            return temp
        raise StopIteration
    
    def _getHeapAsList(self):
        """
        Returns the internal array representation of the heap.
        """
        return self._heapList