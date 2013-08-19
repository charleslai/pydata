#datastructures.py
#Charles J. Lai
#July 13, 2013

"""
==============
datastructures
==============
This module contains both implementations of common abstract data types as
well as "helper" data structures for different implementations including
linked nodes and tree cells.

If the class name of the ADT implementation has no sigils/suffix/prefix, then
the ADT is a list implementation of the ADT. Otherwise, the augmented name
will describe the implementation of the ADT i.e. linked for a linked list
implementation and etc.

Contents
--------
Helper Data Structures:
* Node
* Linked List
* Doubly Linked List
* TreeCell

Classic Data Structures:
* Bag
* Stack
* Linked Stack
* Queue
* Linked Queue
* Priority Queue
* Dictionary/Hash Table

"""
#============================
#   Helper Data Structures
#============================
class Node(object):
    """
    Instances represent a linked node that can be used to implement ADTs

    ===========
    Description
    ===========
    The node has two attributes: a data field that wraps the data contained
    by the node, and a next field that points to another node. Using this
    helper data structure, we can create a list of linked nodes in which the
    next value in the series is wrapped in the node pointed to in the "next"
    field.
    """
    #Properties
    _data = None
    _next = None
    _size = 0

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        assert type(node) == Node or type(node) == None, "The next data given is not a Node object"
        self._next = node

    #Methods
    def __init__(self, data=None, next=None):
        """
        Constructor:
        """
        self._data = data
        self._next = next

    def insert(self, value):
        """
        Procedure: Adds another node at the end of the series of nodes.
        """
        #Case 1: assume value is a Node object
        node = value
        #Case 2: Else, change value into a Node object
        if type(node) != Node:
            node = Node(value)
        #Use a current and scout probe to interatively insert a node
        current = self
        scout = self._next
        while scout != None:
            current = scout
            scout = scout.next
        current.next = node


    def remove(self, value):
        """
        Procedure: Remove the first instance of a piece of data from the
        series of nodes.

        Does not remove the node object wrapping the data from memory.
        """
        #Check the first node in the series

        #Use a current and scout probe to iteratively remove the value/nodes
        current = self
        scout = self._next
        while scout != None and scout.data != value:
            current = scout
            scout = scout.next
        if scout != None:
            current.next = scout.next
        else:
            return

    def find(self, value):
        """
        Checks if "value" is in the series of linked nodes. Returns True if
        the value is in the series and False if it isn't. O(N)

        This uses linear search to find the value.
        """
        #Use a current and scout probe to iteratively find the value/nodes
        current = self
        scout = self._next
        while scout != None and scout.data != value:
            current = scout
            scout = scout.next
        if scout != None:
            return True
        else:
            return False


class LinkedList(Node):
    """
    Instances represent a linked list data structure which can also be used to
    implement more specialized data structures such as a stacks, queues, and 
    priority queue.

    ===========
    Description
    ===========
    A linked list is a data structures consisting of a series of nodes. This
    one in particular simply subclasses the Node class and represents the 
    head of a linked list. This allows us to replace the first value of a 
    linked series of data a bit easier and lets us have a clear "tag" for 
    the beginning of the list. The header cannot contain list items.

    Most methods are inherited from the Node class other than remove.
    """
    #Methods
    def __init__(self, data=None, next=None, head_data="This is the head of the list."):
        """
        Constructor:
        """
        #Construct the LinkedList/Node object - the header of the list
        super(LinkedList, self).__init__(head_data, None)
        #Add the series of nodes after - the data of the list
        node_after_header = Node(data, next)
        self._next = node_after_header

    def remove(self, value):
        """
        Procedure: Remove the first instance of a piece of data from the
        series of nodes. Overwrites Node class remove to take the header
        node into accout (ignores it completely)

        Does not remove the node object wrapping the data from memory.
        """
        #Use a current and scout probe to iteratively remove the value/nodes
        current = self
        scout = self._next
        while scout != None and scout.data != value:
            current = scout
            scout = scout.next
        if scout != None:
            current.next = scout.next
        else:
            return


class DLList(Node):
    """
    Instances represent a doubly linked list data structure which can also 
    be used toimplement more specialized data structures such as a stacks, 
    queues, and priority queues.

    ===========
    Description
    ===========
    A linked list is a data structures consisting of a series of nodes. This
    one in particular simply subclasses the Node class and represents the 
    head of a linked list. This allows us to replace the first value of a 
    linked series of data a bit easier and lets us have a clear "tag" for 
    the beginning of the list. A doubly linked list ###Descritption###.

    Some methods are inherited directly from the node class.
    """
        
class TreeCell(object):
    """
    Instances represent a tree cell that can be used to build trees and ADT's

    ===========
    Description
    ===========
    A tree is a unique data structure.
    """
    pass

#=============================
#   Classic Data Structures
#=============================
class Bag(object):
    """
    Instances represent a list implementation of the bag data structure.

    ============
    Description:
    ============     
    The Bag data structure is a way of holding data in a manner that 
    resembles a bag.
    """
    #Properties
    _data = []              #Field:The list of data wrapped in a Bag
    _size = 0               #Field:The number of entries in the Bag
    _DEFAULT_CAPACITY = 25  #Field:The default size of a given Bag

    def __init__(self, data=[], DEFAULT_CAPACITY = 25):
        """
        Constructor: Create a new instance of a Bag data structure
        
        Precondition: data is a valid list of data
        """
        self._data = data
        self._size = len(self._data)
        self._DEFAULT_CAPACITY = DEFAULT_CAPACITY

    #Data Entry/Removal Methods
    def add(self, new_entry):
        self._data.append(new_entry)
        
    def remove(self):
        pass

    def clear(self):
        pass

    #Data Checking Methods
    def get_current_size(self):
        return self._size

    def is_full(self):
        pass

    def is_empty(self):
        if self._size <= 0:
            return True
        else:
            return False

    def contains(self):
        pass

    def get_frequency_of(self, entry):
        pass


class Stack(object):
    """
    Instances represent a list implementation of the Stack data structure.

    ============
    Description:
    ============ 
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

    ============
    Description:
    ============ 
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
        data = self._linked_list.data
        self._linked_list = self._linked_list.next
        return data

    def peek(self):
        return self._linked_list.data

    def remove(self):
        self._linked_list = self._linked_list.next

    def clear(self):
        #while there are still nodes in the linked list, remove the head.
        while self._linked_list.next != None:
            self.remove()
        #Then set the last node's data field to 0 usng a setter method.
        self._linked_list.data(None)


class Queue(object):
    """
    Instances represent a list implementation of the Queue data structure.

    ============
    Description:
    ============ 
    """
    pass


class LinkedQueue(object):
    """
    Instances represent a linked node/list implementation of the Queue
    data structure.

    ============
    Description:
    ============
    """
    pass


class PriorityQueue(object):
    """
    Instances represent a list implementation of the Priority Queue data 
    structure.

    ============
    Description:
    ============
    """
    pass


class HashTable(object):
    """
    Instances represent an implementation of the Dictionary/HashTable
    data structure.

    ============
    Description:
    ============
    """
    pass


#===========================
#   Other Data Structures
#===========================

#====================
#   Helper Methods
#====================