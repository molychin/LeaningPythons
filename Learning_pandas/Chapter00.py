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

So, let's jump in In this chapter, we will cover:
●What pandas is, why it was created, and what it gives you
●How pandas relates to data analysis and data science
●The processes involved in data analysis and how it is supported by pandas
●General concepts of data and analytics
●Basic concepts of data analysis and statistical analysis
●Types of data and their applicability to pandas
●Other libraries in the Python ecosystem that you will likely use with pandas
所以，让我们跳进去。在本章中，我们将介绍：
●熊猫是什么，它为什么被创造出来，它给了你什么
●大熊猫与数据分析和数据科学的关系
●数据分析所涉及的过程以及熊猫如何支持数据分析
●数据和分析的一般概念
●数据分析和统计分析的基本概念
●数据类型及其对大熊猫的适用性
●python生态系统中可能与熊猫一起使用的其他库

pandas is a Python library containing high-level data structures and tools that have been created to help
Python programmers to perform powerful data analysis. 
PANDAS是一个包含高级数据结构和工具的python库，创建这些结构和工具是为了帮助python程序员执行强大的数据分析。

To do this processing, a tool was needed that allows us to retrieve, index, clean and tidy, reshape,
combine, slice, and perform various analyses on both single- and multidimensional data, including
heterogeneous-typed【混合类型】 data that is automatically aligned along a set of common index labels. This is where
pandas comes in, having been created with many useful and powerful features such as the following:
要进行这种处理，需要一种工具，允许我们检索、索引、清理和整理、重塑、组合、切片和对一维和多维数据执行各种分析，
包括异构类型的【混合类型】数据，这些数据会自动沿一组公共索引标签对齐。熊猫就是在这里诞生的，它们具有许多有用和强大的特征，如：
●Fast and efficient Series and DataFrame objects for data manipulation with integrated indexing
●Intelligent data alignment using indexes and labels
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
●Hierarchical indexing facilitating working with high-dimensional data in a lower-dimensional data structure
●Extensive features for time series data, including date range generation and frequency conversion,
moving window statistics, moving window linear regressions, date shifting, and lagging
●Highly optimized for performance, with critical code paths written in Cython or C
●快速高效的数据操作系列和数据帧对象，集成索引智能数据对齐
●使用索引和标签的智能数据对齐
●对丢失数据的综合处理
●将杂乱数据转换为有序数据的设施（整理）
●用于在内存数据结构和文件、数据库和Web服务之间读取和写入数据的内置工具
●能够处理存储在许多常用格式（如csv、excel、hdf5和json）中的数据
●数据集的灵活重塑和旋转
●基于智能标签的切片、花式索引和大型数据集子集
●可以从数据结构中插入和删除列，以实现大小的可变性。
●使用强大的数据分组功能聚合或转换数据，以便对数据集执行拆分应用程序组合
●数据集的高性能合并和连接
●分层索引，便于在低维数据结构中处理高维数据
●时间序列数据的广泛功能，包括日期范围生成和频率转换、移动窗口统计、移动窗口线性回归、日期移动和滞后
●高度优化性能，关键代码路径用cython或c编写

Logically, the overall process can be broken into three major areas of discipline:
从逻辑上讲，整个过程可以分为三个主要领域：
●Data manipulation  数据处理
●Data analysis    数据分析
●Data science    数据科学

■Data manipulation  数据处理
This requires many different tasks and capabilities from a tool that
manipulates data in preparation for analysis. The features needed from such a tool include:
这需要一个工具提供许多不同的任务和功能，该工具可以操作数据，为分析做准备。这种工具所需的特性包括：
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
●Application of functions to calculate meaning or perform transformations 应用函数计算意义或执行转换
●Query and slicing to explore pieces of the whole 为探索整体而查询和切片
●Restructuring into other forms 重构数据形式
●Modeling distinct categories of data such as categorical, continuous, discrete, and time series
为不同类别的数据建模，如分类、连续、离散和时间序列
●Resampling data to different frequencies 将数据重新采样到不同的频率


