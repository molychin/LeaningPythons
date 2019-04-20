
# coding: utf-8

# ## Accessing Data

# In[ ]:


Specifcally, in this chapter, we will cover:
• Reading and writing pandas data from files
• Working with data in CSV, JSON, HTML, Excel, and HDF5 formats
• Accessing data on the web and in the cloud
• Reading and writing from/to SQL databases
• Reading data from remote web data services


# ### Reading a CSV fle into a DataFrame

# In[9]:


# read in msft.csv into a DataFrame
import numpy as np
import pandas as pd

msft = pd.read_csv("data/msft.csv")
msft.head()

#Specifying the index column when reading a CSV fle
# use column 0 as the index
msft = pd.read_csv("data/msft.csv", index_col=0)   #指定0列即第1列作为索引
msft.head()
#Data type inference and specifcation
# examine the types of the columns in this DataFrame
msft.dtypes   #列出所有列的数据类型
#To force the types of columns, use the dtypes parameter of pd.read_csv().
#The following forces the Volume column to also be float64:
# specify that the Volume column should be a float64
msft = pd.read_csv("data/msft.csv",dtype = { 'Volume' : np.float64})
msft.dtypes
#Specifying column names
# specify a new set of names for the columns
# all lower case, remove space in Adj Close
# also, header=0 skips the header row
df = pd.read_csv("data/msft.csv",header=0,names=['open', 'high', 'low','close', 'volume', 'adjclose'])
df.head()
#Specifying specifc columns to load
# read in data only in the Date and Close columns
# and index by the Date column
df2 = pd.read_csv("data/msft.csv",usecols=['Date', 'Close'],index_col=['Date'])    #载入指定列数据
df2.head()

### Saving DataFrame to a CSV fle
# save df2 to a new csv file
# also specify naming the index as date

#It was necessary to tell the method that the index label should be saved with a column
#name of date using index_label=date. Otherwise, the index does not have a name
#added to the frst row of the fle, which makes it diffcult to read back properly.
df2.to_csv("data/msft_modified.csv")
#df2.to_csv("data/msft_modified.csv", index_label='date')




# In[11]:


# use read_table with sep=',' to read a CSV
df = pd.read_table("data/msft.csv", sep=',')
df.head()
# save as pipe delimited
df.to_csv("data/msft_piped.txt", sep='|')




# ### Handling noise rows in feld-delimited data

# In[16]:


# read, but skip rows 0, 2 and 3
df = pd.read_csv("data/msft2.csv", skiprows=[0, 2, 3])  #读取文件时，跳过头部的第0、2、3行
df
# skip only two lines at the end
#df = pd.read_csv("data/msft_with_footer.csv",skipfooter=2) 
#C:\ProgramData\Anaconda3a\lib\site-packages\ipykernel_launcher.py:5: ParserWarning: 
#Falling back to the 'python' engine because the 'c' engine does not support skipfooter; 
#you can avoid this warning by specifying engine='python'.
df = pd.read_csv("data/msft_with_footer.csv",skipfooter=2,engine = 'python')   #跳过文件尾部的2行
df






# In[ ]:


第二版P84.   2015第一版 P203

