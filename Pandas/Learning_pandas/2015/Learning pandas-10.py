
# coding: utf-8

# ## Time-series Data
# A time series is a measurement of one or more variables over a period of time and
# at a specifc interval. Once a time series is captured, analysis is often performed to
# identify patterns in the data, in essence, determining what is happening as time goes
# by. Being able to process time-series data is essential in the modern world, be it in
# order to analyze fnancial information or to monitor exercise on a wearable device
# and match your exercises to goals and diet.
# 时间序列是一段时间内以特定间隔对一个或多个变量的测量。一旦捕获了一个时间序列，
# 通常会执行分析来识别数据中的模式，本质上，是确定随着时间的推移发生了什么。
# 通过。能够处理时间序列数据在现代世界是至关重要的，无论是为了分析财务信息，还是在可穿戴设备上监测运动，并将运动与目标和饮食相匹配。
# 
# pandas provides extensive support for working with time-series data. When working
# with time-series data, you are frequently required to perform a number of tasks, such
# as the following:
# • Converting string-based dates and time into objects
# • Standardizing date and time values to specific time zones
# • Generating sequences of fixed-frequency dates and time intervals
# • Efficiently reading/writing the value at a specific time in a series
# • Converting an existing time series to another with a new frequency
# of sampling
# • Computing relative dates, not only taking into account time zones, but also
# dealing with specific calendars based upon business days
# • Identifying missing samples in a time series and determining appropriate
# substitute values
# • Shifting dates and time forward or backward by a given amount
# • Calculating aggregate summaries of values as time changes

# In[ ]:


Specifcally, in this chapter, we will cover:
• Creating time series with specific frequencies
• Date offsets
• Representation of differences in time with timedelta
• Durations of time with Period objects
• Calendars
• Time zones
• Shifting and lagging
• Up and down sampling
• Time series moving-window operations


# In[4]:


# import pandas, numpy and datetime
import numpy as np
import pandas as pd
# needed for representing dates and times
#import datetime
from datetime import datetime
import matplotlib.pyplot as plt


# In[ ]:


The datetime, day, and time objects

With respect to pandas, the datetime objects do not have the accuracy needed
for much of the mathematics involved in extensive calculations on time-series
data. However, they are commonly used to initialize pandas objects with pandas
converting them into pandas timestamp objects behind the scenes. Therefore, they
are worth a brief mention here, as they will be used frequently during initialization.


# In[7]:


# datetime object for Dec 15 2014
datetime(2014, 12, 15)
# specific date and also with a time of 5:30 pm
datetime(2014, 12, 15, 17, 30)
# get the local "now" (date and time)
# can take a time zone, but that's not demonstrated here
datetime.now()
# a date without time can be represented
# by creating a date using a datetime object


# In[10]:


datetime.date(datetime(2019, 2, 4, 11, 46, 23, 507374))
# get just the current date
datetime.now().date()
# get the current local time
datetime.now().time()



# #### Timestamp objects
# Specifc dates and times in pandas are represented using the pandas.tslib.
# Timestamp class. Timestamp is based on the datetime64 dtype and has higher
# precision than the Python datetime object. Timestamp objects are generally
# interchangeable with datetime objects, so you can typically use them wherever
# you may use datetime objects.
# 

# In[14]:


# a timestamp representing a specific date
pd.Timestamp('2014-12-15')
# a timestamp with both date and time
pd.Timestamp('2014-12-15 17:30')
# timestamp with just a time
# which adds in the current local date
pd.Timestamp('17:30')
# get the current date and time (now)
pd.Timestamp("now")



# #### Timedelta
# A difference between two pandas Timestamp objects is represented by a timedelta
# object, which is a representation of an exact difference in time. These are common as
# results of determining the duration between two dates or to calculate the date at a
# specifc interval of time from another date and/or time.
# 两个pandas时间戳对象之间的差异由一个TimeDelta对象表示，它表示精确的时间差异。这些通常是
# 确定两个日期之间的持续时间或从另一个日期和/或时间开始以特定时间间隔计算日期的结果。

