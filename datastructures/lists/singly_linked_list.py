'''
Created on Aug 12, 2015
@author: hari
'''
class LinkedNode(object):
    """
    A node in a Linked list.
    """
    __slots__ = 'element', 'nextNode'
    def __init__(self, element = None, nextNode = None):
        '''
        a node is created with the element object and the next node. If any of these
        are not available, use the default value None.
        '''
        self.nextNode = nextNode
        self.element = element
        
    def __str__(self):
        return '%s %s' % (self.__class__.__name__, self._element)
    
    def __repr__(self):
        return '%s(element = %s)' % (self.__class__.__name__, self._element)
        
class LinkedList(object):
    '''
    A Linked list implementation. More pythonic by using iterator features.
    Note:
    1) Iterating over the list does not take out the nodes.
    2) Node with duplicate elements are allowed.
    3) LinkedNode A == LinkedNode B does not compare their elements. You must do 
       A.element == B.element How element objects match is up to the application. 
    '''
    def __init__(self):
        self._head = None
        self._tail = self._head
        self._length = 0
            
    @property
    def length(self):
        return self._length
    
    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail
        
    def append(self, element):
        """
        Adds an element to the end of the list as a Node.
        """
        if self._head is None:
            self._head = LinkedNode(element)
            self._tail = self._head
        else:
            new_node = LinkedNode(element)
            self._tail.nextNode = new_node
            self._tail = new_node
        
        self._length = self._length + 1
    #
    
    def index(self, element):
        '''
        Returns -1 if element is not present in list. If present function returns the
        0 based index of the element in the list.
        '''
        if self._length == 0:
            return -1
         
        index = 0
        current_node = self._head
        while (current_node is not None):
            if current_node.element == element:
                return index
            current_node = current_node.nextNode
            index = index + 1
        return -1
    #
    
    def insert_at(self, index, element):
        if index <= 0 or index >= self._length: #insert at head or at tail
            self.append(element) #takes care of length, head, tail etc
            return
        #index is somewhere in between head and tail locations. we find the node at index - 1
        count = 0
        till_where = index - 1 #calculate this before hand rather than leave it to the while condition. Helps in very large index.
        current_node = self._head
        
        while count != till_where:
            current_node = current_node.nextNode
            count = count + 1
        temp = current_node.nextNode
        current_node.nextNode = LinkedNode(element = element, nextNode = temp)
        self._length = self._length + 1
            
    def extend(self, linked_list):
        '''
        extend takes another LinkedList instance and adds each element of linked_list as a NEW
        node of this list.
        '''
        if linked_list is None:
            return   
        for element in linked_list:
            self.append(element)
    #
    
    def remove(self, element):
        if self._length == 0:
            return
        
        if self._head.element == element:
            if self._head.nextNode == None:
                self._head = None
                self._tail = None
            else:
                self._head = self._head.nextNode
            self._length = self._length - 1
            return
        
        current_node = self._head
        prev_node = current_node
        
        while (current_node != None):
            if current_node.element != element:
                prev_node = current_node
                current_node = current_node.nextNode
            else:
                break
        
        if current_node == None:#did not find the element in the list.
            return
        #element found. it is in current_node.
        prev_node.nextNode = current_node.nextNode
        if prev_node.nextNode == None: #Prev is the tail now.
            self._tail = prev_node
        self._length = self._length - 1
    #
    def __iter__(self):
        start_node = self._head
        while start_node != None:
            yield start_node.element
            start_node = start_node.nextNode
    #
    def __len__(self):
        return self._length
    
    def __str__(self):
        return '%s has %s element(s)' % (self.__class__.__name__, str(self._length))
    
    def remove_duplicates(self):
        '''
        Removes nodes with duplicate elements. We build the corrected list.
        '''
        if self.length < 2:
            return
        last_node_of_corrected_list = self._head
        running_node = self._head
        current_node = last_node_of_corrected_list.nextNode
        
        while current_node != None:#all the way until end
            running_node = self._head
            while running_node != current_node:
                if running_node.element == current_node.element: #duplicate
                    nxt_of_duplicate = current_node.nextNode
                    last_node_of_corrected_list.nextNode = nxt_of_duplicate
                    self._length = self._length - 1 
                    current_node = nxt_of_duplicate
                    break
                running_node = running_node.nextNode
                
            if running_node == current_node:# current node did not have a duplicate element in the list seen so far
                last_node_of_corrected_list = current_node
                current_node = current_node.nextNode
        
        self._tail = last_node_of_corrected_list    