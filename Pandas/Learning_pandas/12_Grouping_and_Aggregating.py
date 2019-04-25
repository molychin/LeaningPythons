
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


# # Data for the examples

# In[2]:


# load the sensors data
sensor_data = pd.read_csv("data/sensors.csv")
sensor_data[:5]


# # Grouping by a single column's values

# In[3]:


# group this data by the sensor column / variable
# returns a DataFrameGroupBy object
grouped_by_sensor = sensor_data.groupby('sensor')
grouped_by_sensor


# In[4]:


# get the number of groups that this will create
grouped_by_sensor.ngroups


# In[5]:


# what are the groups that were found?
grouped_by_sensor.groups


# # Accessing the results of a grouping

# In[6]:


# a helper function to print the contents of the groups
def print_groups (group_object):
    # loop over all groups, printing the group name 
    # and group details
    for name, group in group_object:
        print (name)
        print (group[:5])


# In[7]:


# examine the content of the groups we created
print_groups(grouped_by_sensor)


# In[8]:


# get how many items are in each group
grouped_by_sensor.size()


# In[9]:


# get the count of items in each column of each group
grouped_by_sensor.count()


# In[10]:


# get the data in one specific group
grouped_by_sensor.get_group('accel')[:5]


# In[11]:


# get the first three items in each group
grouped_by_sensor.head(3)


# In[12]:


# get the 2nd item in each group
grouped_by_sensor.nth(1)


# In[13]:


# get descriptive statistics for each group
grouped_by_sensor.describe()


# # Grouping using muiltiple columns

# In[14]:


# group by both sensor and axis values
mcg = sensor_data.groupby(['sensor', 'axis'])
print_groups(mcg)


# ## Grouping using index levels

# In[15]:


# make a copy of the data and reindex the copy
mi = sensor_data.copy()
mi = mi.set_index(['sensor', 'axis'])
mi


# In[16]:


# group by the first level of the index 
print_groups(mi.groupby(level=0))


# In[17]:


# group by multiple levels of the index
print_groups(mi.groupby(level=['sensor', 'axis']))


# ## Applying aggregation functions to groups

# In[18]:


# calculate the mean for each sensor/axis
sensor_axis_grouping = mi.groupby(level=['sensor', 'axis'])
sensor_axis_grouping.agg(np.mean)


# In[19]:


# do not create an index matching the original object
sensor_data.groupby(['sensor', 'axis'], as_index=False).agg(np.mean)


# In[20]:


# can simply apply the agg function to the group by object
sensor_axis_grouping.mean()


# In[21]:


# apply multiple aggregation functions at once
sensor_axis_grouping.agg([np.sum, np.std])


# In[22]:


# apply a different function to each column
sensor_axis_grouping.agg({'interval' : len,
                          'reading': np.mean})


# In[23]:


# calculate the mean of the reading column
sensor_axis_grouping['reading'].mean()


# # Transforming groups of data

# In[24]:


# a DataFrame to use for examples
transform_data = pd.DataFrame({ 'Label': ['A', 'C', 'B', 'A', 'C'],
                                'Values': [0, 1, 2, 3, 4],
                                'Values2': [5, 6, 7, 8, 9],
                                'Other': ['foo', 'bar', 'baz', 
                                          'fiz', 'buz']},
                              index = list('VWXYZ'))
transform_data


# In[25]:


# group by label
grouped_by_label = transform_data.groupby('Label')
print_groups(grouped_by_label)


# In[26]:


# add ten to all values in all columns
grouped_by_label.transform(lambda x: x + 10)


# # Filling missing values with the mean of the group

# In[27]:


# data to demonstrate replacement on NaN
df = pd.DataFrame({ 'Label': list("ABABAB"),
                    'Values': [10, 20, 11, np.nan, 12, 22]})
grouped = df.groupby('Label')
print_groups(grouped)


# In[28]:


# calculate the mean of the two groups
grouped.mean()


# In[29]:


# use transform to fill the NaNs with the mean of the group
filled_NaNs = grouped.transform(lambda x: x.fillna(x.mean()))
filled_NaNs


# # Calculating z-scores

# In[30]:


# generate a rolling mean time series
np.random.seed(123456)
data = pd.Series(np.random.normal(0.5, 2, 365*3), 
                 pd.date_range('2013-01-01', periods=365*3))
periods = 100
rolling = data.rolling(
    window=periods,
    min_periods=periods,
    center=False).mean().dropna()
rolling[:5]


# In[31]:


# visualize the series
rolling.plot();


# In[32]:


# calculate mean and std by year
group_key = lambda x: x.year
groups = rolling.groupby(group_key)
groups.agg([np.mean, np.std])


# In[33]:


# normalize to the z-score
z_score = lambda x: (x - x.mean()) / x.std()
normed = rolling.groupby(group_key).transform(z_score)
normed.groupby(group_key).agg([np.mean, np.std])


# In[34]:


# plot original vs normalize
compared = pd.DataFrame({ 'Original': rolling,
                          'Normed': normed })
compared.plot();


# # Filtering groups

# In[35]:


# data for our examples
df = pd.DataFrame({'Label': list('AABCCC'),
                   'Values': [1, 2, 3, 4, np.nan, 8]})
df


# In[36]:


# drop groups with one or fewer non-NaN values
f = lambda x: x.Values.count() > 1
df.groupby('Label').filter(f)


# In[37]:


# drop any groups with NaN values
f = lambda x: x.Values.isnull().sum() == 0
df.groupby('Label').filter(f)


# In[38]:


# select groups with a mean of 2.0 or greater 
grouped = df.groupby('Label')
group_mean = grouped.mean().mean()
f = lambda x: abs(x.Values.mean() - group_mean) > 2.0
df.groupby('Label').filter(f)

