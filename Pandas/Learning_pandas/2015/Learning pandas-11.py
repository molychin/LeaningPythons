
# coding: utf-8

# ## Visualization

# In[19]:


'''
Humans are visual creatures and have evolved to be able to quickly notice the
meaning when information is presented in certain ways that cause the wiring in our
brains to have the light bulb of insight turn on. This "aha" can often be performed
very quickly, given the correct tools, instead of through tedious numerical analysis.
人类是视觉生物，当信息以某种方式呈现时，人类已经进化到能够迅速注意到它的意义，
而这种方式会导致我们大脑中的连线打开“洞察”的灯泡。如果使用正确的工具，而不是通过繁琐的
数值分析，这种“aha”通常可以很快执行。

Tools for data analysis, such as pandas, take advantage of being able to quickly
and iteratively provide the user to take data, process it, and quickly visualize the
meaning. Often, much of what you will do with pandas is massaging your data to
be able to visualize it in one or more visual patterns, in an attempt to get to "aha" by
simply glancing at the visual representation of the information.
用于数据分析的工具（如pandas）利用能够快速和迭代地为用户提供数据获取、处理和快速可视化含义
的优势。通常，你对大熊猫所做的大部分工作就是按摩你的数据，使其能够以一种或多种视觉模式呈现
出来，试图通过简单地浏览信息的视觉表现来达到“啊哈”的目的。

This chapter will cover common patterns in visualizing data with pandas. It is not
meant to be exhaustive in coverage. The goal is to give you the required knowledge
to create beautiful data visualizations on pandas data quickly and with very few
lines of code.
本章将介绍大熊猫数据可视化的常见模式。它并不意味着覆盖范围太广。我们的目标是为您提供
所需的知识，使您能够快速、少用几行代码在熊猫数据上创建漂亮的数据可视化。
'''



# In[20]:


'''
• Bar plots
• Histograms
• Box and whisker charts
• Area plots
• Scatter plots
• Density plots
• Scatter plot matrixes
• Heatmaps
'''


# In[21]:


'''
Plotting basics with pandas
The pandas library itself performs data manipulation. It does not provide data
visualization capabilities itself. The visualization of data in pandas data structures is
handed off by pandas to other robust visualization libraries that are part of the Python
ecosystem, most commonly, matplotlib, which is what we will use in this chapter.
熊猫图书馆本身执行数据操作。它不提供数据可视化功能本身。熊猫数据结构中的数据可视化由熊猫
传递给其他健壮的可视化库，这些库是Python生态系统的一部分，最常见的是matplotlib，我们将在本章中使用它。
'''



# In[1]:


#Creating time-series charts with .plot()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

seedval = 111111

# generate a random walk time-series
np.random.seed(seedval)
s = pd.Series(np.random.randn(1096),index=pd.date_range('2012-01-01','2014-12-31'))
walk_ts = s.cumsum()
# this plots the walk - just that easy :)
'''
The .plot() method on pandas objects is a wrapper function around the matplotlib
libraries' plot() function. It makes plots of pandas data very easy to create. It is
coded to know how to use the data in the pandas objects to create the appropriate
plots for the data, handling many of the details of plot generation, such as selecting
series, labeling, and axes generation. In this situation, the .plot() method
determines that as Series contains dates for its index that the x axis should be
formatted as dates and it selects a default color for the data.
pandas对象上的.plot（）方法是matplotlib库的plot（）函数的包装函数。它使大熊猫数据的绘制变
得非常容易。它被编码为知道如何使用熊猫对象中的数据为数据创建适当的绘图，处理绘图生成的许
多细节，例如选择系列、标记和轴生成。在这种情况下，.plot（）方法确定as-series包含索引的日期，
x轴应格式化为日期，并为数据选择默认颜色。
'''

walk_ts.plot();
plt.show()


# In[11]:


# a DataFrame with a single column will produce
# the same plot as plotting the Series it is created from
walk_df = pd.DataFrame(walk_ts)
walk_df.plot();
plt.show()


# In[15]:


