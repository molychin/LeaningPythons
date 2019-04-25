





# In[16]:





# In[17]:







# In[18]:





# In[19]:





# In[20]:





# # Indexing by dates and times using DatetimeIndex

# In[21]:


# create a DatetimeIndex from a date range
rng = pd.date_range('5/1/2017', periods=5, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts


# In[22]:


ts.index


# # Indexing periods of time using PeriodIndex

# In[23]:


# explicily create a PeriodIndex
periods = pd.PeriodIndex(['2017-1', '2017-2', '2017-3'], freq='M')
periods


# In[24]:


# use the index in a Series
period_series = pd.Series(np.random.randn(len(periods)), 
                          index=periods)
period_series


# # Creating and using an index with a Series or DataFrame

# In[25]:


# create a DatetimeIndex
date_times = pd.DatetimeIndex(pd.date_range('5/1/2017', 
                                            periods=5, 
                                            freq='H'))
date_times


# In[26]:


# create a DataFrame using the index
df_date_times = pd.DataFrame(np.arange(0, len(date_times)), 
                             index=date_times)
df_date_times


# In[27]:


# set the index of a DataFrame
df_date_times.index = pd.DatetimeIndex(pd.date_range('6/1/2017', 
                                                     periods=5, 
                                                     freq='H'))
df_date_times


# # Selecting values using an index

# In[28]:


# create a series
s = pd.Series(np.arange(0, 5), index=list('abcde'))
s


# In[29]:


# lookup by index label
s['b']


# In[30]:


# explicit lookup by label
s.loc['b']


# In[31]:


# create a DataFrame with two columns
df = pd.DataFrame([ np.arange(10, 12), 
                    np.arange(12, 14)], 
                  columns=list('ab'), 
                  index=list('vw'))
df


# In[32]:


# this returns the column 'a'
df['a']


# In[33]:


# return the row 'w' by label
df.loc['w']


# In[34]:


# slices the Series from index label b to d
s['b':'d']


# In[35]:


# this explicitly slices from label b to d
s.loc['b':'d']


# In[36]:


# and this looks up rows by label
s.loc[['a', 'c', 'e']]


# # Moving data to and from the index 

# In[37]:


# examine asome of the sp500 data
sp500[:5]


# In[38]:


# reset the index which moves the values in the index to a column
index_moved_to_col = sp500.reset_index()
index_moved_to_col[:5]


# In[39]:


# and now set the Sector column to be the index
index_moved_to_col.set_index('Sector')[:5]


# In[40]:


# reindex to have MMM, ABBV, and FOO index labels
reindexed = sp500.reindex(index=['MMM', 'ABBV', 'FOO'])
# note that ABT and ACN are dropped and FOO has NaN values
reindexed


# In[41]:


# reindex columns
sp500.reindex(columns=['Price', 
                       'Book Value', 
                       'NewCol'])[:5]


# # Hierarchical indexing

# In[42]:


# first, push symbol into a column
reindexed = sp500.reset_index()
# and now index sp500 by sector and symbol
multi_fi = reindexed.set_index(['Sector', 'Symbol'])
multi_fi[:5]


# In[43]:


# the index is a MultiIndex
type(multi_fi.index)


# In[44]:


# this has two levels
len(multi_fi.index.levels)


# In[45]:


# each index level is an index
multi_fi.index.levels[0]


# In[46]:


# each index level is an index
multi_fi.index.levels[1]


# In[47]:


# values of index level 0
multi_fi.index.get_level_values(0)


# In[48]:


# get all stocks that are Industrials
# note the result drops level 0 of the index
multi_fi.xs('Industrials')[:5]


# In[49]:


# select rows where level 1 (Symbol) is ALLE
# note that the Sector level is dropped from the result
multi_fi.xs('ALLE', level=1)


# In[50]:


# Industrials, without dropping the level
multi_fi.xs('Industrials', drop_level=False)[:5]


# In[51]:


# drill through the levels
multi_fi.xs('Industrials').xs('UPS')


# In[52]:


# drill through using tuples
multi_fi.xs(('Industrials', 'UPS'))

