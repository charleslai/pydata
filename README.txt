======
PyData
======

PyData provides modules for various implementations of data
stuctures as well as algorithms and tools for analyzing/manipulating
them. 

These modules are mainly focused around *new* students of computer
science and thusly contain name focused variables as well as longer
comments and explanations in order to describe some of the uses of 
each algorithm/data structure (i.e. explaining how quicksort works 
or what a priority queue is).

Algorithms
==========
Module of different searching and sorting algorithms. These algorithms will
look slightly different in python than java because lists are mutable. This
way, we dont have to create a new data structure for creating partions for
various divide and conquer algorithms which reduces the need for a bunch of
new variables in recursive call stacks

The module includes a lot of excessive comments that will explain what each
algorithm is doing which I think will be useful to new computer science 
students.

Contents
--------
Searching Algorithms: 
* Linear Search (iterative and recursive)
* Binary Search (iterative and recursive)
* Bogosearch 

Sorting Algorithms: 
* Insertion Sort
* Selection Sort
* Quick Sort
* Merge Sort 
* Shell Sort
* Radix Sort
* Bogo Sort
* Bogobogo Sort

Data Structures
===============
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
