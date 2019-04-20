
# coding: utf-8

# ## NumPy for pandas




Numerical Python (NumPy) is an open source Python library for scientific computing.
NumPy provides a host of features that allow a Python programmer to work with high-performance 
arrays and matrices. NumPy arrays are stored more efficiently than Python lists and 
allow mathematical operations to be vectorized, which results in significantly higher 
performance than with looping constructs in Python.
numpy提供了许多特性，允许Python程序员使用高性能数组和矩阵。numpy数组的存储效率高于python列表，
并且允许对数学操作进行矢量化，这使得性能显著高于python中的循环结构。





In this chapter, we will cover the following topics about NumPy arrays:
• Installing and importing NumPy
• Benefits and characteristics of NumPy arrays
• Creating NumPy arrays and performing basic array operations
• Selecting array elements
• Logical operation on arrays
• Slicing arrays
• Reshaping arrays
• Combining arrays
• Splitting arrays
• Useful numerical methods of NumPy arrays





NumPy arrays have several advantages over Python lists. These benefits are focused
on providing high-performance manipulation of sequences of homogenous data
items. Several of these benefits are as follows:
• Contiguous allocation in memory  内存中的连续分配
• Vectorized operations  矢量化操作
• Boolean selection
• Sliceability  可切片性





Vectorized operation is a technique of applying an operation across all or a subset of 
elements without explicit coding of loops. Vectorized operations are often orders of 
magnitude more efficient in execution as compared to loops implemented in a higher-level 
language. They are also excellent for reducing the amount of code that needs to be written, 
which also helps in minimizing coding errors.
矢量化操作是一种在所有元素或元素子集上应用操作的技术，而不需要对循环进行显式编码。与在高级
语言中实现的循环相比，矢量化操作在执行中通常效率高出几个数量级。它们还可以很好地减少需要编
写的代码量，这也有助于最小化编码错误。


# In[2]:


import numpy as np
# a function that squares all the values
# in a sequence
def squares(values):
    result = []
    for v in values:
        result.append(v * v)
    return result
'''
# create 100,000 numbers using python range
to_square = range(100000)
# time how long it takes to repeatedly square them all
%timeit squares(to_square)   #获取代码执行的效率
#11.6 ms ± 44.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
'''

# now lets do this with a numpy array
array_to_square = np.arange(0, 100000)
# and time using a vectorized operation
get_ipython().magic('timeit array_to_square ** 2')
#68 µs ± 361 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)



# In[9]:


a1=np.array([1,2,3,5,7])
a1
type(a1)
np.size(a1)





NumPy arrays must have all of their elements of the same type. If you specify
different types in the list, NumPy will try to coerce all the items to the same type.


# In[7]:


a3 = np.array([0]*10)
a3
#An array can also be initialized with sequential values using the Python range() function. 
np.array(range(10))
# create a numpy array of 10 0.0's
np.zeros(10)   #float
np.zeros(10, dtype=int)
np.arange(0, 10)
np.arange(0, 10, 2)
np.arange(10, 0, -1)
np.linspace(0, 10, 11)   #array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
#Note that the datatype of the array by default is float, and that the start and end values are inclusive.
#请注意，默认情况下数组的数据类型为float，并且起始值和结束值都包含在内。
a1 = np.arange(0, 10)
a1 * 2
a2 = np.arange(10, 20)
a1 + a2
a1[1],a1[2]





NumPy arrays are n-dimensional, but for purposes of pandas, we will be most
interested in one- and two-dimensional arrays. This is because the pandas Series
and DataFrame objects operate similarly to one-and two-dimensional arrays,
respectively.
To create a two-dimensional NumPy array, you can pass in a list of lists as shown in
the following example:
NumPy array是一维的，实现二维的方式是：


# In[29]:


# create a 2-dimensional array (2x2)
np.array([[1,2], [3,4]])
#A more convenient and efficient means is to use the NumPy array's .reshape()
#method to reorganize a one-dimensional array into two dimensions.
m = np.arange(0, 20).reshape(5, 4)
print(m)
np.size(m)
# can ask the size along a given axis (0 is rows)
np.size(m, 0)
# and 1 is the columns
np.size(m, 1)
m[1,2]
# all items in row 1
m[1,]   #返回array
# all items in column 2
m[:,2]
m[:,1:3]
# in row positions 3 up to but not including 5, all columns
m[3:5,:]
# combined to pull out a sub matrix of the matrix
m[3:5,1:3]
# using a python array, we can select
# non-contiguous rows or columns
m[[1,3,4],:]





