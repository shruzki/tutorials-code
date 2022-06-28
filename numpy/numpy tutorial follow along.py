import numpy as np

# a = np.array([1,2,3])
# print(a)

# b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
# print(b)

# get dimension
# print(a.ndim)
# print(b.ndim)

# get shape
# print(a.shape)
# print(b.shape)

# get type
# print(a.dtype)
# print(b.dtype)

# different size
# c = np.array([1,2,3], dtype='int16')
# print(c)
# print(c.dtype)

# get size
# print(a.itemsize)
# print(c.itemsize)

# number of elements
# print(a.size)
# print(c.size)

# total size
# print(a.size * a.itemsize)
# print(c.size * c.itemsize)

# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

# accessing/changing specific elements, rows, columns - nparray[r, c]
# print(a)
# print(a[1, 5])
# print(a[1, -2])
# print(a[0, 0])

# get a specific row
# print(a[0, :])

# get a specific column
# print(a[:, 2])

# getting a little more fancy [startindex:endindex:stepsize]
# print(a[0, 1:6:2])
# print(a[0, 1:-1:2])

# a[1,5] = 20 # replacing 13
# print(a)

# a[:, 2] = 5 # replacing any row 3rd column with 5s
# print(a)

# a[:, 2] = [1,2]
# print(a)


# 3D example
# b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b)

# get specific element
# work outside in
# print(b[0,1,1])
# print(b[:,1,:])
# print(b[:,0,:])

# replace
# print(b[:,1,:])
# b[:,1,:] = [[9,9],[8,8]]
# print(b[:,1,:])
# print(b)


# initializing different types of arrays
# all 0s matrix
# print('1D\n',np.zeros(5))
# print('2D\n',np.zeros((2,3)))
# print('4D\n',np.zeros((4,3,3,2)))

# all 1s matrix
# print(np.ones((4,2,2), dtype='int32'))

# any other number
# print(np.full((2,2),99))
# print(np.full((2,2),99, dtype='float32'))

# a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(np.full_like(a, 4))

# Random decimal numbers
# print(np.random.rand(4,2))
# print(np.random.rand(4,2,3))
# print(np.random.random_sample(a.shape))

# random integer values
# print(np.random.randint(7, size=(3,3))) # selects from 0-6 (7 is not inclusive)
# print(np.random.randint(4,7, size=(3,3)))
# print(np.random.randint(-4,8, size=(3,3)))

# identity matrix
# print(np.identity(3))
# print(np.identity(5))

# repeat an array
# arr = np.array([1,2,3])
# r1 = np.repeat(arr,3)
# print(r1)

# arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,3, axis=0)
# print(r1)
# r2 = np.repeat(arr,3, axis=1)
# print(r2)

# ex = np.ones((5,5))
# print(ex)

# my solution
# ex[1:4,1:4] = 0
# print(ex)
# ex[2,2] = 9
# print(ex)

# instructor's solution
# z = np.zeros((3,3))
# z[1,1] = 9
# print(z)
# ex[1:4,1:4] = z
# print(ex)

####### Be careful when copying arrays
# a = np.array([1,2,3])
# print(a)
# b = a
# print(b)
# b[0] = 100
# print('b', b)
# print('a', a)

# a = np.array([1,2,3])
# b = a.copy()
# b[0] = 100
# print('b',b)
# print('a',a)

# MATHEMATICS
# a = np.array([1,2,3,4])
# print(a)

# print(a+2)
# a += 2

# print(a+2)
# print(a-2)
# print(a*2)
# print(a/2)

# b = np.array([1,0,1,0])
# print(a+b)

# print(a ** 2)

# take the sine/cosine
# print(np.sin(a))
# print(np.cos(a))

# LINEAR ALGEBRA
# a = np.ones((2,3))
# print(a)

# b = np.full((3,2),2)
# print(b)
### throws an error -  print(a*b)
# print(np.matmul(a,b))

# Find the determinant
# c = np.identity(3)
# print(np.linalg.det(c))

# STATISTICS
# stats = np.array([[1,2,3],[4,5,6]])
# print(stats)
# print(np.min(stats))
# print(np.min(stats, axis=0))
# print(np.min(stats, axis=1))
# print(np.max(stats))

# print(np.sum(stats))

# Reorganizing arrays
# before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)

# after = before.reshape((8,1))
# print(after)

# print(before.reshape((4,2)))
# print(before.reshape((2,2,2)))

# vertically stacking matrices/vectors
# v1 = np.array([1,2,3,4])
# v2 = np.array([5,6,7,8])

# print(np.vstack([v1,v2]))
# print(np.vstack([v1,v2,v2,v2]))
# print(np.vstack([v1,v2,v1,v2]))

# horizontal stack
# h1 = np.ones((2,4))
# print(h1)
# h2 = np.zeros((2,2))
# print(h2)
# print(np.hstack((h1,h2)))

# MISCELLANEOUS
# filedata = np.genfromtxt('data.txt', delimiter=',')
# print(filedata)
# if we want this to be integer
# filedata = filedata.astype('int32')
# print(filedata)


# BOOLEAN MASKING AND ADVANCED INDEXING
# print(filedata > 50)
# print(filedata[filedata > 50])

# a = np.array([1,2,3,4,5,6,7,8,9])
# print(a[[1,2,8]])

# print(filedata)
# print(np.any(filedata>50, axis=0)) # if any of the numbers in a particular column is >50
# print(np.all(filedata>50, axis=0)) # if all of the numbers in a particular column is >50
# print(np.any(filedata>50, axis=1)) # if any of the numbers in a particular column is >50
# print(np.all(filedata>50, axis=1)) # if all of the numbers in a particular column is >50

# print((filedata > 50) & (filedata < 100))
# print(~(filedata > 50) & (filedata < 100))

# arr1 = np.array([1,2,3,4,5])
# arr2 = np.full(5,5)
# print(arr2)
# mat = np.array([arr1, arr1+arr2, arr1+2*arr2, arr1+3*arr2, arr1+4*arr2])
# print(mat)