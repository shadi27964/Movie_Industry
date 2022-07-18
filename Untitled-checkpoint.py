#!/usr/bin/env python
# coding: utf-8

# In[26]:


# importing the libs
#a popular Python-based data analysis toolkit
import pandas as pd

#Numerical Python, a scientific computing library 
import numpy as np

#data visualization library 
import seaborn as sns

#Pyplot is a state-based interface to a Matplotlib module which provides a MATLAB-like interface
import matplotlib.pyplot as plt

#mlab. Numerical python functions written for compatability with MATLAB commands 
import matplotlib.mlab as mlab

#data visualization and graphical plotting
import matplotlib

#express is an interface to Plotly, which operates on a variety of types of 
#data and produces easy-to-style figures
import plotly.express as px

#ggplot (a popular plotting package for R).
plt.style.use('ggplot')

#figure() Function in pyplot module of matplotlib library is used to create a new figure
from matplotlib.pyplot import figure

#magic function %matplotlib inline enable the inline plotting, where the plots/graphs
#will be displayed just below the cell where your plotting commands are written
get_ipython().run_line_magic('matplotlib', 'inline')

#rcParams contains some properties in matplotlibrc file. it control the defaults of almost every property 
#in Matplotlib: figure size and DPI, line width, color and style, axes, axis and grid properties, 
#text and font properties and so on.
matplotlib.rcParams['figure.figsize'] = (12,8)

#You can change the behaviour of SettingWithCopyWarning warning using pd.options.mode.chained_assignment 
#with three option "raise"/"warn"/None
pd.options.mode.chained_assignment = None


# In[27]:


# load the data and take a look at the data
df = pd.read_csv('movies.csv')
df


# In[12]:


# Data Types for our columns
print(df.dtypes)


# In[13]:


# Checking for missing data
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())
    print('{} - {}%'.format(col, round(pct_missing*100)))


# In[14]:


#Let's summerize our missing values
print (df.isnull().sum())


# In[28]:


#Droping missing values
df = df.dropna()


# In[29]:


# Change column data type. Getting rid of decimal
df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')
df.head(5)


# In[30]:


#a new column
df['yearcorrect'] = df['released'].astype(str).str.extract(pat = '([0-9]{4})')
df.head(5)


# 

# In[31]:


#sorting the gross column in descending order
df.sort_values(by=['gross'], inplace=False, ascending=False)


# In[ ]:


#Checking all the dataset
pd.set_option(display,'max_rows', None)


# In[32]:


#Checking duplicates in Company
df['company'].drop_duplicates().sort_values(ascending=False)


# In[33]:


# Checking Outliers in gross column
df.boxplot(column=['gross'])


# In[39]:


#scatter plot with budget vs gross

fig = px.scatter(df
           ,x = 'budget'
           ,y = 'gross'
           ,color = 'gross',size='budget', hover_data=['gross'], trendline="ols"
           ,title = 'Budget vs Gross Earnings'
           ,labels={
                     "gross": "Gross Earnings",
                     "budget": "Budget For Film"})
fig.update_layout(
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
)

fig.show()


# In[40]:


#checking correlation matrix between numeric columns
df.corr(method ='pearson')


# In[41]:


df.corr(method ='kendall')


# In[42]:


df.corr(method ='spearman')


# In[50]:


#heatmap visualization of Pearson matrix method
correlation_matrix = df.corr(method ='pearson')
fig = px.imshow(correlation_matrix, color_continuous_scale='hot', title='Pearson Matrix Method HeatMap'
                , width=800, height=700, aspect='equal',text_auto=True)
fig.show()


# In[51]:


df_numerized = df
for col_name in df_numerized.columns:
    if(df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] = df_numerized[col_name].astype('category')
        df_numerized[col_name] = df_numerized[col_name].cat.codes
df_numerized


# In[59]:


correlation_matrix = df_numerized.corr(method ='pearson')
fig = px.imshow(correlation_matrix, color_continuous_scale='hot', title='Pearson Matrix Method HeatMap'
                , width=1000, height=800, aspect='equal',text_auto=True)
fig.show()


# In[60]:


#Simplify above visualization
df_numerized.corr()


# In[63]:


#Let's organize above table
correlation_mat = df_numerized.corr()
corr_pairs = correlation_mat.unstack()
corr_pairs


# In[64]:


sorted_pairs = corr_pairs.sort_values()
print(sorted_pairs)


# In[65]:


# We can now take a look at the ones that have a high correlation (> 0.5)
strong_pairs = sorted_pairs[(sorted_pairs) > 0.5]
print(strong_pairs)


# In[66]:


#scatter plot with votes vs gross

fig = px.scatter(df
           ,x = 'votes'
           ,y = 'gross'
           ,color = 'gross',size='votes', hover_data=['gross'], trendline="ols"
           ,title = 'Votes vs Gross Earnings'
           ,labels={
                     "gross": "Gross Earnings",
                     "votes": "Votes For Film"})
fig.update_layout(
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
)

fig.show()


# In[ ]:


#Votes and Budget have the highest correlation to earning.
#Company has the lowest correlation.

