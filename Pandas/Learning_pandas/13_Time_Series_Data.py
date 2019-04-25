
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


# # The datetime, day, and time objects

# In[2]:


# datetime object for Dec 15 2014
datetime(2014, 12, 15)


# In[3]:


# specific date and also with a time of 5:30 pm
datetime(2014, 12, 15, 17, 30)


# In[4]:


# get the local "now" (date and time)
# can take a timezone, but that's not demonstrated here
datetime.now()


# In[5]:


# a date without time can be represented
# by creating a date using a datetime object
datetime.date(datetime(2014, 12, 15))


# In[6]:


# get just the current date
datetime.now().date()


# In[7]:


# get just a time from a datetime
datetime.time(datetime(2014, 12, 15, 17, 30))


# In[8]:


# get the current local time
datetime.now().time()


# # Timestamp objects

# In[9]:


# a timestamp representing a specific date
pd.Timestamp('2014-12-15')


# In[10]:


# a timestamp with both date and time
pd.Timestamp('2014-12-15 17:30')


# In[11]:


# timestamp with just a time
# which adds in the current local date
pd.Timestamp('17:30')


# In[12]:


# get the current date and time (now)
pd.Timestamp("now")


# # Timedelta

# In[13]:


# what is one day from 2014-11-30?
today = datetime(2014, 11, 30)
tomorrow = today + pd.Timedelta(days=1)
tomorrow


# In[14]:


# how many days between these two dates?
date1 = datetime(2014, 12, 2)
date2 = datetime(2014, 11, 28)
date1 - date2


# # The DatetimeIndex

# In[15]:


# create a very simple time-series with two index labels
# and random values
dates = [datetime(2014, 8, 1), datetime(2014, 8, 2)]
ts = pd.Series(np.random.randn(2), dates)
ts


# In[16]:


# what is the type of the index?
type(ts.index)


# In[17]:


# and we can see it is a collection of timestamps
type(ts.index[0])


# In[18]:


# create from just a list of dates as strings!
np.random.seed(123456)
dates = ['2014-08-01', '2014-08-02']
ts = pd.Series(np.random.randn(2), dates)
ts


# In[19]:


# convert a sequence of objects to a DatetimeIndex
dti = pd.to_datetime(['Aug 1, 2014', 
                      '2014-08-02', 
                      '2014.8.3', 
                      None])
for l in dti: print (l)


# In[20]:


# this is a list of objects, not timestamps...
# Throws an error in 0.20.1
# pd.to_datetime(['Aug 1, 2014', 'foo'])


# In[21]:


# force the conversion, NaT for items that dont work
pd.to_datetime(['Aug 1, 2014', 'foo'], errors="coerce")


# In[22]:


# create a range of dates starting at a specific date
# and for a specific number of days, creating a Series
np.random.seed(123456)
periods = pd.date_range('8/1/2014', periods=10)
date_series = pd.Series(np.random.randn(10), index=periods)
date_series


# In[23]:


# slice by location
subset = date_series[3:7]
subset


# In[24]:


# a Series to demonstrate alignment
s2 = pd.Series([10, 100, 1000, 10000], subset.index)
s2


# In[25]:


# demonstrate alignment by date on a subset of items
date_series + s2


# In[26]:


# lookup item by a string representing a date
date_series['2014-08-05']


# In[27]:


# slice between two dates specified by string representing dates
date_series['2014-08-05':'2014-08-07']


# In[28]:


# a two year range of daily data in a Series
# only select those in 2013
s3 = pd.Series(0, pd.date_range('2013-01-01', '2014-12-31'))
s3['2013']


# In[29]:


# 31 items for May 2014
s3['2014-05'] 


# In[30]:


# items between two months
s3['2014-08':'2014-09']


# # Creating time-series data with specific frequencies

# In[31]:


# generate a Series at one minute intervals
np.random.seed(123456)
bymin = pd.Series(np.random.randn(24*60*90), 
                  pd.date_range('2014-08-01', 
                                '2014-10-29 23:59',
                                freq='T'))
bymin[:5]


# In[32]:


# slice down to the minute
bymin['2014-08-01 00:02':'2014-08-01 00:07']


# In[33]:


# generate a series based upon business days
days = pd.date_range('2014-08-29', '2014-09-05', freq='B')
days


# In[34]:


# periods will use the frequency as the increment
pd.date_range('2014-08-01 12:10:01', freq='S', periods=5)


# # Date offsets

# In[35]:


# get all business days between and inclusive of these two dates
dti = pd.date_range('2014-08-29', '2014-09-05', freq='B')
dti.values


# In[36]:


