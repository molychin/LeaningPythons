
# create example to demonstrate fills
s3 = pd.Series(['red', 'green', 'blue'], index=[0, 3, 5])
s3


# In[82]:


# forward fill example
s3.reindex(np.arange(0,7), method='ffill')


# In[83]:


# backwards fill example
s3.reindex(np.arange(0,7), method='bfill')


# # Modifying a Series in-place

# In[84]:


# generate a Series to play with
np.random.seed(123456)
s = pd.Series(np.random.randn(3), index=['a', 'b', 'c'])
s


# In[85]:


# change a value in the Series
# this is done in-place
# a new Series is not returned that has a modified value
s['d'] = 100
s


# In[86]:


# modify the value at 'd' in-place
s['d'] = -100
s


# In[87]:


# remove a row / item
del(s['a'])
s


# In[88]:


copy = s.copy() # preserve s
slice = copy[:2] # slice with first two rows
slice


# In[89]:


# change item with label 10 to 1000
slice['b'] = 0
# and see it in the source
copy

