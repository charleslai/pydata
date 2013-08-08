#Algorithms.py
#Charles J. Lai
#July 3, 2013
import random
import time

"""
==========
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
*linear search (iterative and recursive)
*binary search (iterative and recursive)
*bogosearch 

Sorting Algorithms: 
*insertion sort
*selection sort
*quick sort
*merge sort 
*shell sort

"""
#===========================
#   Searching Algorithms   
#===========================
def linear_search_i(sequence, value):
    """
    Returns: Index position of the searched value. If the value is not
    in the list, raise a ValueError. Runs in O(n) time. Function is an
    iterative function.

    Precondition: sequence is a mutable sequence (i.e. a list)

    ============
    Description:
    ============
    Linear search is a linear searching algorithm that runs in
    O(n) time. The algorithm iteratively checks if each value in the list is
    the value we are looking for or not. A common implementation is to check
    if the first value is the value we are looking for. If so, return the
    index. If not, run the algorithm again on the rest of the list. This is a
    naive searching algorithm that checks every value in the list until the
    value has been found: hence O(n).
    """

    #Initialize loop counter/return variable
    index = 0
    while index < len(sequence):
        #If the value is located, return the value
        if sequence[index] == value:
            return index
        index += 1
    #Else raise a value error
    raise ValueError


def linear_search_r(sequence, value):
    """
    Returns: True if value is found in the list. If the value is not in the list,
    raise a ValueError. Runs in O(n) time. Function is a recursive function.

    Precondition: sequence is a mutable list data structure

    ============
    Description: 
    ============
    This is a recursive implementation of the linear search
    algorithm described above. For more information about the algorithm,
    please read the description on the implementation above.
    """

    #Base case: If the length of the list is 0, raise a value error
    if len(sequence) == 0:
        raise ValueError
    #If the first value of the list is the right value, return a 0
    if sequence[0] == value:
        return 0
    #Else, recursively add index positions and call the function on the next portion of the list
    else:
        return 1 + linear_search_r(sequence[1:], value)


def binary_search_i(sequence, value):
    """
    Returns: Index position of the searched value. If the value is not in
    the list, raise a ValueError. Runs in O(log(n)) time. Function is iterative.

    Precondition: sequence is a mutable list already sorted from
    sequence[0...len(sequence)-1]

    ============
    Description: 
    ============
    Binary search is a divide-and-conquer searching algorithm
    that runs in O(log(n)) time. First the algorithm finds the middle of the
    list and checks if its greater than the goal value. If it is, then run the
    algorithm again on list[:middle] or values less than middle. Otherwise,
    run the algorithm again on the list[middle:] or values greater than the
    middle. If it is the same value, then we are done and return the index
    position of the value.

    You can see how the algorithm "divides" the list up and locates the value
    we want faster than the O(n) linear search algorithm. We don't have to
    check every single value this time to find it!
    """

    #Initialize start and end variables to use as flags for the while loop
    start = 0
    end = len(sequence)
    #While there are still values to be checked
    while start < end:
        middle = (start+end)/2
        #If the middle of the list is our value, return the middle index
        if sequence[middle] == value:
            return middle
        #Else run binary search on the middle to end if the middle of the sequence is
        #less than the value and vice versa if the middle is greater than the value
        elif sequence[middle] < value:
            start = middle + 1
        else:
            end = middle
    raise ValueError


def binary_search_r(sequence, value):
    """
    Returns: Index position o the searched value. If the value is not in the
    list, raise a ValueError. Runs in O(log(n)) time. Function is recursive.

    Precondition: sequence is a mutafble list already sorted from
    sequence[0...len(sequence)-1]

    ============
    Description: 
    ============
    This is a recursive implementation of the binary search algorithm
    described above. For more information about the algorithm, please read the
    description on the implementation above.
    """

    #If the length of the sequence is 0, return False.
    if len(sequence) == 0:
        raise ValueError
    if len(sequence) == 1 and sequence[0] != value:
        raise ValueError
    middle = len(sequence)/2
    #If the middle of the sequence is our value, return the middle position.
    if sequence[middle] == value:
        return middle
    #Else call binary search on the middle to end if the middle of the sequence is
    #less than the value and vice versa if the middle is greater than the value
    elif sequence[middle] < value:
        return middle + binary_search_r(sequence[middle:], value)
    else:
        return binary_search_r(sequence[:middle], value)