Logical operations on arrays
Logical operations can be applied to arrays to test the array values against specific
criteria. The following code tests if the values of the array are less than 2:


# In[14]:


a = np.arange(5)
print(a)
a < 2
# less than 2 or greater than 3?
(a<2) | (a>3)





NumPy provides the np.vectorize() function, which applies an expression or
function to an array in a vectorized manner. The following code demonstrates the
use of np.vectorize() to apply a function named exp() to each item in the array:


# In[16]:


a = np.arange(5)
# create a function that is applied to all array elements
def exp (x):
    return x<3 or x>3

# np.vectorize applies the method to all items in an array
np.vectorize(exp)(a)


# In[18]:


# boolean select items < 3
r = a<3
# applying the result of the expression to the [] operator
# selects just the array elements where there is a matching True
a[r]
# np.sum treats True as 1 and False as 0
# so this is how many items are less than 3
np.sum(a < 3)





Slicing arrays
NumPy arrays support a feature called slicing. Slicing retrieves zero or more items
from an array, and the items also don't need to be sequential, whereas the normal
array element operator [] can only retrieve one value. This is very convenient as it
provides an ability to efficiently select multiple items from an array without the need
to implement Python loops.
numpy数组支持称为切片的功能。切片从数组中检索零个或多个项，这些项也不需要是连续的，
而普通数组元素运算符[]只能检索一个值。这非常方便，因为它提供了从一个数组中有效地选
择多个项的能力，而不需要实现Python循环。
Slicing overloads the normal array [] operator to accept what is referred to as a slice
object. A slice object is created using a syntax of start:end:step. Each component
of the slice is optional and, as we will see, this provides convenient means to select
entire rows or columns by omitting the component of the slice.


# In[25]:


a1 = np.arange(1, 10)
print(a1)
a1[3:8]
#This example has omitted specifying the step value, which uses the default value
#of 1. To demonstrate using other values for step, the following code selects every
#other element in the array
# every other item
a1[::2]
#By omitting the start and end, NumPy chooses 0 through the length of the array as
#those values and then retrieves every other item. Changing this slightly, a negative
#step value of -1 will conveniently reverse the array:
# in reverse order
a1[::-1]
#note that when in reverse, this does not include  the element specified in the second 
#component of the slice that is, there is no 1 printed in this
a1[9:0:-1]
a1[9::-1]
# all items from position 5 onwards
a1[5:]


# ### Reshaping arrays

# In[6]:


import numpy as np
# create a 9 element array (1x9)
a = np.arange(0, 9)
# and reshape to a 3x3 2-d array
m = a.reshape(3, 3)
m
reshaped = m.reshape(9)
reshaped

# .ravel will generate array representing a flattened 2-d array
raveled = m.ravel()   #展平，将二维数据转化为1维
raveled
#Even though .reshape() and .ravel() do not change the shape of the original
#array or matrix, they do actually return a one-dimensional view into the specified
#array or matrix. If you change an element in this view, the value in the original array
#or matrix is changed. 

#The .flatten() method functions similarly to .ravel() but instead returns a new
#array with copied data instead of a view. Changes to the result do not change the
#original matrix
# flattened is like ravel, but a copy of the data,
# not a view into the source
m2 = np.arange(0, 9).reshape(3,3)
flattened = m2.flatten()
# change in the flattened object
flattened[0] = 1000
flattened
# we can reshape by assigning a tuple to the .shape property
# we start with this, which has one dimension
flattened.shape
# and make it 3x3
flattened.shape = (3, 3)
# it is no longer flattened
print(flattened)
# transpose a matrix  转置矩阵
flattened.transpose()
# can also use .T property to transpose
flattened.T
#The .resize() method functions similarly to the .reshape() method, except
#that while reshaping returns a new array with data copied into it, .resize()
#performs an in-place reshaping of the array
# we can also use .resize, which changes shape of
# an object in-place
m3 = np.arange(0, 9).reshape(3,3)
m3.resize(1, 9)
m3


# In[22]:


#Combining arrays
#Arrays can be combined in various ways. This process in NumPy is referred to
#as stacking. Stacking can take various forms, including horizontal, vertical, and
#depth-wise stacking. To demonstrate this, we will use the following two arrays(a and b):
# creating two arrays for examples
a = np.arange(9).reshape(3, 3)
b = (a + 1) * 10
a
b
#Horizontal stacking combines two arrays in a manner where the columns of the
#second array are placed to the right of those in the first array. The function actually
#stacks the two items provided in a two-element tuple. The result is a new array with
#data copied from the two that are specified:
#水平堆叠以将第二个阵列的列放置在第一个阵列的列的右侧的方式组合两个阵列。函数实际上将提供
#的两个项堆叠在一个两元素元组中。结果是一个新数组，其中包含从指定的两个数组中复制的数据
# horizontally stack the two arrays
# b becomes columns of a to the right of a's columns
np.hstack((a, b))   #水平堆叠  =np.concatenate((a, b), axis = 1)
#This functionally is equivalent to using the np.concatenate() function while
#specifying axis = 1:

#Vertical stacking returns a new array with the contents of the second array as
#appended rows of the first array
np.vstack((a,b))   #垂直堆叠  = np.concatenate((a, b), axis = 0)

#Depth stacking takes a list of arrays and arranges them in order along an additional
#axis referred to as the depth
# dstack stacks each independent column of a and b
print(np.dstack((a, b)))    #深度堆叠
#Column stacking performs a horizontal stack of two one-dimensional arrays, making
#each array a column in the resulting array
# set up 1-d array
one_d_a = np.arange(5)
one_d_a
# another 1-d array
one_d_b = (one_d_a + 1) * 10
one_d_b
# stack the two columns
np.column_stack((one_d_a, one_d_b))
#Row stacking returns a new array where each one-dimensional array forms one of
#the rows of the new array
# stack along rows
np.row_stack((one_d_a, one_d_b))


# In[18]:


import numpy as np
#Splitting arrays
#Arrays can also be split into multiple arrays along the horizontal, vertical, and depth
#axes using the np.hsplit(), np.vsplit(), and np.dsplit() functions. We will
#only look at the np.hsplit() function as the others work similarly.
# sample array
a = np.arange(12).reshape(3, 4)
print(a)
#We can split this into four arrays, each representing the values in a specific column
# horiz split the 2-d array into 4 array columns
bb=np.hsplit(a, 4)
bb
np.hsplit(a, 2)
# split at columns 1 and 3
np.hsplit(a, [1, 3])
# along the rows
np.split(a, 2, axis = 1)
np.split(a, [1,2], axis = 0)

a = np.arange(12).reshape(4, 3)
print(a)
# split into four rows of arrays
np.vsplit(a, 4)
# into two rows of arrays
np.vsplit(a, 2)
# rows 1 and 2 of original are row 1
np.vsplit(a, [1, 3])

#Depth splitting splits three-dimensional arrays.
# 3-d array
c = np.arange(27).reshape(3, 3, 3)
print(c)
# split into 3
np.dsplit(c, 3)


# ### Useful numerical methods of NumPy arrays

# In[28]:


#NumPy arrays have many functions that can be applied to the arrays. Many of these
#are statistical functions that you can use for data analysis. 
# demonstrate some of the properties of NumPy arrays
m = np.arange(10, 19).reshape(3, 3)
print (m)
print ("{0} min of the entire matrix".format(m.min()))
print ("{0} max of entire matrix".format(m.max()))
print ("{0} position of the min value".format(m.argmin()))
print ("{0} position of the max value".format(m.argmax()))
print ("{0} mins down each column".format(m.min(axis = 0)))
print ("{0} mins across each row".format(m.min(axis = 1)))
print ("{0} maxs down each column".format(m.max(axis = 0)))
print ("{0} maxs across each row".format(m.max(axis = 1)))

# demonstrate included statistical methods
a = np.arange(10)
print(a)
#The .mean(), .std(), and .var() methods compute the mathematical mean,
#standard deviation, and variance of the values in an array
a.mean(), a.std(), a.var()   #算术平均值，标准差，方差
a = np.arange(1, 6)
a.sum(), a.prod()    #和与乘积
# and cumulative sum and prod
a.cumsum(), a.cumprod()   #累加和累成

a = np.arange(10)
(a < 5).any() # any < 5?   .any()只要有一个为真，即为Ture
(a < 5).all() # all < 5? (a < 5).any() # any < 5?    .all() 全部为真，则为True


# In[31]:


# size is always the total number of elements
np.arange(10).reshape(2, 5).size
# .ndim will give you the total # of dimensions
np.arange(10).reshape(2,5).ndim





第二版P84.   2015第一版 P72

