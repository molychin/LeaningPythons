# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 15:40:41 2019

@author: Administrator
Learning pandas-Michael Heydt BIRMINGHAM-2017版
"""

#Representing Univariate Data with the Series
#用序列表示单变量数据

The Series is the primary building block of pandas. It represents a one-dimensional array-like set of values
of a single data type. It is often used to model zero or more measurements of a single variable. While it
can appear like an array, a Series has an associated index that can be used to perform very efficient
retrievals of values based upon labels.
A Series also performs automatic alignment of data between itself and other pandas objects. Alignment is a
core feature of pandas where data is multiple pandas objects that are matched by label value before any
operation is performed. This allows the simple application of operations without needing to explicitly
code joins.
In this chapter, we will examine how to model measurements of a variable using a Series, including using
an index to retrieve samples. This examination will include overviews of several patterns involved in
index labeling, slicing and querying data, alignment, and re-indexing data.
Specifically, in this chapter we will cover the following topics:
Creating a series using Python lists, dictionaries, NumPy functions, and scalar values
Accessing the index and values properties of the Series
Determining the size and shape of a Series object
Specifying an index at the time of Series creation
Using heads, tails, and takes to access values
Value lookup by index label and position
Slicing and common slicing patterns
Alignment via index labels
Performing Boolean selection
Re-indexing a Series
In-place modification of values

























