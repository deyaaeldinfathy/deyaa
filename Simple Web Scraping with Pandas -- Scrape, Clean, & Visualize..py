#!/usr/bin/env python
# coding: utf-8

# # Web Scraping for Game of Thrones Data

# Load in Pands and scrape the data from Wikipedia and creat concatenated dataframe

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_html('https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes')[0]
df


# In[3]:


append_data=[]
for i in range(1,9):
    append_data.append(pd.read_html('https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes')[i])


# In[4]:


df=pd.concat(append_data)


# In[5]:


df.head()


# In[6]:


print(df['U.S. viewers(millions)'])


# In[7]:


df['U.S. viewers(millions)'] = [x[ :4] for x in df['U.S. viewers(millions)']]
df['U.S. viewers(millions)']=pd.to_numeric(df['U.S. viewers(millions)'])


# In[8]:


df.head()


# # Creat an Interactive Visual for Episodes Popularity Overall and Per Season

# Use Plotly to create an interactive visual

# In[9]:


import plotly.express as go


# In[10]:


go.bar(df,x='No.overall', y='U.S. viewers(millions)')


# In[11]:


group=df.groupby('No. inseason', as_index=False)['U.S. viewers(millions)'].mean()
go.bar(group,x='No. inseason', y='U.S. viewers(millions)')


# In[ ]:





# In[ ]:




