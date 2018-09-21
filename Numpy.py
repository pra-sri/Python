import numpy as np

# Declaration of 2D array
a=np.array([(1,2,3,4),(4,5,6,7),(7,8,9,10)])
b=np.array([(10,9,8,7),(7,6,5,4),(4,3,2,1)])



print("1st array is : \n",a)
print("2nd array is : \n",b)
# Basic operations of Numpy

# to check the
# 1. Dimension
print("Dimension of 1st array : \n",a.ndim)
print("Dimension of 2nd array : \n",b.ndim)

# 2. Size of each elements
print("Size of each element of 1st array : \n",a.itemsize)
print("Size of each element of 2nd array : \n",b.itemsize)

# 3. Data Type
print("Data Type of 1st array : \n",a.dtype)
print("Dtat Type of 2nd array : \n",b.dtype)

# 4. Size of the array
print("Size of 1st array : \n",a.size)
print("Size of 2nd array : \n",b.size)

# 5. Shape of the array
print("Shape of 1st array : \n",a.shape)
print("Shape of 2nd array : \n",b.shape)

# 6. To change the shape
print("Reshaped 1st array is : \n",a.reshape(6,2))
print("Reshaped 2nd array is : \n",b.reshape(6,2))

# Linespace 
c= np.linspace(1,5,10)
#(start,stop,x) where x is the no of elements b/w start & stop with equal difference
print("Linespace b/w 1 & 5 is :",c)


# To find Max. Min. & Sum of elements
print("Maximun element in 1st array : \n",a.max())
print("Maximun element in 2nd array : \n",b.max())
print("Minimum element in 1st array : \n",a.min())
print("Minimum element in 2nd array : \n",b.min())
print("Sum of elements of 1st array : \n",a.sum())
print("Sum of elements of 2nd array : \n",b.sum())

# For Square Root of each element
print("Square root of elements of 1st array : \n",np.sqrt(a))
print("Square root of elements of 2nd array : \n",np.sqrt(b))

# For Standard Deviation of each elements
print("Standard Deviation of elements of 1st array : \n",np.std(a))
print("Standard Deviation of elements of 2nd array : \n",np.std(b))

# BASIC MATRIX OPERATIONS USING Numpy LIBRARY
print("Addition of both the array is : \n",a+b) #Addition of Corresponding elements
print("Subtraction of both the array is : \n",a-b) #Subtraction of Corresponding elements
print("Multiplication of both the array is : \n",a*b) #Multiplication of Corresponding elements
print("Division of both the array is : \n",a/b) #Division of Corresponding elements
print("Concatination of both the array, vertically, is : \n",np.vstack((a,b))) #concat vertically 
print("Concatination of both the array, horizontally, is : \n",np.hstack((a,b))) #concat hrizontally

#to make 1xN matrix
print("Single coloumned array of 1st array is : \n",a.ravel())
print("Single coloumned array of 2nd array is : \n",b.ravel())

#to find expotential of each elements
print("Expotential of every elements of 1st array is : \n",np.exp(a))
print("Expotential of every elements of 2nd array is : \n",np.exp(b))

#Logarithmic Operations
print("Natural Log of every elements of 1st array is : \n",np.log(a))
print("Natural Log of every elements of 2nd array is : \n",np.log(b))
print("Log base 10 of every elements of 1st array is : \n",np.log10(a))
print("Log base 10 of every elements of 2nd array is : \n",np.log10(b))
