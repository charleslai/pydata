#Algorithms.py
#Charles J. Lai
#July 13, 2013

"""
This module contains both implementations of common abstract data types as
well as "helper" data structures for different implementations including
linked nodes and tree cells.

If the class name of the ADT implementation has no sigils/suffix/prefix, then
the ADT is a list implementation of the ADT. Otherwise, the augmented name
will describe the implementation of the ADT i.e. linked for a linked list
implementation and etc.
"""

#==========================HELPER STRUCTURES================================

class Node(object): #NEEDS TO BE DEBUGGED ... USING A GETTER OR SETTER MAKES PYTHON CALL ON NONE TYPE
    """
    Instances represent a linked node that can be used to implement ADTs
    """
    #Properties
    _data = None      #Field: The data property of this particular node
    _next = None    #Field: The "next" node that is linked to this node

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

    def __init__(self, value=None, node=None):
        self._data = value
        self._next = node


class TreeCell(object):
    """
    Instances represent a tree cell that can be used to build trees and ADT's
    """
    pass


#=========================ADT IMPLEMENTATIONS===============================
class Bag(object):
    """
    Instances represent a list implementation of the Bag data structure.

    The Bag data structure is a way of holding data in a manner that 
    resembles a bag.
    """
    #Properties
    _data = []              #Field:The list of data wrapped in a Bag
    _number_of_entries = 0  #Field:The number of entries in the Bag
    _DEFAULT_CAPACITY = 25  #Field:The default size of a given Bag

    def __init__(self, data=[], DEFAULT_CAPACITY = 25):
        """
        Constructor: Create a new instance of a Bag data structure
        
        Precondition: data is a valid list of data
        """
        self._data = data
        self._number_of_entries = len(self.q_data)
        self._DEFAULT_CAPACITY = DEFAULT_CAPACITY

    #Data Entry/Removal Methods
    def add(self, new_entry):
        pass
    def remove(self):
        pass
        pass
    def clear(self):
        pass

    #Data Checking Methods
    def get_current_size(self):
        return self._number_of_entries
    def is_full(self):
        pass
    def is_emptry(self):
        pass
    def contains(self):
        pass
    def get_frequency_of(self, entry):
        pass


class Stack(object):
    """
    Instances represent a list implementation of the Stack data structure.

    The Stack data structure is a LIFO (Last in First Out) data in a manner 
    similar to a stack of objects in real life. This is in contrast to the
    Queue data structure which is FIFO (First in First Out).
    """
    #Properties
    _data = []              #Field:The list of data wrapped as a Stack

    def __init__(self, data=[]):
        """
        Constructor: Creates a new instance of the stack data structure
        """
        self._data = data

    #Data Entry/Removal Methods
    def push(self, value):
        _data.append(value)

    def pop(self):
        _data.pop([len(_data) - 1])

    def peek(self):
        return _data[len(_data) - 1]

    def clear(self):
        del s[0:len(_data)]

class LinkedStack(object):
    """
    Instances represent a LinkedList implementation of the Stack data structure.

    The Stack data structure is a LIFO (Last in First Out) data in a manner 
    similar to a stack of objects in real life. This is in contrast to the
    Queue data structure which is FIFO (First in First Out).
    """

    #Properties
    _linked_list = None

    def __init__(self, linked_list):
        """
        Constructor: creates a new instace of the LinkedStack data structure
        """
        self._linked_list = linked_list

    #Data Entry/Removal Methods
    def push(self, value):
        self._linked_list = Node(value, self._linked_list)

    def pop(self):
        data = self._linked_list.data()
        self._linked_list = self._linked_list.next()
        return data

    def peek(self):
        return self._linked_list.data()

    def remove(self):
        self._linked_list = self._linked_list.next()

    def clear(self):
        #while there are still nodes in the linked list, remove the head.
        while self._linked_list.next() != None:
            self.remove()
        #Then set the last node's data field to 0 usng a setter method.
        self._linked_list.data(None)


class Queue(object):
    pass

class LinkedQueue(object):
    pass

class PriorityQueue(object):
    pass

class Dictionary(object):
    pass
