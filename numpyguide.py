import numpy as np;
#numpy arrays are fast as compared to lists 
#this is because the numpy arrays have fixed type,and they have contiguous memory
#application of numpy: MATLAB replacement=>Matplotlib,and pandas
a=np.array([1,2,4])
print(a)
b=np.array([[1,2,4],[2,3,6]])
print (b)
print (a.ndim)
print(b.ndim)#prints us the dimention of the array b
print (a.shape)
print(b.shape)#prints us the shape of the array
print(a.dtype)
print(a.itemsize) #prints the byte size of the array elements
print(b[1,2])#prints the element at the location given
print(b[0,:])# : means all the elements int the 0 th row
print(b[:,1])
a=np.zeros((2,3,4))#creates an array of the give size
a=np.ones((1,3,5,6))
a=np.random.rand(4,2)
a=np.identity(3)
c=b.copy()
c[0,0]=7
print (c)
print(a) 
print(a+2)#addition ,subtraction ,multiplication and division will be done in all the elements of the arrayand a power 2 can also be done by a**2/3/4/...
np.sin(a)#cos ,etc..
a=np.ones((2,3))
b=np.full((3,2),2)
print(np.matmul(a,b))#matrix multiplication
print (np.linalg.det(np.matmul(a,b)))#helps in finding out the determinant value of the matrix
print (np.min(a))
np.max(a)
print (np.sum(b,axis=0))
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a.reshape(8,1))
#Stacking is also possible
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2,v2]))
print(np.hstack([v1,v2]))
filedata=np.genfromtxt('data.txt',delimiter=',')#can be used to get data in numpy instead of pandas
filedata.astype('int32')
filedata>50
filedata[filedata>50]#this makes an array that is greater than 50 nums

