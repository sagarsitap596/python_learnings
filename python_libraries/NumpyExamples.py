import numpy as np

# Code starts here

# initialize NumPy array
array = np.arange(1, 11)

# check dimensions
dim = array.ndim

# reshaped array
reshaped = array.reshape(5, 2)

# check shape
new_dim = reshaped.ndim

print(array)
print(reshaped)

print("=" * 80)

print(" Dimension : "+str(new_dim))

print("Shape : number of items in each row Eg.(5,3) 5 columns and 3 rows {}".format(reshaped.shape))

ssp = reshaped.shape
print("Number of rows : " + str(ssp[0]))  # number of rows
print("Number of columns : " + str(ssp[1]))  # number of columns

print("Size : total number of elements in array : {}".format(reshaped.size))

print("Datatype of values in ndarray : " + str(array.dtype))

print("Itemsize : It represents the number of bytes in each element of the array. : " + str(array.itemsize))

print("=" * 80)

emptyArray = np.empty((2, 3), dtype="int32")
print("Empty array")
print(emptyArray)
print("=" * 80)

zerosArray = np.zeros((2, 3))
print("Zeros array")
print(zerosArray)
print("=" * 80)

onesArray = np.ones((2, 3))
print("Ones array")
print(onesArray)
print("=" * 80)

constantValueArray = np.full((2, 3), 7)
print(" 7 constantValueArray array")
print(constantValueArray)
print("=" * 80)

onesDiagonalArray = np.eye(4, dtype='float16')
print("  onesDiagonalArray array")
print(onesDiagonalArray)
print("=" * 80)

print(np.arange(5))

print("=" * 80)

a = np.arange(9).reshape(3, 3)
print(a)
print(a[1, 1])

print("=" * 80)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Pull out second element of third row
print(a[2][1])
print('==========')
# Pull out first two rows and first 3 columns
print(a[:2, :3])
print('==========')
# Pull all elements of the third row
print(a[2, :])

print("=" * 80)

# Code starts here
import numpy as np

# initialize array
array = np.array([3, 4.5, 3 + 5j, 0])

# boolean filter
real = np.isreal(array)
real_array = array[real]

# boolean filter
imag = np.iscomplex(array)
imag_array = array[imag]

print(real_array[1])
print(imag_array[0])
# Code ends here



np.su