
# coding: utf-8

# # Configuring pandas

# In[1]:


# import numpy and pandas
import numpy as np
import pandas as pd

# used for dates
import datetime
from datetime import datetime, date

# Set formattign options
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 60)

# bring in matplotlib for graphics
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

# read in the data and print the first five rows
# use the Symbol column as the index, and 
# only read in columns in positions 0, 2, 3, 7
sp500 = pd.read_csv("data/sp500.csv", 
                    index_col='Symbol', 
                    usecols=[0, 2, 3, 7])

# one month of stock history data
omh = pd.read_csv("data/omh.csv")


# # Performing arithmetic on a DataFrame or Series

# In[2]:


# set the seed to allow replicatable results
np.random.seed(123456)
# create the DataFrame
df = pd.DataFrame(np.random.randn(5, 4), 
                  columns=['A', 'B', 'C', 'D'])
df


# In[3]:


# multiply everything by 2
df * 2


# In[4]:


# get first row 
s = df.iloc[0] 
# subtract first row from every row of the DataFrame
diff = df - s 
diff


# In[5]:


# subtract DataFrame from Series
diff2 = s - df
diff2


# In[6]:


# B, C
s2 = s[1:3]
# add E
s2['E'] = 0
# see how alignment is applied in math
df + s2


# In[7]:


# get rows 1 through three, and only B, C columns
subframe = df[1:4][['B', 'C']]
# we have extracted a little square in the middle of df
subframe


# In[8]:


# demonstrate the alignment of the subtraction
df - subframe


# In[9]:


# get the A column
a_col = df['A']
df.sub(a_col, axis=0)


# # Counts of values

# In[10]:


s = pd.Series(['a', 'a', 'b', 'c', np.NaN])
# number of occurrences of each unique value
s.count()


# # Unique and number of unique values

# In[11]:


# return a list of unique items
s.unique()


# In[12]:


s.nunique()


# In[13]:


s.nunique(dropna=False)


# In[14]:


# get summary stats on non-numeric data
s.value_counts(dropna=False)


# # Minimum and maximums

# In[15]:


# location of min price for both stocks
omh[['MSFT', 'AAPL']].min()


# In[16]:


# and location of the max
omh[['MSFT', 'AAPL']].max()


# In[17]:


# location of min price for both stocks
omh[['MSFT', 'AAPL']].idxmin()


# In[18]:


# and location of the max
omh[['MSFT', 'AAPL']].idxmax()


# # Smallest and Largest Values

# In[19]:


# get the 4 smallest values
omh.nsmallest(4, ['MSFT'])['MSFT']


# In[20]:


# get the 4 largest values
omh.nlargest(4, ['MSFT'])['MSFT']


# In[21]:


# nsmallest on a Series
omh.MSFT.nsmallest(4)


# # Accumulations

# In[22]:


# calculate a cumulative product
pd.Series([1, 2, 3, 4]).cumprod()


# In[23]:


# calculate a cumulative sum
pd.Series([1, 2, 3, 4]).cumsum()


# # Summary descriptive statistics

# In[24]:


# get summary statistics for the stock data
omh.describe()


# In[25]:


# just the stats for MSFT
omh.MSFT.describe()


# In[26]:


# only the mean for MSFT
omh.MSFT.describe()['mean']


# In[27]:


# get summary stats on non-numeric data
s = pd.Series(['a', 'a', 'b', 'c', np.NaN])
s.describe()


# # Mean

# In[28]:


# the mean of all the columns in omh
omh.mean()


# In[29]:


# calc the mean of the values in each row
omh.mean(axis=1)[:5]


# # Median

# In[30]:


# calc the median of the values in each column
omh.median()


# # Mode

# In[31]:


# find the mode of this Series
s = pd.Series([1, 2, 3, 3, 5])
s.mode()


# In[32]:


# there can be more than one mode
s = pd.Series([1, 2, 3, 3, 5, 1])
s.mode()


# # Variance

# In[33]:


# calc the variance of the values in each column
omh.var()


# # Standard Deviation

# In[34]:


# standard deviation
omh.std()


# # Covariance

# In[35]:


# covariance of MSFT vs AAPL
omh.MSFT.cov(omh.AAPL)


# # Correlation

# In[36]:


# correlation of MSFT relative to AAPL
omh.MSFT.corr(omh.AAPL)


# # Discretization and quantiling

# In[37]:


# generate 10000 normal random #'s
np.random.seed(123456)
dist = np.random.normal(size = 10000)
dist


# In[38]:


# show the mean and std
(dist.mean(), dist.std())


# In[39]:


# cut into 5 equally sized bins
bins = pd.cut(dist, 5)
bins


# In[40]:


# just the categories 
bins.categories


# In[41]:


# codes tells us which bin each item is in
bins.codes


# In[42]:


# move the closed side of the interval to the left
pd.cut(dist, 5, right=False).categories


# In[43]:


# generate 50 ages between 6 and 45
np.random.seed(123456)
ages = np.random.randint(6, 45, 50)
ages


# In[44]:


# cut into ranges and then get descriptive stats
ranges = [6, 12, 18, 35, 50]
agebins = pd.cut(ages, ranges)
agebins.describe()


# In[45]:


# add names for the bins
ranges = [6, 12, 18, 35, 50]
labels = ['Youth', 'Young Adult', 'Adult', 'Middle Aged']
agebins = pd.cut(ages, ranges, labels=labels)
agebins.describe()


# In[46]:


# cut into quantiles
# 5 bins with an equal quantity of items
qbin = pd.qcut(dist, 5)
# this will tell us the range of values in each quantile
qbin.describe()


# In[47]:


# make the quantiles at the +/- 3, 2 and 1 std deviations
quantiles = [0,
             0.001, 
             0.021,
             0.5-0.341,
             0.5,
             0.5+0.341,
             1.0-0.021,
             1.0-0.001,
             1.0]
qbin = pd.qcut(dist, quantiles)
# this data should be a perfect normal distribution
qbin.describe()


# # Ranking

# In[48]:


# random data
np.random.seed(12345)
s = pd.Series(np.random.np.random.randn(5), index=list('abcde'))
s


# In[49]:


# rank the values
s.rank()


# # Percent change

# In[50]:


# calculate % change on MSFT
omh[['MSFT']].pct_change()[:5]


# # Moving window operations

# In[51]:


# create a random walk
np.random.seed(123456)
s = pd.Series(np.random.randn(1000)).cumsum()
s[:5]


# In[52]:


s[0:100].plot();


# In[53]:


# calculate rolling window of three days
r = s.rolling(window=3)
r


# In[54]:


# the rolling mean at three days
means = r.mean()
means[:7]


# In[55]:


# check the mean of the first 3 numbers
s[0:3].mean()


# In[56]:


# mean of 1 through 3
s[1:4].mean()


# In[57]:


# plot the 3 day rolling mean
means[0:100].plot();


# # Random sampling

# In[58]:


# create a random sample of four columns of 50 items
np.random.seed(123456)
df = pd.DataFrame(np.random.randn(50, 4))
df[:5]


# In[59]:


# sample three random rows
df.sample(n=3)


# In[60]:


# sample 10% of the rows
df.sample(frac=0.1)


# In[61]:


# 10% with replacement
df.sample(frac=0.1, replace=True)