def bogo_search(sequence, value, counter=20):
    """
    Returns: Index position of the searched value. If the value is not in 
    the list, raise a ValueError. Default counter value is 20 seconds.

    ============
    Description: 
    ============
    This is a very naive searching algorithm that simply
    checks random index positions in the list until the value we are looking
    for has been found or we hit our defined counter value.
    """

    #Initialize the starting time because time.clock is not fixed.
    starting_time = counter + time.clock()
    while True:
        #Select the ranom index position and check if its the value.
        index = random.randint(0, len(sequence)-1)
        if sequence[index] == value:
            return index
        #If time runs out, return a value error
        if time.clock() >= starting_time:
            raise ValueError


#========================
#   Sorting Algorithms   
#========================
def bubble_sort(sequence):
    """
    Procedure: Sorts the list in O(n^2) worst case time. 

    Precondition: sequence is a mutable sequence i.e. a list

    ============
    Description: 
    ============
    BubbleSort is an iterative, linear sorting algorithm that
    runs in O(n^2) time. this algorithm works by "bubbling" each element up
    the list into its sorted order. After each iteration, the amount of
    unsorted elements in the list decreases by 1 - the max value is at the end
    of the list. This process continues until all of the elements in the list
    are in sorted order. We can see we have to compare n + n-1 + n-2 ...
    elements in the list each time which results in n(n+1)/2 comparisons and
    thus O(n^2) time.
    """

    #Initialize the first n sized loop counter, index of end of unsorted values.
    end = len(sequence) - 1
    while end > 0:
        #Bubble up values from the beginning to end index into sorted position. Helper procedure runs in O(n) time.
        _bubble_up(sequence, end)
        #Decrement end index by one and reiterate
        end += -1


def insertion_sort(sequence):
    """ 
    Procedure: sorts the sequence in O(n^2) worst case time. 

    Precondition: sequence is a mutable sequence i.e. a list

    ============
    Description: 
    ============
    Insertion sort is similar to the bubble sort; it's a
    iterative, linear sorting algorithm that runs in O(n^2) time. The
    difference is two-fold. It starts from a small portion of a list, sorts
    it, and then runs again on an iteratively larger portion of the list such
    that the loop invariant maintains a sorted list after each sorting
    iteration. And, where bubble sort "bubbles" up the list, the insertion
    pushes each value of the list down into its sorted position.
    """

    #Initialize the first n sized loop counter, index of start of unsorted values
    index = 0
    while index < len(sequence):
        #Push down the value from end to start index into sorted position. Helper procedure runs in O(n) time.
        _push_down(sequence, index)
        #Increase start index by one and reiterate
        index += 1


def selection_sort(sequence):
    """ 
    Procedure: sorts the sequence in O(n^2) worst case time. 

    Precondition: sequence is a mutable sequence i.e a list

    ============
    Description:
    ============ 
    Insertion sort is similar to the bubble sort; it's a
    iterative, linear sorting algorithm that runs in O(n^2) time. The
    difference is two-fold. It starts from a small portion of a list, sorts
    it, and then runs again on an iteratively larger portion of the list such
    that the loop invariant maintains a sorted list after each sorting
    iteration. And, where bubble sort "bubbles" up the list, the insertion
    pushes each value of the list down into its sorted position.
    """

    #Initialize the first n sized loop counter, index of start of unsorted values
    start = 0
    while start < len(sequence):
        #Find the minimum value of the list from the start value's index value
        min = _find_min(sequence[start:]) + start
        #If the start value is greater than the minimum of the unsorted portion, swap the two
        if sequence[start] > sequence[min]:
            _swap(sequence, start, min)
        #Increase start index by one and reiterate
        start += 1


