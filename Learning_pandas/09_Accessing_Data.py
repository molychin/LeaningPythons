
# coding: utf-8

# # Configuring pandas

# In[1]:


# import numpy and pandas
import numpy as np
import pandas as pd

# used for dates
import datetime
from datetime import datetime, date

# Set some pandas options controlling output format
pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 8)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 90)

# bring in matplotlib for graphics
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:


# view the first five lines of data/msft.csv
get_ipython().system('head -n 5 data/msft.csv # mac or Linux')
# type data/msft.csv # on windows, but shows the entire file


# # Reading a CSV into a DataFrame

# In[3]:


# read in msft.csv into a DataFrame
msft = pd.read_csv("data/msft.csv")
msft[:5]


# # Specifying the index column when reading a CSV file

# In[4]:


# use column 0 as the index
msft = pd.read_csv("data/msft.csv", index_col=0)
msft[:5]


# # Data type inference and specification

# In[5]:


# examine the types of the columns in this DataFrame
msft.dtypes


# In[6]:


# specify that the Volume column should be a float64
msft = pd.read_csv("data/msft.csv", 
                   dtype = { 'Volume' : np.float64})
msft.dtypes


# # Specifying column names

# In[7]:


# specify a new set of names for the columns
# all lower case, remove space in Adj Close
# also, header=0 skips the header row
df = pd.read_csv("data/msft.csv", 
                 header=0,
                 names=['date', 'open', 'high', 'low', 
                        'close', 'volume'])
df[:5]


# # Specifying specific columns to load

# In[8]:


# read in data only in the Date and Close columns
# and index by the Date column
df2 = pd.read_csv("data/msft.csv", 
                  usecols=['Date', 'Close'], 
                  index_col=['Date'])
df2[:5]


# # Saving a DataFrame to a CSV

# In[9]:


# save df2 to a new csv file
# also specify naming the index as date
df2.to_csv("data/msft_modified.csv", index_label='date')


# In[10]:


# view the start of the file just saved
get_ipython().system('head -n 5 data/msft_modified.csv')
#type data/msft_modified.csv # windows


# # General field-delimited data

# In[11]:


# use read_table with sep=',' to read a CSV
df = pd.read_table("data/msft.csv", sep=',')
df[:5]


# In[12]:


# save as pipe delimited
df.to_csv("data/msft_piped.txt", sep='|')
# check that it worked
get_ipython().system('head -n 5 data/msft_piped.txt # osx or Linux')
# type data/psft_piped.txt # on windows


# # Handling variants of formats in field-delimited data

# In[13]:


# messy file
get_ipython().system('head -n 6 data/msft2.csv # osx or Linux')
# type data/msft2.csv # windows


# In[14]:


# read, but skip rows 0, 2 and 3
df = pd.read_csv("data/msft2.csv", skiprows=[0, 2, 3])
df[:5]


# In[15]:


# another messy file, with the mess at the end
get_ipython().system('cat data/msft_with_footer.csv # osx or Linux')
# type data/msft_with_footer.csv # windows


# In[16]:


# skip only two lines at the end
df = pd.read_csv("data/msft_with_footer.csv", 
                 skipfooter=2,
                 engine = 'python')
df


# In[17]:


# only process the first three rows
pd.read_csv("data/msft.csv", nrows=3)


# In[18]:


# skip 100 lines, then only process the next five
pd.read_csv("data/msft.csv", skiprows=100, nrows=5, 
            header=0,
            names=['date', 'open', 'high', 'low', 
                   'close', 'vol']) 


# # Reading and writing data in Excel format

# In[19]:


# read excel file
# only reads first sheet (msft in this case)
df = pd.read_excel("data/stocks.xlsx")
df[:5]


# In[20]:


# read from the aapl worksheet
aapl = pd.read_excel("data/stocks.xlsx", sheetname='aapl')
aapl[:5]


# In[21]:


# save to an .XLS file, in worksheet 'Sheet1'
df.to_excel("data/stocks2.xls")