脏数据（Dirty Read）是指源系统中的数据不在给定的范围内或对于实际业务毫无意义，或是数据格式非法，
以及在源系统中存在不规范的编码和含糊的业务逻辑。
通俗的讲，当一个事务正在访问数据，并且对数据进行了修改，而这种修改还没有提交到数据库中，这时，
另外一个事务也访问这个数据，然后使用了这个数据。因为这个数据是还没有提交的数据，那么另外一个
事务读到的这个数据是脏数据，依据脏数据所做的操作可能是不正确的。

■Data analysis 数据分析
Data analysis is the process of creating meaning from data. Data with quantified meaning is often called
information. Data analysis is the process of creating information from data through the creation of data
models and mathematics to find patterns. It often overlaps【重叠】 data manipulation and the distinction between
the two is not always clear. Many data manipulation tools also contain analyses functions, and data
analysis tools often provide data manipulation capabilities.
数据分析是从数据中创造意义的过程。具有量化意义的数据通常称为信息。数据分析是从数据中创建信息的过程，
通过创建数据模型和数学来寻找模式。它经常与数据操作重叠，两者之间的区别并不总是很清楚。
许多数据操作工具还包含分析功能，数据分析工具通常提供数据操作功能。

数据分析是赋予数据意义的过程。数据的定性分形往往意味着（产生）信息。

■Data science  数据科学
Data science is the process of using statistics and data analysis processes to create an understanding of
phenomena within data. Data science usually starts with information and applies a more complex
domain-based analysis to the information. These domains span many fields such as mathematics,
statistics, information science, computer science, machine learning, classification, cluster analysis, data
mining, databases, and visualization. Data science is multidisciplinary【多学科】. 
Its methods of domain analysis are often very different and specific to a specific domain.
数据科学是利用统计和数据分析过程来理解数据中的现象的过程。数据科学通常从信息开始，并对信息应用更复杂的基于领域的分析。
这些领域涉及许多领域，如数学、统计学、信息科学、计算机科学、机器学习、分类、聚类分析、数据挖掘、数据库和可视化。
数据科学是多学科的。它的领域分析方法通常非常不同，并且针对特定的领域。

■The process of data analysis  数据分析过程

One description of the steps involved in the process of data analysis is given on the pandas web site:
熊猫网站上提供了数据分析过程中涉及的步骤说明：
●Munging and cleaning data  挖掘和清理数据
●Analyzing/modeling  分析与建模
●Organization into a form suitable for communication  组织适合的形式便于交流

This process sets up a framework for defining logical steps that are taken in working with data. For now,
let's take a quick look at each of these steps in the process and some of the tasks that you as a data analyst
using pandas will perform.
It is important to understand that this is not purely a linear process. It is best done in a
highly interactive and agile/iterative manner.
这个过程建立了一个框架，用于定义在处理数据时所采取的逻辑步骤。现在，让我们快速了解过程中的每个步骤，
以及作为使用熊猫的数据分析师将执行的一些任务。
重要的是要理解这不是一个纯粹的线性过程。最好以高度交互和敏捷/迭代的方式完成。

■The Data Process 数据过程

• Ideation 构思能力/思考问题/提出问题（以期找到合理的模式假设去运用于有效/灵活/科学的决策）
The first step in any data problem is to identify what it is you want to figure out. 
Ideation generally relates to hypothesizing about patterns in data that can 
be used to make intelligent decisions.
任何数据问题的第一步都是确定您想要找出什么。意念通常与数据模式的假设有关，数据模式可用于做出明智的决策。

【寻找问题】
But what kinds of decision are we typically looking to make? The following are 
several questions for which answers are commonly asked:
但我们通常希望做出什么样的决定？以下是几个常见问题的答案：
○ Why did something happen?  事情为什么会发生
○ Can we predict the future using historical data? 是否可以利用历史数据来预见/预测未来
○ How can I optimize operations in the future?  怎样可以在以后优化操作