def quick_sort(sequence, start=0, end=None):
    """
    Procedure: Sorts the list in O(nlog(n)) average case time in place.
 
    Parameters: Takes a start and end argument. Default arguments is the
    beginning index of the list for start and the end index of the list for
    the end.

    Precondition: start and end are valid indices of the list and start < end.
    sequence is a mutable sequence, i.e., a list.

    ============
    Description:
    ============
    QuickSort is a recursive, divide-and-conquer sorting
    algorithm in O(nlog(n)) time. This algorithm works by heuristically
    locating a "pivot" position (we'll assume the list is equi-disordered so
    we'll simply take the beginning of the list as the pivot).

    On our first recursive call, we partition the list around the pivot such that
    values greater than or equal to the pivot are moved after it and values
    less than the pivot are moved before it. The list will then look like:
    [...smaller values..., pivot,...larger values...]. Then we call quick sort
    on both the lower half of the list and upper half of the list. We can see
    that this process of recursive partitioning results in log(n) dividing
    function calls with n comparisons. The function is thus O(nlog(n)) average
    time complexity for sorting a list.
    """

    #I can't put a default length function targeting the "sequence" parameter in the header, so I check for None
    if end is None:
        end = len(sequence) - 1
    #The base case: If the start and end indices are the same or start > end, return and do nothing
    if end - start < 1:
        return
    #Partition the list by a pivot. Values less than the pivot go before the pivot and vice versa for
    #values greater than the pivot. This runs in O(n)
    pivot = _partition(sequence, start, end)
    #Recursively call quick sort of the left side of list before the pivot and the right side of the list
    #after the pivot - we essentially recursively partition until the list is sorted! O(log(n)) time.
    quick_sort(sequence, start, pivot - 1)
    quick_sort(sequence, pivot + 1, end)


def merge_sort(sequence):
    """
    Returns: A newly sorted list from an unsorted list. Not sorted in place.

    Precondition: sequence is a mutable sequence (i.e. a list)

    ============
    Description: 
    ============
    Merge sort is a divide-and-conquer sorting algorithm that runs 
    in O(nlog(n)) time.
    """
    if len(sequence) > 1:
        middle = len(sequence)/2
        left = merge_sort(sequence[:middle])
        right = merge_sort(sequence[middle:])
        return _merge(left, right)
    return sequence


def heap_sort(sequence):
    """ 
    Returns: A newly sorted list using the O(nlog(n)) heap sort algorithm.

    Precondition: sequence is a mutable sequence (i.e. a list)
 
    ============
    Description:
    ============ 
    Heapsort is a divide-and-conquer sorting algorithm that runs
    in O(nlog(n)) time. This algorithm works by creating a balanced min-heap
    data structure out of a list/sequence. [explain what a balanced min-heap is
    here]. 

    After the heap is created, the heap data structure is repeatedly
    popped to get the minimum value (n times) and placed into a new, sorted
    list. After each pop, the heap is resorted in order to maintain the
    balanced, min-heap invariant (log n steps). We can see that after this, we
    recieve a sorted list from O(nlog(n)) time complexity.
    """

    #Step 1: Make a heap out of the list with our heapify helper function
    heap = _heapify(sequence)
    #Step 2: Use the heap and: repeatedly extract the root value (min), maintain heap order, and
    #append into a new list. This new list will be the heap sorted sequence that is returned.
    sorted_list = []
    while len(heap) > 0:
        #Extract the min element (root) from the heap
        sorted_list.append(heap[0])
        heap.remove(heap[0])
        #Case 0: If the heap has only one element left, add it to the sorted list, and break out by returning the
        #sorted list
        if len(heap) == 1:
            sorted_list.append(heap[0])
            return sorted_list
        #After extraction, pop the last value of the heap and add it to the top of the heap
        heap.insert(0, heap.pop())
        #Maintain the heap invariant
        root = 0
        heap_invariant = False
        while not heap_invariant:
            left_child = 2 * root + 1
            right_child = 2 * root + 2
            smallest_child = None
            #Case 1: There isn't a left child (and hence no children) - Heap invariant is maintained and break out
            if left_child > len(heap) - 1:
                heap_invariant = True
                break
            #Case 2: There is only a left child - Test the heap invariant on that child only and then break out
            if right_child > len(heap) - 1:
                smallest_child = left_child
                if heap[root] <= heap[smallest_child]:
                    heap_invariant = True
                elif heap[root] > heap[smallest_child]:
                    _swap(heap, root, smallest_child)
                    heap_invariant = True
                break
            #Case 3: There are two children - Test the heap invariant normally: Find the smallest child and compare with root
            if heap[left_child] <= heap[right_child]:
                smallest_child = left_child
            if heap[right_child] < heap[left_child]:
                smallest_child = right_child
            #Swap down the root if its greater than the smallest child, else the invariant
            #is already met
            if heap[root] <= heap[smallest_child]:
                heap_invariant = True
            if heap[root] > heap[smallest_child]:
                _swap(heap, root, smallest_child)
                root = smallest_child


