
# coding: utf-8

# ## Grouping and Aggregating Data

# In[ ]:


in this chapter, we will cover:
• An overview of the split, apply, and combine pattern for data analysis
• Grouping by column values
• Accessing the results of grouping
• Grouping using index levels
• Applying functions to groups to create aggregate results
• Transforming groups of data using filtering to selectively remove groups
of data
• The discretization of continuous data into bins


# ### The split, apply, and combine (SAC) pattern
# Many data analysis problems utilize a pattern of processing data, known as
# split-apply-combine. In this pattern, three steps are taken to analyze data:
# 1. A data set is split into smaller pieces
# 2. Each of these pieces are operated upon independently
# 3. All of the results are combined back together and presented as a single unit
# 
# Splitting in pandas is performed using the .groupby() method of a Series or
# DataFrame object, which given one or more index labels and/or column names, will
# divide the data based on the values present in the specifed index labels and columns.
# 
# Once the data is split into groups, one or more of the following three broad classes of
# operations is applied:
# • Aggregation: This calculates a summary statistic, such as group means or
# counts of the items in each group
# • Transformation: This performs group- or item-specific calculations and
# returns a set of like-indexed results
# • Filtration: This removes entire groups of data based on a group
# level computation

# #### Split

# In[3]:


import numpy as np
import pandas as pd

#Data for the examples
# load the sensors data
sensors = pd.read_csv("data/sensors.csv")
sensors
#Grouping by a single column's values
# group this data by the sensor column / variable
# returns a DataFrameGroupBy object
grouped = sensors.groupby('sensor')
grouped   #<pandas.core.groupby.DataFrameGroupBy object at 0x0000010BADC165F8>
'''
The result of calling .groupby() on DataFrame is not the actual grouped data, but a
DataFrameGroupBy object (SeriesGroupBy when grouping on Series). The actual
process of grouping is a deferred/lazy process in pandas, and at this point, the
grouping has not actually been performed. This object represents an interim description
of the grouping to be performed. This allows pandas to frst validate that the grouping
description provided to it is valid, relative to the data before starting processing.
对数据帧调用.groupby（）的结果不是实际分组的数据，而是一个dataframe groupby对象（对序列分组时为seriesGroupby）。
实际分组过程在熊猫中是一个延迟/懒惰的过程，此时还没有真正执行分组。此对象表示要执行的分组的临时描述。
这允许pandas在开始处理之前，相对于数据，验证提供给它的分组描述是否有效。
'''
# get the number of groups that this will create
grouped.ngroups
'''
The .groups property will return a Python dictionary whose keys represent the
names of each group (if multiple columns are specifed, it is a tuple). The values in
the dictionary are an array of the index labels contained within each respective group:
'''
# what are the groups that were found?
grouped.groups


# In[3]:


#Accessing the results of grouping
'''
The grouped variable can be thought of as a collection of named groups. We will
use these properties, and the following function, to examine many of the results
of groupings:
'''
# a helper function to print the contents of the groups
def print_groups (groupobject):
    # loop over all groups, printing the group name
    # and group details
    for name, group in groupobject:
        print (name)
        print (group)

# examine the content of the groups we created
print_groups(grouped)


# In[13]:


# get how many items are in each group
grouped.size()
# get the count of items in each column of each group
grouped.count()
# get the data in one specific group
grouped.get_group('accel')
# get the first three items in each group
grouped.head(3)
# get the first item in each group
grouped.nth(0)


# In[15]:


#Grouping can also be performed on multiple columns by passing a list of column
#names. The following groups the data by both sensor and axis variables:
# group by both sensor and axis values
mcg = sensors.groupby(['sensor', 'axis'])
print_groups(mcg)
# get descriptive statistics for each
mcg.describe()


# In[18]:


#Grouping using index levels
'''
The examples up to this point, have used DataFrame without any specifc indexing
(just the default sequential numerical index). This type of data would actually be
very well suited for a hierarchical index. This can then be used directly to group the
data based upon index label(s).
'''
# make a copy of the data and reindex the copy
mi = sensors.copy()
mi = mi.set_index(['sensor', 'axis'])
mi
#Grouping can now be performed using the levels of the hierarchical index.
#The following groups by index level 0 (the sensor names):
# group by the first level of the index
mig_l1 = mi.groupby(level=0)
print_groups(mig_l1)    
   


# In[21]:


'''
Grouping by multiple levels can be performed by passing the levels in a list to
.groupby(). Also, if MultiIndex has names specifed for the levels, then these
names can be used instead of integers. The following code groups the two levels
of MultiIndex by their names:
'''    
# group by multiple levels of the index
mig_l12 = mi.groupby(level=['sensor', 'axis'])    
print_groups(mig_l12) 


# ### Apply
# After the grouping is performed, we have the ability to perform either aggregate
# calculations on each group of data resulting in a single value from each group, or to
# apply a transformation to each item in a group and return the combined result for
# each group. We can also flter groups based on results of expressions to exclude the
# groups from being included in the combined results.

