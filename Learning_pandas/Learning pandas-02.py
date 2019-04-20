
# coding: utf-8

# # Installing pandas

# In[ ]:


We will cover the following topics in this chapter:
• Getting Anaconda (and pandas)
• Installing Anaconda on Linux, Mac, and Windows
• Verifying the version of pandas
• Updating the pandas packages within Anaconda with conda
• Running a small pandas sample in IPython
• Starting the IPython Notebook server
• Installing and running the workbooks for the textbook
• Using Wakari for pandas


# In[7]:


import pandas as pd

pd.__version__   #'0.23.4'

df = pd.DataFrame(['column1', [1, 2, 3]])
print (df)


# In[ ]:


<shifr>+<enter>  运行当前栏的代码


# ### Using Wakari for pandas

# In[ ]:



Another option for learning pandas and running the examples in this book is to utilize
the Wakari web-based Python Data Analysis platform. This service is freemium and
it only takes a few minutes to create an account. All the examples in this book can be
run with a free account. Wakari is available at https://wakari.io/.