def shell_sort(sequence):
    """
    Procedure: Sorts an sequence/list in-place

    Preconditions: sequence is a mutable sequence i.e. a list

    ===========
    Descrition:
    =========== 
    Shell Sort is a variant of insertion sort that
    is optimized for large sequences. A series of gaps are initialized
    and an insertion sort is done for each gap size - the value that the
    sort is incremented. This allows us to prep large sequences by "half-sorting"
    them. The final gap is of size 1 where a normal insertion sort occurs
    with - hopefully - less steps than a typical insertion sort.
    """

    #List of gaps for the algorithm - Marcin Ciura Default Gaps
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    #Iterate through the algorithm for each gap
    for gap in gaps:
        i = gap
        #Do an insertion sort for each gap size
        while i < len(sequence):
            temp = sequence[i]
            j = i
            while j >= gap and sequence[j - gap] > temp:
                sequence[j] = sequence[j - gap]
                j -= gap
            sequence[j] = temp
            i += 1



def radix_sort(sequence):
    pass


def bogo_sort(sequence):
    """
    Returns: A sorted list using the bogosort sorting algorithm.

    Precondition: sequence is a mutable sequence (i.e. a list)

    ===========
    Decription:
    =========== 
    Bogosort is a joke in the computer science community. It has a
    best case time complexity of O(1) and a worst case of O(Inf). The
    algorithm works by shuffling the sequence completely. If the sequence is sorted,
    return it. Otherwise, shuffle it again.

    There's even another variant called bogobogosort which is designed to not
    finish until the heat death of the universe.
    """

    #While the sequence is not in order, shuffle it
    while not _in_order(sequence):
        random.shuffle(sequence)
    return sequence


def bogobogo_sort(sequence):
    """
    Returns: a sorted list using the bogobogosort sorting algorithm.

    Precondition: sequence is a mutable sequence (i.e. a list)

    ===========
    Decription: 
    ===========
    Bogobogo sort is bogosort taken to the next level. The time
    complexity of the algorithm is O(Infinity). For a very large sized list, the
    algorithm will NOT finish until the heat death of the universe
    which makes this algorithm impossible to complete. They sort of took a
    joke and took it way too far.
    """

    while not _in_order(sequence):
        counter = 1
        while counter < len(sequence) - 1:
            #Shuffle the sequence from the beginning to the counter
            temp_array = random.shuffle(sequence[:counter])
            #If it's in order, increment the counter and shuffle again
            if _in_order(temp_array):
                counter += 1
            #Else, start over
            else:
                counter = 1
        return temp_array


#======================
#   Helper Functions
#======================
def _swap(sequence, a, b):
    """
    Procedure: Swaps the values of a and b in a mutable list called sequence.

    Note: I'm not sure if this is worth making a helper but I might as well
    for readability I guess.
    """

    #Swap the sequence values in one line!
    sequence[a], sequence[b] = sequence[b], sequence[a]


def _bubble_up(sequence, a):
    """
    Procedure moves the value at position index into its sorted position 
    in sequence[1...a]. This is a helper function for algorithms such as 
    bubble_sort.

    Preconditon: sequence[1...a] is a sorted mutable sequence (i.e. a list)
    """

    #Initialize the n sized loop counter
    index = 0
    while index < len(sequence[:a]):
        #Swap positions if the value above index is less
        if sequence[index + 1] < sequence[index]:
            _swap(sequence, index + 1, index)
        index += 1


def _push_down(sequence, a):
    """
    Procedure moves the value at position a into its sorted position in
    sequence[0...a-1]. This is a helper function for algorithms such as insertion
    sort.

    Precondition: sequence[0...a-1] is a sorted mutable sequence (i.e. a list)
    """

    #Initialize the n sized loop counter
    index = a
    while index > 0:
        #Swap positions if the value below index is greater
        if sequence[index - 1] > sequence[index]:
            _swap(sequence, index - 1, index)
        index += -1


def _find_min(sequence):
    """
    Returns: Index position of the minimum value of a list.
    this is a helper function for algorithms such as selection sort.
    Runs in O(n) time.
    """

    #Initialize loop counter and return index
    index = 0
    counter = 0
    while counter < len(sequence):
        #If the "scouting" counter is less than the return index, set index equal to the counter
        if sequence[counter] < sequence[index]:
            index = counter
        counter += 1
    #Return the min index position
    return index


