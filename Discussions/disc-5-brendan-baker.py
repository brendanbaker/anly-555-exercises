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

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())