# In[22]:


#Applying aggregation functions to groups
'''
pandas allows the application of an aggregation function to each group of data.
Aggregation is performed using the .aggregate() (or in short, .agg()) method
of the GroupBy object. The parameter of .agg() is a reference to a function that is
applied to each group. In the case of DataFrame, the function will be applied to
each column.
'''
# calculate the mean for each sensor/axis
mig_l12.agg(np.mean)
'''
The result of the aggregation will have an identically structured index as the original
data. If you do not want this to happen, you can use the as_index=False option of
the .groupby() method to specify not to duplicate the structure of the index:
'''
# do not create an index matching the original object
sensors.groupby(['sensor', 'axis'],as_index=False).agg(np.mean)


# In[ ]:


Many aggregation functions are built in directly to the GroupBy object to save you
some more typing. Specifcally, these functions are (prefxed by gb.):
    
gb.agg gb.boxplot gb.cummin gb.describe gb.filter
gb.get_group gb.height gb.last gb.median gb.ngroups
gb.plot gb.rank gb.std gb.transform
gb.aggregate gb.count gb.cumprod gb.dtype gb.first
gb.groups gb.hist gb.max gb.min gb.nth
gb.prod gb.resample gb.sum gb.var
gb.apply gb.cummax gb.cumsum gb.fillna gb.gender
gb.head gb.indices gb.mean gb.name gb.ohlc
gb.quantile gb.size gb.tail gb.weight


# In[26]:


#An equivalent to the previous .agg(np.mean) method is the following:
# can simply apply the agg function to the group by object
mig_l12.mean()
# apply multiple aggregation functions at once
mig_l12.agg([np.sum, np.std])
# apply a different function to each column
mig_l12.agg({'interval' : len,'reading': np.mean})
#Aggregation can also be performed on specifc columns using the [] operator on the
#GroupBy object. The following sums only the reading column:
# calculate the mean of the reading column
mig_l12['reading'].mean()




# #### The transformation of group data
# Transformation is one of the more mysterious capabilities of pandas. I have
# personally found the operation of the .transform() method to be diffcult for many
# to grasp (including myself) when starting to frst use it. This is easily verifable with
# many Stack Overﬂow postings about not being able to get it to work the way you
# think it should.
# Documentation is fuzzy on these diffculties, so I feel it worthwhile to give some
# good examples and explanations for its operation. We will start with a general
# overview of transformation and then examine a few practical examples to make
# the operation more understandable.
# 转变是熊猫更神秘的能力之一。我亲自发现了transform（）方法在很多人开始使用它时（包括我自己）很难掌握。这很容易被证实
# 很多关于不能让它像你认为的那样工作的过火的帖子。
# 对于这些困难，文档是模糊的，所以我觉得有必要为它的操作提供一些好的例子和解释。我们将从转换的一般概述开始，然后检查
# 一些实际示例，以使操作更易于理解。

# In[8]:


import numpy as np
import pandas as pd

# a DataFrame to use for examples
df = pd.DataFrame({ 'Label': ['A', 'C', 'B', 'A', 'C'],
    'Values': [0, 1, 2, 3, 4],
    'Values2': [5, 6, 7, 8, 9],
    'Noise': ['foo', 'bar', 'baz',
    'foobar', 'barbaz']})
df

# group by label
grouped = df.groupby('Label')
print_groups(grouped)
# add ten to all values in all columns
grouped.transform(lambda x: x + 10)


# In[9]:


# a function to print the input before we are adding 10 to it
def xplus10(x):
    print (x)
    return x + 10

# transform using xplus10
grouped.transform(xplus10)


# In[10]:


# sum returns existing as it is applied to each individual item
grouped.transform(lambda x: x.sum())




# In[12]:


# data to demonstrate replacement on NaN
df = pd.DataFrame({ 'Label': list("ABABAB"),
    'Values': [10, 20, 11, np.nan, 12, 22]},
    index=['i1', 'i2', 'i3', 'i4', 'i5', 'i6'])
df

# show the groups in the data based upon Label
grouped = df.groupby('Label')
print_groups(grouped)


# In[13]:


# calculate the mean of the two groups
grouped.mean()


# In[14]:


# use transform to fill the NaNs with the mean of the group
filled_NaNs = grouped.transform(lambda x: x.fillna(x.mean()))    #以分类的平均值填充NaN
filled_NaNs


# In[15]:


# overwrite old values with the new ones
df.Values = filled_NaNs
df


# In[ ]:


The .transform() method does not change the original data
or the data in the group that is being applied to. Index labels are
preserved, so you can go back and relate the results to the original
data or any of the groups. If you want to patch this data, you will
need to align/merge the results with the original data or grouped
data. These changes, then, do not affect already calculated groups
or the results for the apply step.


# In[21]:


import matplotlib.pyplot as plt