# generate two random walks, one in each of
# two columns in a DataFrame
np.random.seed(seedval)
df = pd.DataFrame(np.random.randn(1096, 2),index=walk_ts.index, columns=list('AB'))
walk_df = df.cumsum()
print(walk_df.head())
# plot the DataFrame, which will plot a line
# for each column, with a legend
walk_df.plot();
plt.show()


# In[25]:


# copy the walk

df2 = walk_df.copy()
# add a column C which is 0 .. 1096
df2['C'] = pd.Series(np.arange(0, len(df2)), index=df2.index)
# instead of dates on the x axis, use the 'C' column,
# which will label the axis with 0..1000
df2.plot(x='C', y=['A', 'B'])
plt.show()


# In[26]:


'''
The built-in .plot() method has many options that you can use to change the
content in the plot. We will cover several of the common options used in most plots.
Adding a title and changing axes labels
The title of the chart can be set using the title parameter of the .plot() method.
Axes labels are not set with .plot(), but by directly using the plt.ylabel()
and plt.xlabel() functions after calling .plot():
'''


# In[27]:


# create a time-series chart with a title and specific
# x and y axes labels
# the title is set in the .plot() method as a parameter
walk_df.plot(title='Title of the Chart')
# explicitly set the x and y axes labels after the .plot()
plt.xlabel('Time')
plt.ylabel('Money');
plt.show()



# In[32]:


#Specifying the legend content and position
# change the legend items to be different
# from the names of the columns in the DataFrame
ax = walk_df.plot(title='Title of the Chart')
ax =walk_df.plot(title='Title of the Chart', legend=False)  #关闭标签显示
# this sets the legend labels
#ax.legend(['1', '2'])    #修改图例标识
'''
However, you can
also specify any of the following to position the legend more specifically (you can use
either the string or the numeric code):
Text Code
'best' 0
'upper right' 1
'upper left' 2
'lower left' 3
'lower right' 4
'right' 5
'center left' 6
'center right' 7
'lower center' 8
'upper center' 9
'center' 10
'''
ax.legend(['1', '2'], loc='upper center')
# omit the legend by using legend=False

plt.show()


# In[35]:


#Specifying line colors, styles, thickness, and markers

# change the line colors on the plot
# use character code for the first line,
# hex RGB for the second
walk_df.plot(style=['g', '#FF0000'])

plt.show()


# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

# show off different line styles
t = np.arange(0., 5., 0.2)
legend_labels = ['Solid', 'Dashed', 'Dotted','Dot-dashed', 'Points']
line_style = pd.DataFrame({0 : t,1 : t**1.5,2 : t**2.0,3 : t**2.5,4 : t**3.0})
# generate the plot, specifying color and line style for each line
ax = line_style.plot(style=['r-', 'g--', 'b:', 'm-.', 'k:'])
# set the legend
ax.legend(legend_labels, loc='upper left')
plt.show()


# In[2]:


# regenerate the plot, specifying color and line style
# for each line and a line width of 3 for all lines
ax = line_style.plot(style=['r-', 'g--', 'b:', 'm-.', 'k:'], lw=3)
ax.legend(legend_labels, loc='upper left')

plt.show()


# In[3]:


# redraw, adding markers to the lines
ax = line_style.plot(style=['r-o', 'g--^', 'b:*','m-.D', 'k:o'], lw=3)
ax.legend(legend_labels, loc='upper left')

plt.show()


# #### Specifying tick mark locations and tick labels
# Every plot we have seen to this point, has used the default tick marks and labels
# on the ticks that pandas decides are appropriate for the plot. These can also be
# customized using various matplotlib functions.

# In[6]:


# a simple plot to use to examine ticks
ticks_data = pd.DataFrame(np.arange(0,5))
ticks_data.plot()
ticks, labels = plt.xticks()
ticks
plt.show()


# In[7]:


# resize x axis to (-1, 5), and draw ticks
# only at integer values
ticks_data = pd.DataFrame(np.arange(0,5))
ticks_data.plot()
plt.xticks(np.arange(-1, 6))

plt.show()


# In[8]:


# rename y axis tick labels to A, B, C, D, and E
ticks_data = pd.DataFrame(np.arange(0,5))
ticks_data.plot()
plt.yticks(np.arange(0, 5), list("ABCDE"))

plt.show()


# #### Formatting axes tick date labels using formatters

# In[16]:


# plot January-February 2014 from the random walk
walk_df.loc['2014-01':'2014-02'].plot()
plt.show()


# In[17]:


# this import styles helps us type less
from matplotlib.dates import WeekdayLocator,DateFormatter, MonthLocator
# plot Jan-Feb 2014
ax = walk_df.loc['2014-01':'2014-02'].plot()
# do the minor labels
weekday_locator = WeekdayLocator(byweekday=(0), interval=1)
ax.xaxis.set_minor_locator(weekday_locator)
ax.xaxis.set_minor_formatter(DateFormatter("%d\n%a"))
# do the major labels
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter('\n\n\n%b\n%Y'))

plt.show()


# In[20]:


# this gets around the pandas / matplotlib year issue
# need to reference the subset twice, so let's make a variable
walk_subset = walk_df['2014-01':'2014-02']
# this gets the plot so we can use it, we can ignore fig
fig, ax = plt.subplots()
# inform matplotlib that we will use the following as dates
# note we need to convert the index to a pydatetime series
ax.plot_date(walk_subset.index.to_pydatetime(), walk_subset, '-')
# do the minor labels
weekday_locator = WeekdayLocator(byweekday=(0), interval=1)
ax.xaxis.set_minor_locator(weekday_locator)
ax.xaxis.set_minor_formatter(DateFormatter('%d\n%a'))
# do the major labels
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter('\n\n\n%b\n%Y'));
ax.xaxis.set_major_formatter(DateFormatter('\n\n\n%b\n%Y'));

plt.show()


# In[21]:


# this gets the plot so we can use it, we can ignore fig
fig, ax = plt.subplots()
# inform matplotlib that we will use the following as dates
# note we need to convert the index to a pydatetime series
ax.plot_date(walk_subset.index.to_pydatetime(), walk_subset, '-')
# do the minor labels
weekday_locator = WeekdayLocator(byweekday=(0), interval=1)
ax.xaxis.set_minor_locator(weekday_locator)
ax.xaxis.set_minor_formatter(DateFormatter('%d\n%a'))
ax.xaxis.grid(True, "minor") # turn on minor tick grid lines
ax.xaxis.grid(False, "major") # turn off major tick grid lines
# do the major labels
ax.xaxis.set_major_locator(MonthLocator())
ax.xaxis.set_major_formatter(DateFormatter('\n\n\n%b\n%Y'));

plt.show()


# In[22]:


# this gets the plot so we can use it, we can ignore fig
fig, ax = plt.subplots()
# inform matplotlib that we will use the following as dates
# note we need to convert the index to a pydatetime series
ax.plot_date(walk_subset.index.to_pydatetime(), walk_subset, '-')
ax.xaxis.grid(True, "major") # turn off major tick grid lines
# do the major labels
ax.xaxis.set_major_locator(weekday_locator)
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'));
# informs to rotate date labels
fig.autofmt_xdate();

plt.show()


# ### Common plots used in statistical analyses
# Having seen how to create, lay out, and annotate time-series charts, we will now
# look at creating a number of charts, other than time series that are commonplace in
# presenting statistical information.
# 在了解了如何创建、布局和注释时间序列图之后，我们现在将了解如何创建许多图表，而不是在呈现统计信息时常见的时间序列。

# #### Bar plots 条状图
# Bar plots are useful in order to visualize the relative differences in values of
# non time-series data. Bar plots can be created using the kind='bar' parameter
# of the .plot() method

# In[23]:


# make a bar plot
# create a small series of 10 random values centered at 0.0
np.random.seed(seedval)
s = pd.Series(np.random.rand(10) - 0.5)
# plot the bar chart
s.plot(kind='bar')

plt.show()


# In[24]:


# draw a multiple series bar chart
# generate 4 columns of 10 random values
np.random.seed(seedval)
df2 = pd.DataFrame(np.random.rand(10, 4),columns=['a', 'b', 'c', 'd'])
# draw the multi-series bar chart
df2.plot(kind='bar')

plt.show()


# In[25]:


# horizontal stacked bar chart
df2.plot(kind='bar', stacked=True)

plt.show()


# In[26]:


# horizontal stacked bar chart
df2.plot(kind='barh', stacked=True)

