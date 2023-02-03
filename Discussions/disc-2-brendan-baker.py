'''
This script contains two classes. 

The first class is a matrix class that allows for matrix addition and multiplication.  If addition and multiplication are not possible, an error is raised.

The second class is a vector class that inherits from the matrix class. It specifically inherits addition and multiplication, but it also extends to outer product.
'''

class Matrix:
    '''Represents a multidimensional matrix'''
    
    def __init__(self, rows, cols, values = None):
        '''
        
        Creates a matrix with the specified number of rows and columns
        If values are provided as an iterable, the matrix is set to those values in rowwise order
        Otherwise, the matrix is initialized as all zeroes.
        
        '''
        
        self._rows = rows # Set number of rows
        self._cols = cols # Set number of columns
        self._matrix = [[0 for i in range(cols)] for j in range(rows)] # Create a list of lists in the specified rowXcol format
        self.shape = [self._rows, self._cols] # Add a shape attribute
        
        if values is not None: # If values are provided, set the matrix to those values
            if len(values) == self._rows*self._cols: # Check if the number of values matches the number of rows and columns
                matrix = [] # Create a list to hold the matrix
                row_vec = [] # Create a list to hold the row vector
                for i, j in enumerate(values):
                    row_vec.append(j)
                    if (i+1) % cols == 0: # If the number of values in the row vector is equal to the number of columns, append the row vector to the matrix and reset the row vector
                        matrix.append(row_vec)
                        row_vec = []
                self._matrix = matrix # Set the matrix values to the matrix
            else:
                raise ValueError('invalid number of values')
    def __str__(self):
        """Produce string representation of matrix when printing."""
        return str(self._matrix) # print list representation
    
    def __add__(self, other):
        '''
        
        Adds two matrices together if they are the same shape
        If the matrices are not the same shape, an error is raised
        
        '''
        
        if self.shape == other.shape: # If the shapes are equal
            new_values = []
            for i in range(self._rows): # Add the values with the same coordinates
                for j in range(self._cols):
                    new_values.append(self._matrix[i][j] + other._matrix[i][j]) # Add these values to a new matrix
            return Matrix(self._rows, self._cols, values = new_values)
        else:
            raise ValueError("incompatible dimensions!") # If the dimensions are not the same, raise an error
    
    def __mul__(self, other):
        '''
        Multiplies to matrices together if the number of columns of the first matrix matches the number of rows of the second matrix.
        '''
        if self.shape[1] == other.shape[0]: # If columns of first matrix match columns of second matrix
            new_values = [] 
            for i in range(self._rows): # Iterate through the rows of the first matrix
                for j in range(other._cols): # Iterate through the columns of the second matrix
                    val = 0
                    for k in range(other._rows): # Iterate through the rows of the second matrix
                        val += self._matrix[i][k] * other._matrix[k][j] # Multiply the corresponding values and add them to the total for that location
                    new_values.append(val)
            return Matrix(self._rows, other._cols , values = new_values)
            
        else:
            raise ValueError("incompatible dimensions!")
                
class Vector(Matrix):
    '''
    A vector class that inherits from the matrix class.
    Specifically inherits addition and multiplication (inner product), but also extends to outer product.
    '''
    
    def __init__(self, cols, values = None):
        '''
        Creates a vector with the specified number of values.
        If values are provided as an iterable, the vector is set to those values in rowwise order
        Otherwise, the vector is initialized as all zeroes.
        '''
        super().__init__(1, cols, values) # Initialize the vector as a matrix with 1 column
    
    def __mul__(self, other):
        '''
        Multiplies two vectors together if they are the same length. (small extension since an error will be thrown if col A != row B)
        '''
        return Matrix(1, self._cols, values=self._matrix[0]) * Matrix(other._cols, 1, values=other._matrix[0])
    
    def __rshift__(self, other):
        '''
        Calculates the outer product of two vectors.
        '''
        
        # Get the values of the vectors in a list
        a = self._matrix[0]
        b = other._matrix[0]
        
        new_values = []
        for i in range(len(a)): # Number of rows
            for j in range(len(b)): # Number of columns
                new_values.append(a[i]*b[j]) # Multiply the corresponding values and add them to the total for that location
        return Matrix(len(a), len(b), values = new_values)
                
            
        
        
    
    
if __name__ == "__main__":
    
    # Matrix class
    mat_1 = Matrix(3, 2)
    print("Matrix shape: ") # Show the shape of the matrix
    mat_1.shape
    mat_2 = Matrix(3, 2, range(6))
    print("Matrix with iterable values: ") # Show the matrix given an iter
    print(mat_2)
    
    # Matrix addition
    added = Matrix(2, 2, range(4)) + Matrix(2, 2, range(4)) # Matrix addition
    added
    
    # Matrix multiplication
    a = Matrix(2, 3, values = [1,4,-2,3,5,-6])
    b = Matrix(3, 4, values = [5,2,8,-1,3,6,4,5,-2,9,7,-3])
    mult = a*b  # Matrix multiplication
    print("Matrix multiplication: ")
    print(a)
    print(b)
    print(a*b)
    
    # Vector class
    print("Vector inheritance: ")
    print(Vector(3)) # Create a vector with 3 values
    
    # Vector addition
    print("Vector addition: ")
    print(Vector(3, range(3)) + Vector(3, range(3))) # Vector addition
    
    
    v = Vector(3, range(3))
    v._matrix
    
    # Vector multiplication
    print("Vector multiplication")
    print(Vector(3, range(3)) * Vector(3, range(3))) # Vector multiplication

    
    # Vector outer product
    u = Vector(3, [1,2,3])
    v = Vector(2, [4,5])
    print(u >> v)
    
    