This list is by no means exhaustive, but it does cover a sizable percentage of the reasons why anyone
undertakes these endeavors. To get answers to these questions, one must be involved with collecting and
understanding data relative to the problem. This involves defining what data is going to be researched,
what the benefit is of the research, how the data is going to be obtained, what the success criteria are, and
how the information is going to be eventually communicated.
这份清单决不是详尽的，但它确实涵盖了相当大比例的理由，任何人进行这些努力。要得到这些问题的答案，
必须收集和理解与问题相关的数据。这涉及到定义将要研究的数据、研究的好处、数据将如何获得、成功标准是什么，
以及最终如何传达信息。

	
pandas itself does not provide tools to assist in ideation. But once you have gained 
understanding and skill in using pandas, you will naturally realize how pandas 
will help you in being able to formulate ideas. This is because you will be armed 
with a powerful tool you can used to frame many complicated hypotheses.
熊猫本身不提供帮助构思的工具。但是一旦你在使用熊猫方面获得了理解和技能，你就会自然地意识到熊猫是
如何帮助你形成想法的。这是因为你将拥有一个强大的工具，你可以用来构建许多复杂的假设。	

• Retrieval 检索/获取数据
Once you have an idea you must then find data to try and support your hypothesis. 
【生肉（未经处理过的源数据），不能直接用于数据分析，这样会消化不良或拉肚子。生肉意味着非组织的，
有各种格式，包含错误数据，还需要手工处理。】
Data is often very raw, even if obtained from data sources that you have created or 
from within your  organization. Being raw means that the data can be disorganized,
may be in various formats, and erroneous; relative to supporting your analysis, 
it may be incomplete and need manual augmentation.
数据通常是非常原始的，即使是从您创建的数据源或从组织内部获得的。原始数据意味着数据可能是无序的，
可能是各种格式的，并且是错误的；相对于支持您的分析而言，它可能是不完整的，需要手动扩充。

In either case, pandas provides a robust and easy-to-use set of tools for retrieving 
data from various sources and that may be in many different formats. 
pandas also gives us the ability to not only retrieve data, but to also provide an 
initial structuring of the data via pandas data structures without needing to 
manually create complex coding, which may be required in other tools or programming languages.
在这两种情况下，熊猫都提供了一套强大且易于使用的工具，用于从各种来源检索数据，这些工具可能采用多种不同的格式。
熊猫还使我们不仅能够检索数据，而且能够通过熊猫数据结构提供数据的初始结构，而无需手动创建复杂的编码，
这可能是其他工具或编程语言所需要的。	
	
• Preparation 准备
During preparation, raw data is made ready for exploration. This preparation is often a very interesting
process. It is very frequently the case that data from is fraught with all kinds of issues related to quality.
You will likely spend a lot of time dealing with these quality issues, and often this is a very non-trivial
amount of time.
在准备过程中，原始数据准备好进行勘探。这个准备过程通常是一个非常有趣的过程。通常情况下，来自的数据充满了与质量相关的各种问题。
您可能会花费大量时间处理这些质量问题，而且通常这是非常重要的时间量。

Well there are a number of reasons:
○ The data is simply incorrect
○ Parts of the dataset are missing
○ Data is not represented using measurements appropriate for your analysis
○ The data is in formats not convenient for your analysis
○ Data is at a level of detail not appropriate for your analysis
○ Not all the fields you need are available from a single source
○ The representation of data differs depending upon the provider
原因有很多：
○数据完全不正确
○部分数据集丢失
○没有使用适合您分析的测量值来表示数据
○数据格式不便于分析
○数据的详细程度不适合您的分析
○并非所有需要的字段都可以从单一来源获得
○数据的表示方式因供应商而异


The preparation process focuses on solving these issues. pandas provides many great 
facilities for preparing data, often referred to as tidying up data. 
These facilities include intelligent means of handling missing data, converting data types, 
using format conversion, changing frequencies of measurements,joining data from 
multiple sets of data, mapping/converting symbols into shared representations, 
and grouping data, among many others. 
准备过程的重点是解决这些问题。pandas为准备数据提供了许多很好的设施，通常被称为整理数据。
这些设施包括处理丢失数据的智能方法、转换数据类型、使用格式转换、更改测量频率，连接多组数据中的数据，
将符号映射/转换为共享表示，以及对数据进行分组等。

• Exploration 探索
Exploration involves being able to interactively slice and dice your data to try and make quick discoveries. 
探索包括能够交互地对数据进行切片和骰子，以尝试快速发现。
Exploration can include various tasks such as: 包含如下方法:
○ Examining how variables relate to each other  检查和其他数据的相关性
○ Determining how the data is distributed  决定是否发布数据
○ Finding and excluding outliers    查找和排除异常值
○ Creating quick visualizations  建立快速可视化
○ Quickly creating new data representations or models to feed into more permanent and detailed
快速创建新的数据表示或模型，以提供更持久和更详细的信息
○ modeling processes  建模过程

