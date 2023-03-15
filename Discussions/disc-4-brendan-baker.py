'''
Module 4 Discussion - Sparse Matrix
Brendan Baker

Design a sparse matrix class that supports matrix addition.  The goals is to make it as efficient as possible by only adding nonzero elements.
'''

class SparseMatrix:
    '''
    Creates a sparse matrix class that keeps track of nonzero elements for faster addition. 
    '''
    def __init__(self, rows, cols):
        # Set attributes
        self.rows = rows # Rows
        self.cols = cols # Columns
        self.values = {} # Values
        
    def setitem(self, row, col, value):
        
        if row > self.rows-1 or col > self.cols-1:
            raise ValueError("Index out of range")
        elif value == 0: # Only save an element if it is nonzero
            if (row, col) in self.values:
                del self.values[(row, col)]
        else:
            self.values[(row,col)] = value # Set the key to be row and column
        
        
    def __add__(self, other):
        '''
        Matrix addition that only adds nonzero elements.
        '''
        # Check if matrices are the same size, otherwise, raise an error
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrices must be the same size.')
        else: 
            # Do the addition
            for i in range(self.rows):
                for j in range(self.cols):
                    if (i,j) in self.values and (i,j) in other.values:
                        self.values[(i,j)] += other.values[(i,j)]

            # Return a new matrix 
            newmat = SparseMatrix(self.rows, self.cols)
            newmat.values = self.values
            return(newmat)
    
    def __str__(self):
        '''
        String representation of sparse matrix
        '''
        # Sparse representation
        return(str(self.values))
    
    def printfull(self):
        '''
        Full represenation of sparse matrix
        '''
        rep_list = [[0 for i in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                if (i,j) in self.values:
                    rep_list[i][j] = self.values[(i,j)]
        print(rep_list)


if __name__ == "__main__":
    a = SparseMatrix(3,3)
    # Set some values for a
    a.setitem(0,1,3)
    a.setitem(0,2,5)
    a.setitem(2,2,5)
    
    # Print
    print(a)
    a.printfull()
    
    # Set some values for b
    b = SparseMatrix(3,3)
    b.setitem(0,2,5)
    
    # Add a and b
    c = a + b
    
    # Print c both ways
    print(c)
    c.printfull()   
        
        
'''
Step count function T(n)

(For the addition portion only)

# Do the addition
for i in range(self.rows): # m steps
    for j in range(self.cols): # m*n steps
        if (i,j) in self.values and (i,j) in other.values: # m*n steps (evaluated every time)
            self.values[(i,j)] += other.values[(i,j)] # A or B steps

# Return a new matrix 
newmat = SparseMatrix(self.rows, self.cols) # 1 step
newmat.values = self.values # 1 step
return(newmat) # 1 step


Final function: 
m*n + m + 2m*n + A/B

The linear term would be dominant so I think this would be a linear step count with O(n) as the upperbound. 


Space count function S(n)

Both matrices only have as many items as nonzero values, so assuming each space is key-value pair, the bound would be O(A + B).


Final thoughts: I believe this is an efficient solution with respect to space, but it could be more efficient with respect to time if the loop did not run MxN times. 

'''                        
                    
            

        