plt.show()


# ### Histograms  直方图

# In[27]:


# create a histogram
np.random.seed(seedval)
# 1000 random numbers
dfh = pd.DataFrame(np.random.randn(1000))
# draw the histogram
dfh.hist()

plt.show()


# In[28]:


# histogram again, but with more bins
dfh.hist(bins = 100)

plt.show()


# In[31]:


# generate a multiple histogram plot  生成多个柱状图
# create DataFrame with 4 columns of 1000 random values
np.random.seed(seedval)
dfh = pd.DataFrame(np.random.randn(1000, 4),columns=['A', 'B', 'C', 'D'])
# draw the chart. There are four columns so pandas draws
# four historgrams
dfh.hist(bins=30)

plt.show()


# In[32]:


# directly use pyplot to overlay multiple histograms
# generate two distributions, each with a different
# mean and standard deviation
np.random.seed(seedval)
x = [np.random.normal(3,1) for _ in range(400)]
y = [np.random.normal(4,2) for _ in range(400)]
# specify the bins (-10 to 10 with 100 bins)
bins = np.linspace(-10, 10, 100)
# generate plot x using plt.hist, 50% transparent
plt.hist(x, bins, alpha=0.5, label='x')
# generate plot y using plt.hist, 50% transparent
plt.hist(y, bins, alpha=0.5, label='y')
plt.legend(loc='upper right')

plt.show()


# #### Box and whisker charts 方格和胡须图???
# Box plots come from descriptive statistics and are a useful way of graphically
# depicting the distributions of categorical data using quartiles. Each box represents
# the values between the frst and third quartiles of the data with a line across the
# box at the median. Each whisker reaches out to demonstrate the extent to five
# interquartile ranges below and above the frst and third quartiles:

# In[34]:


# create a box plot
# generate the series
np.random.seed(seedval)
dfb = pd.DataFrame(np.random.randn(10,5))
print(dfb)
# generate the plot
dfb.boxplot(return_type='axes')

plt.show()


# #### Area plots 面积图
# Area plots are used to represent cumulative totals over time, to demonstrate the
# change in trends over time among related attributes. They can also be "stacked"
# to demonstrate representative totals across all variables.
# 面积图用于表示随时间累积的总量，以显示相关属性随时间变化的趋势。它们也可以“叠加”以显示所有变量的代表性总计。

# In[35]:


# create a stacked area plot
# generate a 4-column data frame of random data
np.random.seed(seedval)
dfa = pd.DataFrame(np.random.rand(10, 4),columns=['A', 'B', 'C', 'D'])
# create the area plot
dfa.plot(kind='area')

plt.show()   


# In[36]:


# do not stack the area plot
dfa.plot(kind='area', stacked=False)

plt.show()


# #### Scatter plots 散点图
# A scatter plot displays the correlation between a pair of variables. 
# 散点图显示一对变量之间的相关性。

# In[39]:


# generate a scatter plot of two series of normally
# distributed random values
# we would expect this to cluster around 0,0
np.random.seed(111111)
sp_df = pd.DataFrame(np.random.randn(10000, 2),columns=['A', 'B'])
sp_df.plot(kind='scatter', x='A', y='B')

plt.show()


# In[3]:


# get Google stock data from 1/1/2011 to 12/31/2011
#from pandas.io.data import DataReader
import pandas_datareader.data as web

stock_data = DataReader("GOOGL", "yahoo",datetime(2011, 1, 1),datetime(2011, 12, 31))
# % change per day
delta = np.diff(stock_data["Adj Close"])/stock_data["Adj Close"][:-1]
# this calculates size of markers
volume = (15 * stock_data.Volume[:-2] / stock_data.Volume[0])**2
close = 0.003 * stock_data.Close[:-2] / 0.003 * stock_data.Open[:-2]
# generate scatter plot
fig, ax = plt.subplots()
ax.scatter(delta[:-1], delta[1:], c=close, s=volume, alpha=0.5)
# add some labels and style
ax.set_xlabel(r'$\Delta_i$', fontsize=20)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=20)
ax.set_title('Volume and percent change')
ax.grid(True)

plt.show()


# In[ ]:


第二版P84.   2015第一版 P429

