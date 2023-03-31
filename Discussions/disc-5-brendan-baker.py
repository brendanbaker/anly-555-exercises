# -*- coding: utf-8 -*-
'''
Discussion 5: Binary Heap
Brendan Baker

Prompt: Consider an array implementation of a binary heap. Given the strict balance constraint, an array implementation is very efficient and effective!
An n-ary heap is generalization of a Binary Heap that will allow for a branching factor of n.

1. Edit the code below so that one can create a heap with any branching factor (eg 3-ary heaps, 5-ary heaps, ... ). (Take care to assure the indexing is correct!!)
2. Create a __str__() member similar to the one implemented in the in-class exercise that allows you to visualize the tree using the tool found at: http://mshang.ca/syntree/
3. One main goal associated with trees is improved time complexity, but how is this related to the branching factor? For example, are 2-ary heaps more or less efficient than 5-ary heaps?
Propose an optimal value for n and justify your proposition with an extensive discussion and explanation.

'''
"""
Code created on Thu Oct 15 12:32:31 2020
"Array" implementation of heap using built-in lists
@author: jerem
"""


class NaryHeap:
    def __init__(self, n=2):
        self.heapList = [0]  # Initialize list of elements
        self.currentSize = 0  # Keeps track of size
        self.branching_factor = n  # Branching factor attribute

    def percUp(self, i):
        '''
        Percolates the value up the heaplist at index i to maintain the heap property.
        '''
        while i // self.branching_factor > 0:
            # Calculate the parent's index
            parent = (i - 1)//self.branching_factor
            # If the value at index i is less than the value at the parent's index
            if self.heapList[i] < self.heapList[parent]:
                # Swap the values
                self.heapList[i], self.heapList[parent] = self.heapList[parent], self.heapList[i]
            i = parent  # Set the index to be the parent

    def insert(self, k):
        '''
        Inserts a value into the heaplist.
        '''
        self.heapList.append(k) # Append the value to the end of the list
        self.currentSize = self.currentSize + 1 # Increment the size
        self.percUp(self.currentSize) # Percolate the value up the heaplist

    def percDown(self, i):
        '''
        Percolates a value down the heaplist at index i to maintain the heap property.
        '''
        while i*self.branching_factor - (self.branching_factor - 2) <= self.currentSize:
            mc = self.minChild(i) # Find the index of the minimum child
            if self.heapList[i] > self.heapList[mc]: 
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]  # Swap values down
            i = mc

    def minChild(self, i):
        '''
        Finds the index of the minimum child of the value at index i in the heapList.
        '''
        minIndex = i * self.branching_factor - (self.branching_factor - 2)  # Set initial minimum index
        for j in range(1, self.branching_factor):
            childIndex = i * self.branching_factor - (self.branching_factor - 2) + j  # Calculate child index
            if childIndex <= self.currentSize and self.heapList[childIndex] < self.heapList[minIndex]:
                minIndex = childIndex  # Update minimum index
        return minIndex

    def delMin(self):
        '''
        Deletes the minimum index of the heap
        '''
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        '''
        Constructs the heap based on the list of elements.
        '''
        i = (len(alist) + self.branching_factor - 2) // self.branching_factor # Starting index
        self.currentSize = len(alist) # Set the current size attribute
        self.heapList = [0] + alist[:] # Set the heapList attribute
        while (i > 0):
            self.percDown(i)
            i = i - 1
            
    def __str__(self):
        '''
        Prints the heap in a tree format
        '''
        def build_tree_string(index):
            if index > self.currentSize: # Base condition
                return "[None]"

            first_child_index = index * self.branching_factor - (self.branching_factor - 2) # Find the first child index
            children = []
            for j in range(self.branching_factor):
                current_child_index = first_child_index + j # Find the current child index
                if current_child_index <= self.currentSize: # If the current child index is within the heap
                    child_tree_string = build_tree_string(current_child_index) # Recursively build the child tree string
                    children.append(child_tree_string)

            return f"[{self.heapList[index]}{''.join(children)}]"

        return build_tree_string(1)
            
            


if __name__ == '__main__':
    nh = NaryHeap(3)
    nh.buildHeap([9,5,6,2,3,1,4,7,8,83])

    print(nh)
    print(nh.delMin())
    print(nh.delMin())
    print(nh.delMin())
    print(nh.delMin())
    print(nh.delMin())
    
    nh2 = NaryHeap(5)
    nh2.buildHeap([9,5,6,2,3,1,4,7,8,83])
    print(nh2)
    
    
'''
3. One main goal associated with trees is improved time complexity, but how is this related to the branching factor? 
For example, are 2-ary heaps more or less efficient than 5-ary heaps?
Propose an optimal value for n and justify your proposition with an extensive discussion and explanation.

Examining the heap operations separately: 

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INSERTION
Relies on percUp method. The dominant term would come from the line 

while i // self.branching_factor > 0:

This looks to be about O(log_n(t))

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DELETION
Relies on percDown method.  The dominant term with respect to time complexity from percDown would come from 

while i*self.branching_factor - (self.branching_factor - 2) <= self.currentSize:

percDown also relies on minChild, for which the dominant term would come from 

for j in range(1, self.branching_factor):

Which may approximate to O(n*log_n(t))


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




'''