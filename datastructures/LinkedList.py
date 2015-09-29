'''
Created on Aug 12, 2015
@author: hari
'''
class LinkedNode(object):
    """
    A node in a Linked list.
    """
    def __init__(self, element = None, nextNode = None):
        '''
        a node is created with the element object and the next node. If any of these
        are not available use the default value None.
        '''
        self._next = nextNode
        self._element = element
    
    @property
    def nextNode(self):
        return self._next
    
    @nextNode.setter
    def nextNode(self, value):
        self._next = value
    
    @property
    def element(self):
        return self._element
    
    @element.setter
    def element(self, value):
        self._element = value
        
    def __str__(self):
        return '%s %s' % (self.__class__.__name__, self._element)
    
    def __repr__(self):
        return '%s(element = %s, nextNode = %s)' % (self.__class__.__name__, self._element, self._next)
        
class LinkedList(object):
    '''
    A Linked list implementation. More pythonic by using iterator features.
    '''
    def __init__(self):
        self._head = None
        self._length = 0
        self._tail = self._head
            
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
    
    def extend(self, linked_list):
        '''
        extend takes another LinkedList instance and adds each element of linked_list as a NEW
        node of this list.
        '''
        if linked_list is None:
            return   
        for node in linked_list:
            self.append(node.element)
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
        self._length = self._length - 1
    #
    def __iter__(self):
        self._iterNode = self._head
        return self
    #
    def next(self):
        if self._iterNode is not None:
            temp = self._iterNode
            self._iterNode = self._iterNode.nextNode
            return temp   
        raise StopIteration
    #
    def __str__(self):
        return '%s has %s element(s)' % (self.__class__.__name__, str(self._length))