The expressiveness of the syntax of pandas lets you describe complex data manipulation 
constructs succinctly, and the result of every action you take upon your data is immediately 
presented for your inspection. This allows you to quickly determine the validity of 
the action you just took without having to recompile and completely rerun your programs.
pandas语法的表达性使您能够简洁地描述复杂的数据操作结构，并且您对数据采取的每个操作的结果都会
立即呈现给您进行检查。这允许您快速确定刚执行的操作的有效性，而无需重新编译和完全重新运行程序。


• Modeling 建模
The modeling process is iterative where, through an exploration of the data, 
you select the variables required to support your analysis, organize the variables 
for input to analytical processes, execute the model, and determine how well 
the model supports your original assumptions. It can include a formal modeling 
of the structure of the data, but can also combine techniques from various 
analytic domains such as (and not limited to) statistics, machine learning, 
and operations research.
建模过程是迭代的，通过对数据的研究，您可以选择支持分析所需的变量，组织变量以输入到分析过程，
执行模型，并确定模型对原始假设的支持程度。它可以包括对数据结构的正式建模，也可以结合各种分析
领域的技术，例如（但不限于）统计、机器学习和运筹学。

To facilitate this, pandas provides extensive data modeling facilities. It is in this step that you will move
more from exploring your data, to formalizing the data model in DataFrame objects, and ensuring the
processes to create these models are succinct. Additionally, by being based in Python, you get to use its
full power to create programs to automate the process from beginning to end. The models you create are
executable.
为了方便这一点，熊猫提供了广泛的数据建模设施。在这一步中，您将从探索数据到在数据框架对象中形式化数据模型，
并确保创建这些模型的过程是简洁的。另外，通过在python中的基础，您可以使用它的全部能力来创建程序，
从而从头到尾实现流程自动化。您创建的模型是可执行的。

• Presentation 表达
The penultimate step of the process is presenting your findings to others, 
typically in the form of a report or presentation. You will want to create a 
persuasive and thorough explanation of your solution. This can often be done 
using various plotting tools in Python and manually creating a presentation.
Jupyter notebooks are a powerful tool in creating presentations for your analyses with pandas. 
These notebooks provide a means of both executing code and providing rich markdown 
capabilities to annotate and describe the execution at multiple points in the application. 
These can be used to create very effective, executable presentations that are 
visually rich with pieces of code, stylized text, and graphics.
这个过程的倒数第二步是向他人展示你的发现，通常是以报告或陈述的形式。你需要对你的解决方案做出一个
有说服力的、彻底的解释。这通常可以使用Python中的各种绘图工具并手动创建演示文稿来完成。
Jupyter笔记本是为您的熊猫分析创建演示文稿的强大工具。这些笔记本提供了一种同时执行代码和提供丰富的标记功能的方法，
可以在应用程序的多个点上对执行进行注释和描述。这些可以用来创建非常有效的、可执行的表示，这些表示
在视觉上丰富了代码片段、样式化文本和图形。


• Reproduction 再现/分享
An important piece of research is sharing and making your research reproducible. 
It is often said that if other researchers cannot reproduce your experiment and 
results, then you didn't prove a thing.
Fortunately, for you, by having used pandas and Python, you will be able to easily 
make your analysis reproducible. This can be done by sharing the Python code that 
drives your pandas code, as well as the data.
Jupyter notebooks also provide a convenient means of packaging both the code and 
application in a means that can be easily shared with anyone else with a Jupyter 
Notebook installation. And there are many free, and secure, sharing sites on the 
internet that allow you to either create or deploy your Jupyter notebooks for sharing.
一项重要的研究是分享并使你的研究具有可复制性。人们常说，如果其他研究人员不能复制你的实验和结果，那么你就没有证明什么。
幸运的是，对于您来说，通过使用panda和python，您将能够轻松地使您的分析具有可复制性。这可以通过共享
驱动熊猫代码的python代码以及数据来实现。
Jupyter笔记本电脑还提供了一种方便的方法，将代码和应用程序打包在一种可以通过Jupyter笔记本安装
轻松与任何其他人共享的方法中。互联网上有许多免费、安全的共享站点，允许您创建或部署Jupyter笔记本进行共享。


