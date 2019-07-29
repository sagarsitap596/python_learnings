import sys
import numpy as np

print("python version : {}".format(sys.version))
print("numpy version : {}".format(np.__version__))

# defining scalar
x=6
print(x)

# defining vector
vector1 = np.array((1,2,3,4,5))
print(vector1)
print("Vector dimension : {}".format(vector1.shape))
print("Vector size : {}".format(vector1.size))

# defining metrix
mymetrix = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(mymetrix)
print("metrix dimensions : {}".format(mymetrix.shape))
print("metrix size : {}".format(mymetrix.size))

# define metrix of given dimension
x= np.ones((3,3))
print(x)

# defining tensors
t1=np.ones((3,3,3))
print(t1)
print("Tensor dimensions : {} ".format(t1.shape))
print("Tensor size : {} ".format(t1.size))

# metrix with data types defined
m1=np.ones((4,4), dtype=int)
print(m1)

m1=np.matrix([[1,2],[3,4]])
m2=np.ones((2,2),dtype=np.int)

# Metrix addition
m3=m1+m2
print(m1)
print(m2)
print(m3)

# Metrix substraction
m3=m1-m2
print(m3)

# Metrix multiplication
m3=m1.dot(m2)
print(m3)



m11=np.ones([2,3],dtype=int)
m22=np.ones([3,2],dtype=int)
# m33=m11*m22 -- * doesn't work
m33=m11.dot(m22)
print(m11)
print(m22)
print(m33)


m11=np.matrix([[1,2,3],[4,5,6]])
m22=np.matrix(range(6)).reshape(3,2)
m33=m11*m22
print(m11)
print(m22)
print(m33)


# Transpose of Metrix
m11=np.matrix(range(10)).reshape(2,5)
m22=m11.T
print(m11)
print(m22)


# tensors

t1=np.ones([3,3,3,3,3,3,3,3,3,3,3,3])
print(t1.shape)
print(t1.size)
print(len(t1.shape))
print(len(t1))