# In[22]:


# write making the worksheet name MSFT
df.to_excel("data/stocks_msft.xls", sheet_name='MSFT')


# In[23]:


# write multiple sheets
# requires use of the ExcelWriter class
from pandas import ExcelWriter
with ExcelWriter("data/all_stocks.xls") as writer:
    aapl.to_excel(writer, sheet_name='AAPL')
    df.to_excel(writer, sheet_name='MSFT')


# In[24]:


# write to xlsx
df.to_excel("data/msft2.xlsx")


# # Reading and writing JSON files

# In[25]:


# wirite the excel data to a JSON file
df[:5].to_json("data/stocks.json")
get_ipython().system('cat data/stocks.json # osx or Linux')
#type data/stocks.json # windows


# In[26]:


# read data in from JSON
df_from_json = pd.read_json("data/stocks.json")
df_from_json[:5]


# In[27]:


# the URL to read
url = "http://www.fdic.gov/bank/individual/failed/banklist.html"
# read it
banks = pd.read_html(url)


# In[28]:


# examine a subset of the first table read
banks[0][0:5].iloc[:,0:2]


# In[29]:


# read the stock data
df = pd.read_excel("data/stocks.xlsx")
# write the first two rows to HTML
df.head(2).to_html("data/stocks.html")
# check the first 28 lines of the output
get_ipython().system('head -n 10 data/stocks.html # max or Linux')
# type data/stocks.html # window, but prints the entire file


# # Reading and writing HDF5 format files

# In[30]:


# seed for replication
np.random.seed(123456)
# create a DataFrame of dates and random numbers in three columns
df = pd.DataFrame(np.random.randn(8, 3), 
                  index=pd.date_range('1/1/2000', periods=8),
                  columns=['A', 'B', 'C'])

# create HDF5 store
store = pd.HDFStore('data/store.h5')
store['df'] = df # persisting happened here
store


# In[31]:


# read in data from HDF5
store = pd.HDFStore("data/store.h5")
df = store['df']
df[:5]


# In[32]:


# this changes the DataFrame, but did not persist
df.iloc[0].A = 1 
# to persist the change, assign the DataFrame to the 
# HDF5 store object
store['df'] = df
# it is now persisted
# the following loads the store and 
# shows the first two rows, demonstrating
# the the persisting was done
pd.HDFStore("data/store.h5")['df'][:5] # it's now in there


# # Accessing data on the web and in the cloud

# In[33]:


# read csv directly from Yahoo! Finance from a URL
msft_hist = pd.read_csv(
    "http://www.google.com/finance/historical?" +
    "q=NASDAQ:MSFT&startdate=Apr+01%2C+2017&" +
    "enddate=Apr+30%2C+2017&output=csv")
msft_hist[:5]


# # Reading and writing from/to SQL databases

# In[34]:


# reference SQLite
import sqlite3

# read in the stock data from CSV
msft = pd.read_csv("data/msft.csv")
msft["Symbol"]="MSFT"
aapl = pd.read_csv("data/aapl.csv")
aapl["Symbol"]="AAPL"

# create connection
connection = sqlite3.connect("data/stocks.sqlite")
# .to_sql() will create SQL to store the DataFrame
# in the specified table.  if_exists specifies
# what to do if the table already exists
msft.to_sql("STOCK_DATA", connection, if_exists="replace")
aapl.to_sql("STOCK_DATA", connection, if_exists="append")

# commit the SQL and close the connection
connection.commit()
connection.close()


# In[35]:


# connect to the database file
connection = sqlite3.connect("data/stocks.sqlite")

# query all records in STOCK_DATA
# returns a DataFrame
# inde_col specifies which column to make the DataFrame index
stocks = pd.io.sql.read_sql("SELECT * FROM STOCK_DATA;", 
                             connection, index_col='index')

# close the connection
connection.close()

# report the head of the data retrieved
stocks[:5]


# In[36]:


# open the connection
connection = sqlite3.connect("data/stocks.sqlite")
# construct the query string
query = "SELECT * FROM STOCK_DATA WHERE " +         "Volume>29200100 AND Symbol='MSFT';"
# execute and close connection
items = pd.io.sql.read_sql(query, connection, index_col='index')
connection.close()
# report the query result
items


# # Reading stock data from Google Finance

# In[37]:


# import data reader package
import pandas_datareader as pdr


# In[38]:


# read from google and display the head of the data
start = datetime(2017, 4, 1)
end = datetime(2017, 4, 30)
goog = pdr.data.DataReader("MSFT", 'google', start, end)
goog[:5]


# # Retrieving options data from Google Finance

# In[39]:


# read options for MSFT
options = pdr.data.Options('MSFT', 'google')


# In[40]:


options.expiry_dates


# In[41]:


data = options.get_options_data(expiry=options.expiry_dates[0])
data.iloc[:5,:3]


# In[42]:


# get all puts at strike price of $30 (first four columns only)
data.loc[(30, slice(None), 'put'), :].iloc[0:5, 0:3]


# In[43]:


# put options at strike of $80, between 2017-06-01 and 2017-06-30
data.loc[(30, slice('20180119','20180130'), 'put'), :]     .iloc[:, 0:3]


# # Reading economic data from the Federal Reserve Bank of St. Louis

# In[44]:


# read GDP data from FRED
gdp = pdr.data.FredReader("GDP",
                     date(2012, 1, 1), 
                     date(2014, 1, 27))
gdp.read()[:5]


# In[45]:


# Get Compensation of employees: Wages and salaries
pdr.data.FredReader("A576RC1A027NBEA",
                date(1929, 1, 1),
                date(2013, 1, 1)).read()[:5]


# # Accessing Kenneth French data

# In[46]:


# read from Kenneth French fama global factors data set
factors = pdr.data.FamaFrenchReader("Global_Factors").read()
factors[0][:5]


# # Reading from the World Bank

# In[47]:


# get all indicators
from pandas_datareader import wb
all_indicators = pdr.wb.get_indicators()
all_indicators.iloc[:5,:2]


# In[48]:


# search of life expectancy indicators
le_indicators = pdr.wb.search("life expectancy")
# report first three rows, first two columns
le_indicators.iloc[:5,:2]


# In[49]:


# get countries and show the 3 digit code and name
countries = pdr.wb.get_countries()
# show a subset of the country data
countries.loc[0:5,['name', 'capitalCity', 'iso2c']]


# In[50]:


# get life expectancy at birth for all countries from 1980 to 2014
le_data_all = pdr.wb.download(indicator="SP.DYN.LE00.IN", 
                          start='1980', 
                          end='2014')
le_data_all


# In[51]:


# only US, CAN, and MEX are returned by default
le_data_all.index.levels[0]


# In[52]:


# retrieve life expectancy at birth for all countries 
# from 1980 to 2014
le_data_all = wb.download(indicator="SP.DYN.LE00.IN", 
                          country = countries['iso2c'],
                          start='1980', 
                          end='2012')
le_data_all


# In[53]:


#le_data_all.pivot(index='country', columns='year')
le_data = le_data_all.reset_index().pivot(index='country', 
                                          columns='year')
# examine pivoted data
le_data.iloc[:5,0:3]


# In[54]:


# ask what is the name of country for each year
# with the least life expectancy
country_with_least_expectancy = le_data.idxmin(axis=0)
country_with_least_expectancy[:5]


# In[55]:


# and what is the minimum life expectancy for each year
expectancy_for_least_country = le_data.min(axis=0)
expectancy_for_least_country[:5]


# In[56]:


# this merges the two frames together and gives us
# year, country and expectancy where there minimum exists
least = pd.DataFrame(
    data = {'Country': country_with_least_expectancy.values,
            'Expectancy': expectancy_for_least_country.values},
    index = country_with_least_expectancy.index.levels[1])
least[:5]

