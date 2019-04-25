
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
pd.set_option('display.width', 65)

# bring in matplotlib for graphics
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# # Creating Categoricals

# In[2]:


# create a categorical directly from a list.  
lmh_values = ["low", "high", "medium", "medium", "high"]
lmh_cat = pd.Categorical(lmh_values)
lmh_cat


# In[3]:


# examine the categories
lmh_cat.categories


# In[4]:


# retreive the values
lmh_cat.get_values()


# In[5]:


# .codes shows the integer mapping for each value of the categorical
lmh_cat.codes


# In[6]:


# create from list but explicitly state the categories
lmh_cat = pd.Categorical(lmh_values,
                         categories=["low", "medium", "high"])
lmh_cat


# In[7]:


# the codes are...
lmh_cat.codes


# In[8]:


# sorting is done using the codes underlying each value
lmh_cat.sort_values()


# In[9]:


# create a categorical using a Series and dtype
cat_series = pd.Series(lmh_values, dtype="category")
cat_series


# In[10]:


# create a categorical using .astype()
s = pd.Series(lmh_values)
as_cat = s.astype('category')
cat_series


# In[11]:


# a categorical has a .cat property that lets you access info
cat_series.cat


# In[12]:


# get the index for the categorical
cat_series.cat.categories


# In[13]:


# create a DataFrame of 100 values
np.random.seed(123456)
values = np.random.randint(0, 100, 5)
bins = pd.DataFrame({ "Values": values})
bins


# In[14]:


# cut the values into 
bins['Group'] = pd.cut(values, range(0, 101, 10))
bins


# In[15]:


# examine the categorical that was created
bins.Group


# In[16]:


# create an ordered categorical of precious metals
# order is important for determining relative value
metal_values = ["bronze", "gold", "silver", "bronze"]
metal_categories = ["bronze", "silver", "gold"]
metals = pd.Categorical(metal_values,
                        categories=metal_categories,
                        ordered = True)
metals


# In[17]:


# reverse the metals
metals_reversed_values = pd.Categorical(
    metals.get_values()[::-1],
    categories = metals.categories, 
    ordered=True)
metals_reversed_values


# In[18]:


# compare the two categoricals
metals <= metals_reversed_values


# In[19]:


# codes are the integer value assocaited with each item
metals.codes


# In[20]:


# and for metals2
metals_reversed_values.codes


# In[21]:


# creating a categorical with a non existent category
pd.Categorical(["bronze", "copper"],
               categories=metal_categories)


# # Renaming Categories

# In[22]:


# create a categorical with 3 categories
cat = pd.Categorical(["a","b","c","a"], 
                     categories=["a", "b", "c"])
cat


# In[23]:


# renames the categories (and also the values)
cat.categories = ["bronze", "silver", "gold"]
cat


# In[24]:


# this also renames 
cat.rename_categories(["x", "y", "z"])


# In[25]:


# the rename is not done in-place
cat


# # Appending new categories

# In[26]:


# add a new platimnum category
with_platinum = metals.add_categories(["platinum"])
with_platinum


# # Removing Categories

# In[27]:


# remove bronze category
no_bronze = metals.remove_categories(["bronze"])
no_bronze


# # Removing unused categories

# In[28]:


# remove any unused categories (in this case, platinum)
with_platinum.remove_unused_categories()


# # Setting categories

# In[29]:


# sample Series
s = pd.Series(["one","two","four", "five"], dtype="category")
s


# In[30]:


# remove the "two", "three" and "five" categories (replaced with NaN)
s = s.cat.set_categories(["one","four"])
s


# # Describe

# In[31]:


# get descriptive info on the metals categorical
metals.describe()


# # Value counts

# In[32]:


# count the values in the categorical
metals.value_counts()


# # Minimum, maximum and mode

# In[33]:


# find the min, max and mode of the metals categorical
(metals.min(), metals.max(), metals.mode())


# # Munging school grades

# In[34]:


# 10 students with random grades
np.random.seed(123456)
names = ['Ivana', 'Norris', 'Ruth', 'Lane', 'Skye', 'Sol', 
         'Dylan', 'Katina', 'Alissa', "Marc"]
grades = np.random.randint(50, 101, len(names))
scores = pd.DataFrame({'Name': names, 'Grade': grades})
scores


# In[35]:


# bins and their mappings to letter grades
score_bins =    [ 0,  59,   62,  66,   69,   72,  76,   79,   82,  
                 86,   89,   92,  99, 100]
letter_grades = ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 
                 'B+', 'A-', 'A', 'A+']


# In[36]:


# cut based upon the bins and assign the letter grade
letter_cats = pd.cut(scores.Grade, score_bins, labels=letter_grades)
scores['Letter'] = letter_cats
scores


# In[37]:


# examine the underlying categorical
letter_cats


# In[38]:


# how many of each grade occurred?
scores.Letter.value_counts()


# In[39]:


# and sort by letter grade instead of numeric grade
scores.sort_values(by=['Letter'], ascending=False)

