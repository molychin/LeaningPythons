# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:28:52 2019
@author: Administrator
"""

# coding: utf-8
# # Learning pandas
#High-performance data manipulation and analysis in Python
#Michael Heydt

'''
Chapter 1 , pandas and Data Analysis, is a hands-on introduction to the key features of pandas. 
The idea of this chapter is to provide some context for using pandas in the context of statistics 
and data science. The chapter will get into several concepts in data science and show how they are 
supported by pandas. This will set a context for each of the subsequent chapters, mentioning each 
chapter relates to both data science and data science processes.
第一章，大熊猫与数据分析，是对大熊猫主要特征的亲身介绍。本章的目的是为在统计和数据科学的背景下使用熊猫提供一些背景。
本章将探讨数据科学中的几个概念，并说明熊猫是如何支持它们的。这将为后面的每一章设置一个上下文，
每一章都涉及到数据科学和数据科学过程。

Pandas is a popular Python package used for practical, real-world data analysis. 
It provides efficient,fast, and high-performance data structures that make data exploration and analysis very easy. 
Thislearner's guide will help you through a comprehensive set of features provided by the pandas library to perform 
efficient data manipulation and analysis.
熊猫是一个流行的python包，用于实际的、真实的数据分析。它提供了高效、快速和高性能的数据结构，使数据勘探和分析非常容易。
本学习指南将帮助您通过熊猫图书馆提供的一套综合功能来执行高效的数据操作和分析。

Who this book is for
This book is ideal for data scientists, data analysts, and Python programmers who want to plunge into data
analysis using pandas, and anyone curious about analyzing data. Some knowledge of statistics and
programming will help you to get the most out of this book but that's not strictly required. Prior exposure
to pandas is also not required.
这本书是给谁的
这本书非常适合数据科学家、数据分析师和希望使用熊猫进行数据分析的Python程序员，以及任何对分析数据感兴趣的人。
统计和编程方面的一些知识将帮助您从本书中获得最大的收获，但这并不是严格要求的。也不需要事先接触大熊猫。

So, let's jump in. In this chapter, we will cover:
●What pandas is, why it was created, and what it gives you
●How pandas relates to data analysis and data science
●The processes involved in data analysis and how it is supported by pandas
●General concepts of data and analytics
●Basic concepts of data analysis and statistical analysis
●Types of data and their applicability to pandas
●Other libraries in the Python ecosystem that you will likely use with pandas
所以，让我们跳进去。在本章中，我们将介绍：
熊猫是什么，它为什么被创造出来，它给了你什么
大熊猫与数据分析和数据科学的关系
数据分析所涉及的过程以及熊猫如何支持数据分析
数据和分析的一般概念
数据分析和统计分析的基本概念
数据类型及其对大熊猫的适用性
python生态系统中可能与熊猫一起使用的其他库

pandas is a Python library containing high-level data structures and tools that have been created to help
Python programmers to perform powerful data analysis. 

To do this processing, a tool was needed that allows us to retrieve, index, clean and tidy, reshape,
combine, slice, and perform various analyses on both single- and multidimensional data, including
heterogeneous-typed【混合类型】 data that is automatically aligned along a set of common index labels. This is where
pandas comes in, having been created with many useful and powerful features such as the following:
●Fast and efficient Series and DataFrame objects for data manipulation with integrated indexing
Intelligent data alignment using indexes and labels
●Integrated handling of missing data
●Facilities for converting messy data into orderly data (tidying)
●Built-in tools for reading and writing data between in-memory data structures and files, databases,
and web services
●The ability to process data stored in many common formats such as CSV, Excel, HDF5, and JSON
●Flexible reshaping and pivoting of sets of data
●Smart label-based slicing, fancy indexing, and subsetting of large datasets
●Columns can be inserted and deleted from data structures for size mutability
●Aggregating or transforming data with a powerful data grouping facility to perform split-applycombine on datasets
●High-performance merging and joining of datasets
●Hierarchical indexing facilitating working with high-dimensional data in a lower-dimensional data
structure
●Extensive features for time series data, including date range generation and frequency conversion,
moving window statistics, moving window linear regressions, date shifting, and lagging
●Highly optimized for performance, with critical code paths written in Cython or C

Logically, the overall process can be broken into three major areas of discipline:
●Data manipulation  数据处理
●Data analysis    数据分析
●Data science    数据科学

■数据处理
This requires many different tasks and capabilities from a tool that
manipulates data in preparation for analysis. The features needed from such a tool include:
●Programmability for reuse and sharing  可编程的重用和共享
●Access to data from external sources   访问外部数据来源
●Storing data locally  存储本地数据
●Indexing data for efficient retrieval  对有效检索建立索引数据
●Alignment of data in different sets based upon attributes  基于不用基础属性排列数据
●Combining data in different sets  合并不同集合的数据
●Transformation of data into other representations 转换数据为其他表现形式
●Cleaning data from cruft  清除脏数据
●Effective handling of bad data  有能力处理坏数据
●Grouping data into common baskets  集群同类数据
●Aggregation of data of like characteristics  依据性质分类数据
●Application of functions to calculate meaning or perform transformations
●Query and slicing to explore pieces of the whole 为探索整体而查询和切片
●Restructuring into other forms 重构数据形式
●Modeling distinct categories of data such as categorical, continuous, discrete, and time series
●Resampling data to different frequencies 


脏数据（Dirty Read）是指源系统中的数据不在给定的范围内或对于实际业务毫无意义，或是数据格式非法，
以及在源系统中存在不规范的编码和含糊的业务逻辑。
通俗的讲，当一个事务正在访问数据，并且对数据进行了修改，而这种修改还没有提交到数据库中，这时，
另外一个事务也访问这个数据，然后使用了这个数据。因为这个数据是还没有提交的数据，那么另外一个
事务读到的这个数据是脏数据，依据脏数据所做的操作可能是不正确的。

■Data analysis
Data analysis is the process of creating meaning from data. Data with quantified meaning is often called
information. Data analysis is the process of creating information from data through the creation of data
models and mathematics to find patterns. It often overlaps【重叠】 data manipulation and the distinction between
the two is not always clear. Many data manipulation tools also contain analyses functions, and data
analysis tools often provide data manipulation capabilities.Data science


数据分析是赋予数据意义的过程。数据的定性分形往往意味着（产生）信息。
■Data science
Data science is the process of using statistics and data analysis processes to create an understanding of
phenomena within data. Data science usually starts with information and applies a more complex
domain-based analysis to the information. These domains span many fields such as mathematics,
statistics, information science, computer science, machine learning, classification, cluster analysis, data
mining, databases, and visualization. Data science is multidisciplinary【多学科】. Its methods of domain analysis are
often very different and specific to a specific domain.

The process of data analysis

One description of the steps involved in the process of data analysis is given on the pandas web site:
●Munging and cleaning data  挖掘和清理数据
●Analyzing/modeling  分形与建模
●Organization into a form suitable for communication  组织适合的形式便于交流
'''
import numpy as np
import pandas as pd

s1=pd.Series([2,5,7,9,np.nan])   #加入np.nan后，整数自动转化为浮点数
print(s1[[1,3]])

#A Series object can be created with a user-defined index by specifying the labels for
#the index using the index parameter.
s2=pd.Series([34,44,2,65],index=['a','d','e','伤害'])
print(s2)