def _partition(sequence, start, end):
    """
    Returns: Index position of the pivot after the partitioning

    Preconditions: sequence is a mutable sequence (i.e. a list) and pivot and end
    are valid index positions of the sequence.

    ============
    Description:
    ============ 
    Partitions the sequence[start...end] around the pivot - sequence[start] -
    where the pivot is the first position in the unpartitioned list.
    """

    #Initialize the pivot value and loop counters that will iterate towards completion of the algorithm
    #i is the end of the first partition range and j is before the start of the second partition range
    #such that [start.....i-1 | pivot or i | j ...... end] will be the result of the procedure.
    i = start
    j = end
    pivot = sequence[i]  #at this point sequence[i] is the same as sequence[start]
    while i < j:
        #If the value after i is greater than the pivot, swap j and the value and decrease the j counter
        #by 1 (i.e. put that value after the pivot as far as possible)
        if sequence[i + 1] >= pivot:
            _swap(sequence, i + 1, j)
            j = j - 1
        #Else, swap the value and the i position value (i.e. put the value before the pivot)
        else:
            _swap(sequence, i + 1, i)
            i = i + 1
    return i


def _merge(left, right):
    """
    Returns: New list by merging two different sequences together in sorted
    order. 

    ============
    Description:
    ============ 
    This is a helper function for the Mergesort algorithm.
    """

    new_list = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            new_list.append(left[left_index])
            left_index += 1
        else:
            new_list.append(right[right_index])
            right_index += 1
    if left_index >= len(left):
        new_list = new_list + (right[right_index:])
    else:
        new_list = new_list + (left[left_index:])
    return new_list


def _heapify(sequence):     
    """     
    Returns: A balanced min-heap data structure with elements from sequence.

    Precondition: sequence is a mutable sequence (i.e. a list)

    ============
    Description:
    ============ 
    This algorithm runs in O(nlog(n)) time complexity and is a
    helper function for the heap sort algorithm.
    """

    #Initialize our iterative variables: heap_invariant as a logic gate for maintaining
    #heap invariant during heap creation, counter for looping, and an empty list
    #for our heap.
    counter = 0
    heap = []
    #Insert all elements into a heap
    while counter < len(sequence):
        #Add the list value to the bottom of the heap
        heap.append(sequence[counter])
        #Maintain the heap invariant
        child = len(heap) - 1
        heap_invariant = False
        while not heap_invariant:
            #If the child is at the root - The heap invariant is satisfied and break out of the loop
            if child == 0:
                break
            #Else, compare the child with the parent. If the child is less than the parent, swap it up.
            parent = (child - 1)/2
            if heap[child] >= heap[parent]:
                heap_invariant = True
            elif heap[child] < heap[parent]:
                _swap(heap, child, parent)
                child = parent
        #Repeat until all elements of the list are in a heap
        counter += 1
    return heap


def _in_order(sequence):
    """
    Returns: True if the sequence is in order, else it returns false.
    """

    counter = 0
    #Check until the counter is at the second to last index - avoid index error
    while counter < len(sequence) - 1:
        if sequence[counter] > sequence[counter + 1]:
            return False
        counter += 1
    return True

if __name__ == '__main__':
    #=========================================#
    #           TESTING APPLICATION           #
    #=========================================#
    print "INSERTION SORT:"
    b = [random.randint(1,10) for _ in range(5000)]
    insertion_sort(b)
    print `b`
    #=========================================#
    print "BUBBLE SORT:"
    b = [random.randint(1,10) for _ in range(5000)]
    bubble_sort(b)
    print `b`
    #=========================================#
    print "SELECTION SORT:"
    b = [random.randint(1,10) for _ in range(5000)]
    selection_sort(b)
    print `b`
    #=========================================#
    print "QUICK SORT:"
    b = [random.randint(1,10) for _ in range(5000)]
    quick_sort(b)
    print `b`
    #=========================================#
    print "HEAP SORT:"
    b = [random.randint(1,10) for _ in range(5000)]
    d = heap_sort(b)
    print `d`
    #=========================================#
    print "MERGE SORT:"
    b = [random.randint(1,10) for _ in range(5000)]
    b = merge_sort(b)
    print `b`
    #=========================================#
    print "SHELL SORT:"
    b = [random.randint(1,10) for _ in range(5000)]
    shell_sort(b)
    print `b`


















































