# In[15]:


# what is one day from 2014-11-30?
today = datetime(2014, 11, 30)
tomorrow = today + pd.Timedelta(days=1)
tomorrow


# In[16]:


# how many days between these two dates?
date1 = datetime(2014, 12, 2)
date2 = datetime(2014, 11, 28)
date1 - date2


# #### Introducing time-series data
# Due to its roots in fnance, pandas excels in manipulating time-series data. Its
# abilities have been continuously refned over all of its versions to progressively
# increase its capabilities for time-series manipulation. These capabilities are the
# core of pandas and do not require additional libraries, unlike R, which requires
# the inclusion of Zoo to provide this functionality.
# The core of the time-series functionality in pandas revolves around the use of
# specialized indexes that represent measurements of data at one or more timestamps.
# These indexes in pandas are referred to as DatetimeIndex objects. These are incredibly
# powerful objects, and their being core to pandas provides the ability to automatically
# align data based on dates and time, making working with sequences of data collected
# and time-stamped as easy as with any other type of indexes.
# We will now examine how to create time-series data and DatetimeIndex objects
# both using explicit timestamp objects and using specifc durations of time (referred
# to in pandas as frequencies).

# In[17]:


# create a very simple time-series with two index labels
# and random values
dates = [datetime(2014, 8, 1), datetime(2014, 8, 2)]
ts = pd.Series(np.random.randn(2), dates)
ts


# In[19]:


# what is the type of the index?
type(ts.index)
# and we can see it is a collection of timestamps
type(ts.index[0])


# In[20]:


# create from just a list of dates as strings!
np.random.seed(123456)
dates = ['2014-08-01', '2014-08-02']
ts = pd.Series(np.random.randn(2), dates)
ts


# In[22]:


# convert a sequence of objects to a DatetimeIndex
dti = pd.to_datetime(['Aug 1, 2014','2014-08-02','2014.8.3',None])
for ll in dti: 
    print (ll)


# In[23]:


# this is a list of objects, not timestamps...
pd.to_datetime(['Aug 1, 2014', 'foo'])   #出错


# In[24]:


# force the conversion, NaT for items that don't work
pd.to_datetime(['Aug 1, 2014', 'foo'], coerce=True)    #TypeError: to_datetime() got an unexpected keyword argument 'coerce'


# In[25]:


# create a range of dates starting at a specific date
# and for a specific number of days, creating a Series
np.random.seed(123456)
periods = pd.date_range('8/1/2014', periods=10)
date_series = pd.Series(np.random.randn(10), index=periods)
date_series


# In[26]:


# slice by location
subset = date_series[3:7]
subset


# In[27]:


# a Series to demonstrate alignment
s2 = pd.Series([10, 100, 1000, 10000], subset.index)
s2


# In[28]:


# demonstrate alignment by date on a subset of items
date_series + s2


# In[31]:


# lookup item by a string representing a date
date_series['2014-08-05']


# In[32]:


# slice between two dates specified by string representing dates
date_series['2014-08-05':'2014-08-07']


# In[33]:


# a two year range of daily data in a Series
# only select those in 2013
s3 = pd.Series(0, pd.date_range('2013-01-01', '2014-12-31'))
s3['2013']


# In[34]:


# 31 items for May 2014
s3['2014-05']


# In[35]:


# items between two months
s3['2014-08':'2014-09']


# ### Creating time-series data with specifc frequencies
# Time-series data in pandas can be created on intervals other than daily frequency.
# Different frequencies can be generated with pd.date_range() by utilizing the freq
# parameter. This parameter defaults to a value of 'D', which represents daily frequency.

# In[36]:


# generate a Series at one minute intervals
np.random.seed(123456)
bymin = pd.Series(np.random.randn(24*60*90),pd.date_range('2014-08-01','2014-10-29 23:59',freq='T'))
bymin


# In[ ]:


This time series allows us to slice at a fner resolution, down to the minute and
smaller intervals if using fner frequencies. To demonstrate minute-level slicing,
the following slices the values at 9 consecutive minutes
这个时间序列允许我们以更精细的分辨率进行切片，如果使用更精细的频率，可以将分辨率降
低到分钟和更小的间隔。为了演示分钟级别的切片，下面将连续9分钟对值进行切片


# In[37]:


# slice down to the minute
bymin['2014-08-01 00:02':'2014-08-01 00:10']


# In[38]:


# generate a series based upon business days
days = pd.date_range('2014-08-29', '2014-09-05', freq='B')
for d in days : print (d)


# In[39]:


# periods will use the frequency as the increment
pd.date_range('2014-08-01 12:10:01', freq='S', periods=10)


# In[40]:


# get all business days between and inclusive of these two dates
dti = pd.date_range('2014-08-29', '2014-09-05', freq='B')
dti.values


# In[41]:


# check the frequency is BusinessDay
dti.freq


# In[42]:


# calculate a one day offset from 2014-8-29
d = datetime(2014, 8, 29)
do = pd.DateOffset(days = 1)
d + do


# In[44]:


# import the data offset types
from pandas.tseries.offsets import *
# calculate one business day from 2014-8-31
d + BusinessDay()


# In[45]:


# determine 2 business days from 2014-8-29
d + 2 * BusinessDay()


# In[46]:


# what is the next business month end
# from a specific date?
d + BMonthEnd()


# In[48]:


# calculate the next month end by
# rolling forward from a specific date
BMonthEnd().rollforward(datetime(2014, 8, 15))


# In[49]:


# calculate the date of the Tuesday previous
# to a specified date
d - Week(weekday = 1)


# In[50]:


# calculate all Wednesdays between 2014-06-01
# and 2014-08-31
wednesdays = pd.date_range('2014-06-01','2014-08-31', freq="W-WED")
wednesdays.values


# In[51]:


# what are all of the business quarterly end
# dates in 2014?
qends = pd.date_range('2014-01-01', '2014-12-31',freq='BQS-JUN')
qends.values


# In[53]:


#The Period object
# create a period representing a month of time
# starting in August 2014
aug2014 = pd.Period('2014-08', freq='M')
aug2014
# examine the start and end times of this period
aug2014.start_time, aug2014.end_time




# In[55]:


# calculate the period that is one frequency
# unit of the aug2014 period further along in time
# This happens to be September 2014
sep2014 = aug2014 + 1
sep2014
sep2014.start_time, sep2014.end_time


# In[56]:


#PeriodIndex
# create a period index representing
# all monthly boundaries in 2013
mp2013 = pd.period_range('1/1/2013', '12/31/2013', freq='M')
mp2013






# In[57]:


# loop through all period objects in the index
# printing start and end time for each
for p in mp2013:
    print ("{0} {1}".format(p.start_time, p.end_time))


# In[58]:


# create a Series with a PeriodIndex
np.random.seed(123456)
ps = pd.Series(np.random.randn(12), mp2013)
ps


# In[59]:


# create a Series with a PeriodIndex and which
# represents all calendar month periods in 2013 and 2014
np.random.seed(123456)
ps = pd.Series(np.random.randn(24),pd.period_range('1/1/2013','12/31/2014', freq='M'))
ps


# In[60]:


# get value for period represented by 2014-06
ps['2014-06']


# In[61]:


# get values for all periods in 2014
ps['2014']


# In[62]:


# demonstrate using the US federal holiday calendar
# first need to import it
from pandas.tseries.holiday import *
# create it and show what it considers holidays
cal = USFederalHolidayCalendar()
for d in cal.holidays(start='2014-01-01', end='2014-12-31'):
    print (d)


# In[64]:


# create CustomBusinessDay object based on the federal calendar
cbd = CustomBusinessDay(holidays=cal.holidays())
# now calc next business day from 2014-8-29
datetime(2014, 8, 29) + cbd


# In[ ]:


第二版P84.   2015第一版 P373