# check the frequency is BusinessDay
dti.freq


# In[37]:


# calculate a one day offset from 2014-8-29
d = datetime(2014, 8, 29)
do = pd.DateOffset(days = 1) 
d + do


# In[38]:


# import the data offset types
from pandas.tseries.offsets import *
# calculate one business day from 2014-8-31
d + BusinessDay()


# In[39]:


# determine 2 business days from 2014-8-29
d + 2 * BusinessDay()


# In[40]:


# what is the next business month end
# from a specific date?
d + BMonthEnd()


# In[41]:


# calculate the next month end by
# rolling forward from a specific date
BMonthEnd().rollforward(datetime(2014, 9, 15))


# In[42]:


# calculate the date of the Tuesday previous
# to a specified date 
d - Week(weekday = 1)


# # Anchored Offsets

# In[43]:


# calculate all Wednesdays between 2014-06-01
# and 2014-08-31
wednesdays = pd.date_range('2014-06-01', 
                           '2014-07-31', freq="W-WED")
wednesdays.values


# In[44]:


# what are all of the business quarterly end
# dates in 2014?
qends = pd.date_range('2014-01-01', '2014-12-31', 
                      freq='BQS-JUN')
qends.values


# # The Period object

# In[45]:


# create a period representing a month of time
# starting in August 2014
aug2014 = pd.Period('2014-08', freq='M')
aug2014


# In[46]:


# examine the start and end times of this period
aug2014.start_time, aug2014.end_time


# In[47]:


# calculate the period that is one frequency
# unit of the aug2014 period further along in time
# This happens to be September 2014
sep2014 = aug2014 + 1
sep2014


# In[48]:


sep2014.start_time, sep2014.end_time


# # The PeriodIndex

# In[49]:


# create a period index representing all monthly boundaries in 2013
mp2013 = pd.period_range('1/1/2013', '12/31/2013', freq='M')
mp2013


# In[50]:


# loop through all period objects in the index
# printing start and end time for each
for p in mp2013: 
    print ("{0} {1}".format(p.start_time, p.end_time))


# In[51]:


# create a Series with a PeriodIndex
np.random.seed(123456)
ps = pd.Series(np.random.randn(12), mp2013)
ps[:5]


# In[52]:


# create a Series with a PeriodIndex and which
# represents all calendar month periods in 2013 and 2014
np.random.seed(123456)
ps = pd.Series(np.random.randn(24), 
               pd.period_range('1/1/2013', 
                               '12/31/2014', freq='M'))
ps


# In[53]:


# get value for period represented with 2014-06
ps['2014-06']


# In[54]:


# get values for all periods in 2014
ps['2014']


# In[55]:


# all values between (and including) March and June 2014
ps['2014-03':'2014-06']


# # Handling holidays using calendars

# In[56]:


# demonstrate using the US federal holiday calendar
# first need to import it
from pandas.tseries.holiday import *
# create it and show what it considers holidays
cal = USFederalHolidayCalendar()
for d in cal.holidays(start='2014-01-01', end='2014-12-31'):
    print (d)


# In[57]:


# create CustomBusinessDay object based on the federal calendar
cbd = CustomBusinessDay(holidays=cal.holidays())

# now calc next business day from 2014-8-29
datetime(2014, 8, 29) + cbd


# # Normalizing timestamps using time zones

# In[58]:


# get the current local time and demonstrate there is no
# timezone info by default
now = pd.Timestamp('now')
now, now.tz is None


# In[59]:


# default DatetimeIndex and its Timestamps do not have
# time zone information
rng = pd.date_range('3/6/2012 00:00', periods=15, freq='D')
rng.tz is None, rng[0].tz is None


# In[60]:


# import common timezones from pytz
from pytz import common_timezones
# report the first 5
common_timezones[:5]


# In[61]:


# get now, and now localized to UTC
now = Timestamp("now")
local_now = now.tz_localize('UTC')
now, local_now


# In[62]:


# localize a timestamp to US/Mountain time zone
tstamp = Timestamp('2014-08-01 12:00:00', tz='US/Mountain')
tstamp


# In[63]:


# create a DatetimeIndex using a timezone
rng = pd.date_range('3/6/2012 00:00:00', 
                    periods=10, freq='D', tz='US/Mountain')
rng.tz, rng[0].tz


# In[64]:


# show use of timezone objects
# need to reference pytz
import pytz
# create an object for two different timezones
mountain_tz = pytz.timezone("US/Mountain")
eastern_tz = pytz.timezone("US/Eastern")
# apply each to 'now'
mountain_tz.localize(now), eastern_tz.localize(now)


# In[65]:


# create two Series, same start, same periods, same frequencies,
# each with a different timezone
s_mountain = Series(np.arange(0, 5),
                    index=pd.date_range('2014-08-01', 
                                        periods=5, freq="H", 
                                        tz='US/Mountain'))
s_eastern = Series(np.arange(0, 5), 
                   index=pd.date_range('2014-08-01', 
                                       periods=5, freq="H", 
                                       tz='US/Eastern'))
s_mountain


# In[66]:


s_eastern


# In[67]:


# add the two Series. This only results in three items being aligned
s_eastern + s_mountain


# In[68]:


# convert s1 from US/Eastern to US/Pacific
s_pacific = s_eastern.tz_convert("US/Pacific")
s_pacific


# In[69]:


# this will be the same result as s_eastern + s_mountain
# as the timezones still get aligned to be the same
s_mountain + s_pacific


# # Shifting and lagging 

# In[70]:


# create a Series to work with
np.random.seed(123456)
ts = Series([1, 2, 2.5, 1.5, 0.5],
            pd.date_range('2014-08-01', periods=5))
ts


# In[71]:


# shift forward one day
ts.shift(1)


# In[72]:


# lag two days
ts.shift(-2)


# In[73]:


# calculate daily percentage change
ts / ts.shift(1)


# In[74]:


# shift forward one business day
ts.shift(1, freq="B")


# In[75]:


# shift forward five hours
ts.tshift(5, freq="H")


# In[76]:


# shift using a DateOffset
ts.shift(1, DateOffset(minutes=0.5))


# In[77]:


# shift just the index values
ts.tshift(-1, freq='H')


# # Frequency Conversion

# In[78]:


# create a Series of incremental values
# index by hour through all of August 2014
periods = 31 * 24
hourly = Series(np.arange(0, periods),
               pd.date_range('08-01-2014', freq="2H", 
                             periods = periods))
hourly[:5]


# In[79]:


# convert to daily frequency
# many items will be dropped due to alignment
daily = hourly.asfreq('D')
daily[:5]


# In[80]:


# convert back to hourly.  Results in many NaNs
# as the new index has many labels that do not
# align from the source
daily.asfreq('H')


# In[81]:


# forward fill values
daily.asfreq('H', method='ffill')


# In[82]:


daily.asfreq('H', method='bfill')


# # Up and down resampling

# In[83]:


# calculate a random walk five days long at one second intervals
# this many items will be needed
count = 24 * 60 * 60 * 5
# create a series of values
np.random.seed(123456)
values = np.random.randn(count)
ws = pd.Series(values)
# calculate the walk
walk = ws.cumsum()
# patch the index
walk.index = pd.date_range('2014-08-01', periods=count, freq="S")
walk


# In[84]:


# resample to minute intervals
walk.resample("1Min").mean()


# In[85]:


# calculate the mean of the first minute of the walk
walk['2014-08-01 00:00'].mean()


# In[86]:


# use a right close
walk.resample("1Min", closed='right').mean()


# In[87]:


# resample to 1 minute
walk.resample("1Min").first()


# In[88]:


# resample to 1 minute intervales, then back to 1 sec
bymin = walk.resample("1Min").mean()
bymin.resample('S').mean()


# In[89]:


# resample to 1 second intervales using forward fill
bymin.resample("S").bfill()


# In[90]:


# demonstate interoplating the NaN values
interpolated = bymin.resample("S").interpolate()
interpolated


# In[91]:


# show ohlc resampling
ohlc = walk.resample("H").ohlc()
ohlc


# # Time series moving window operations

# In[92]:


# get data from only the following minute
first_minute = walk['2014-08-01 00:00']
# calculate a rol1ing mean window of 5 periods
means = first_minute.rolling(window=5, center=False).mean()
# plot means vs original data
means.plot()
first_minute.plot();


# In[93]:


# demonstrate the difference between 2, 5 and
# 10 interval rolling windows
h1w = walk['2014-08-01 00:00']
means2 = h1w.rolling(window=2, center=False).mean()
means5 = h1w.rolling(window=5, center=False).mean()
means10 = h1w.rolling(window=10, center=False).mean()
h1w.plot()
means2.plot()
means5.plot()
means10.plot();


# In[94]:


# calculate mean average deviation with window of 5 intervals
mean_abs_dev = lambda x: np.fabs(x - x.mean()).mean()
means = h1w.rolling(window=5, center=False).apply(mean_abs_dev)
means.plot();


# In[95]:


# calculate an expanding rolling mean
h1w.plot()
expanding = h1w.expanding(min_periods=1).mean()
expanding.plot();