# generate a rolling mean time series
np.random.seed(123456)
data = pd.Series(np.random.normal(0.5, 2, 365*3),
pd.date_range('2011-01-01', periods=365*3))
rolling = pd.rolling_mean(data, 100, 100).dropna()
rolling
# visualize the series
rolling.plot()
plt.show()


# In[22]:


# calculate mean and std by year
groupkey = lambda x: x.year
groups = rolling.groupby(groupkey)
groups.agg([np.mean, np.std])


# In[23]:


# normalize to the z-score
zscore = lambda x: (x - x.mean()) / x.std()
normed = rolling.groupby(groupkey).transform(zscore)
normed.groupby(groupkey).agg([np.mean, np.std])


# In[26]:


# plot original vs normalize
compared = pd.DataFrame({ 'Original': rolling,'Normed': normed })
compared.plot()
plt.show()


# In[27]:


# check the distribution % within one std
# should be roughly 64.2%
normed_in1std = normed[np.abs(normed) <= 1.0].count()
float(normed_in1std) / len(normed)


# ### Filtering groups
# The pandas GroupBy object provides a .filter() method, which can be used to
# make group level decisions on whether or not the entire group is included in the
# result after the combination. The function passed to .filter() should return
# True if the group is to be included in the result and False to exclude it

# In[1]:


import numpy as np
import pandas as pd

# data for our examples
df = pd.DataFrame({'Label': list('AABCCC'),'Values': [1, 2, 3, 4, np.nan, 8]})
df
# drop groups with one or fewer non-NaN values
f1 = lambda x: x.Values.count() > 1
f1
df.groupby('Label').filter(f1)


# In[6]:


# drop any groups with NaN values
f = lambda x: x.Values.isnull().sum() == 0
df.groupby('Label').filter(f)


# In[2]:


# select groups with a mean of 2.0 or greater
grouped = df.groupby('Label')
mean = grouped.mean().mean()
f = lambda x: abs(x.Values.mean() - mean) > 2.0
df.groupby('Label').filter(f)


# In[3]:


# replace values in a group where the # of items is <= 1
f = lambda x: x.Values.count() > 1
df.groupby('Label').filter(f, dropna=False)


# ### Discretization and Binning
# Although not directly using grouping constructs, in a chapter on grouping, it is
# worth explaining the process of discretization of continuous data. Discretization is
# a means of slicing up continuous data into a set of "bins", where each bin represents
# a range of the continuous sample and the items are then placed into the appropriate
# bin—hence the term "binning". Discretization in pandas is performed using the
# pd.cut() and pd.qcut() functions.
# 尽管不直接使用分组构造，但在分组一章中，有必要解释连续数据的离散化过程。离散化是将
# 连续数据切片成一组“箱”的一种方法，其中每个箱代表连续样本的一个范围，然后将项目放
# 入适当的箱中，因此称为“箱”。大熊猫的离散化使用pd.cut（）和pd.qcut（）函数。

# In[7]:


# generate 10000 normal random #'s
np.random.seed(123456)
dist = np.random.normal(size = 10000)
# show the mean and std
"{0} {1}".format(dist.mean(), dist.std())
dist



# In[8]:


# split the data into 5 bins
bins = pd.cut(dist, 5)
bins


# In[9]:


'''
The resulting bins object is a type of pandas variable known as Categorical. A
categorical variable that is a result of pd.cut() consists of a set of labels and an
index that describes how the data has been split.
The .categories property will return the index and describe the intervals that
pandas decided upon:
'''
# show the categories in the bins
bins.categories


# In[10]:


# demonstrate the math to calculate the bins
min = dist.min()
max = dist.max()
delta = max - min
iwidth = delta/5
extra = delta*0.001
intervals = np.arange(min, max + extra, iwidth)
intervals[0] -= delta*0.001
intervals


# In[11]:


# codes tells us which bin each item is in
bins.codes


# In[12]:


# move the closed side of the interval to the left
pd.cut(dist, 5, right=False).categories


# In[13]:


# generate 50 ages between 6 and 45
np.random.seed(123456)
ages = np.random.randint(6, 45, 50)
ages


# In[14]:


# cut into ranges and then get descriptive stats
ranges = [6, 12, 18, 35, 50]
agebins = pd.cut(ages, ranges)
agebins.describe()


# In[15]:


# add names for the bins
ranges = [6, 12, 18, 35, 50]
labels = ['Youth', 'Young Adult', 'Adult', 'Middle Aged']
agebins = pd.cut(ages, ranges, labels=labels)
agebins.describe()


# In[16]:


# cut into quantiles
# 5 bins with an equal quantity of items
qbin = pd.qcut(dist, 5)
# this will tell us the range of values in each quantile
qbin.describe()


# In[18]:


# make the quantiles at the +/- 3, 2 and 1 std deviations
quantiles = [0,0.001,0.021,0.5-0.341,0.5,0.5+0.341,1.0-0.021,1.0-0.001,1.0]
qbin = pd.qcut(dist, quantiles)
# this data should be a perfect normal distribution
qbin.describe()



# In[ ]:


第二版P84.   2015第一版 P341

