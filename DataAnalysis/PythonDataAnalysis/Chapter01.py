# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:29:50 2019

@author: Administrator
"""

#Python Data Analysis
#Learn how to apply powerful data analysis techniques
#with popular open source Python modules
#Ivan Idris



#from pandas import Series
import pandas as pd

data1={'state':['0hio','0hio','0hio','Nevada','Nevada'],
  'year':[2000,2001,2002,2001,2002],
  'pop':[1.5,1.7,3.6,2.4,2.9]}
#dataFrame1=pd.DataFrame(data1)
dataFrame11=pd.DataFrame(data1,columns=['year','state','pop'],index=['one','two','three','four','five'])
print (dataFrame11)
print ("-----------------")
print(dataFrame11['state'])
print ("-----------------")
print(dataFrame11.year)
print ("-----------------")
#print(dataFrame11.ix['three'])
print(dataFrame11.loc['three'])

objS_1=pd.Series([4,7,-5,3])
print (objS_1,objS_1.values,objS_1.index)

objS_2=pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(objS_2)
objS_2['d']=6
print('\n\n',objS_2['a'])
print(objS_2[['c','a','d']])