A note on being iterative and agile
Something very important to understand about data manipulation, analysis, and science is that it is an
iterative process. Although there is a natural forward flow along the stages previously discussed, you will
end up going forwards and backwards in the process. For instance, while in the exploration phase you
may identify anomalies in the data that relate to data purity issues from the preparation stage, and need to
go back and rectify those issues.
This is part of the fun of the process. You are on an adventure to solve your initial problem, all the while
gaining incremental insights about the data you are working with. These insights may lead you to ask new
questions, to more exact questions, or to a realization that your initial questions were not the actual
questions that needed to be asked. The process is truly a journey and not necessarily the destination.
关于迭代和敏捷的注记
了解数据操作、分析和科学的一些非常重要的事情是，它是一个迭代过程。虽然在前面讨论的阶段中有一个自然的前进流，
但是您最终将在这个过程中前进和后退。例如，在勘探阶段，您可以识别与准备阶段的数据纯度问题相关的数据中的异常，
并需要返回并纠正这些问题。
这是这个过程的一部分乐趣。您正在冒险解决您的初始问题，同时获得有关您正在使用的数据的增量洞察。
这些见解可能会引导你提出新的问题，更确切的问题，或者意识到你最初的问题不是需要问的实际问题。
这个过程真的是一次旅行，不一定是目的地。


■Concepts of data and analysis in our tour of pandas
大熊猫旅游中的数据与分析概念

Types of data
Working with data in the wild you will come across several broad categories of data that will need to be
coerced into pandas data structures. They are important to understand as the tools required to work with
each type vary.
数据类型
在野外处理数据时，您将遇到几个需要强制转换成熊猫数据结构的广泛数据类别。理解它们很重要，因为使用每种类型所需的工具各不相同。

Structured
Structured data is any type of data that is organized as fixed fields within a record or file, such as data in
relational databases and spreadsheets. Structured data depends upon a data model, which is the defined
organization and meaning of the data and often how the data should be processed. This includes
specifying the type of the data (integer, float, string, and so on), and any restrictions on the data, such as
the number of characters, maximum and minimum values, or a restriction to a certain set of values.
结构化的数据
结构化数据是记录或文件中组织为固定字段的任何类型的数据，例如关系数据库和电子表格中的数据。结构化数据依赖于
一个数据模型，它是数据的定义组织和含义，并且通常是处理数据的方式。这包括指定数据的类型（整数、浮点、字符串等），
以及对数据的任何限制，例如字符数、最大值和最小值，或者对一组特定值的限制。

Unstructured
Unstructured data is data that is without any defined organization and which specifically does not break
down into stringently defined columns of specific types. This can consist of many types of information
such as photos and graphic images, videos, streaming sensor data, web pages, PDF files, PowerPoint
presentations, emails, blog entries, wikis, and word processing documents.
非结构化的数据
非结构化数据是指没有任何定义的组织的数据，具体来说，这些数据不会分解为特定类型的严格定义的列。
这可以包含许多类型的信息，如照片和图形图像、视频、流传感器数据、网页、PDF文件、PowerPoint演示文稿、
电子邮件、博客条目、维基和文字处理文档。

Semi-structured
Semi-structured data fits in between unstructured. It can be considered a type of structured data, but lacks
the strict data model structure. JSON is a form of semi-structured data. While good JSON will have a
defined format, there is no specific schema for data that is always strictly enforced. Much of the time, the
data will be in a repeatable pattern that can be easily converted into structured data types like the pandas
DataFrame, but the process may need some guidance from you to specify or coerce data types.
半结构化数据
半结构化数据介于非结构化数据之间。它可以被视为一种结构化数据，但缺乏严格的数据模型结构。JSON是半结构化数据的一种形式。
虽然好的JSON将有一个定义好的格式，但是对于总是严格执行的数据，没有特定的模式。在大多数情况下，数据将以可重复的模式出现，
可以很容易地转换为结构化数据类型，如熊猫数据帧，但该过程可能需要您提供一些指导，以指定或强制数据类型。







'''










