#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# In[2]:


df=pd.read_csv("C:/Users/deyaa.elden/Desktop/Paython Course/Projects/Mall_Customers.csv")


# In[3]:


df.head()


# # Univariate analysis

# In[4]:


df.describe()


# In[5]:


sns.distplot(df['Annual Income (k$)']);


# In[6]:


columns=['Age','Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.distplot(df[i])


# In[7]:


sns.kdeplot(data= df ,x='Annual Income (k$)',shade=True,hue ='Gender')


# In[8]:


columns=['Age','Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.kdeplot(data= df ,x=i,shade=True,hue ='Gender')


# In[9]:


columns=['Age','Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.boxplot(data= df ,x='Gender',y=i )


# In[10]:


df['Gender'].value_counts(normalize=True)


# # Bivariate Analysis

# In[11]:


sns.scatterplot(data=df, x='Annual Income (k$)',y='Spending Score (1-100)')


# In[12]:


df=df.drop('CustomerID',axis=1)
sns.pairplot(df)


# In[13]:


df.groupby(['Gender'])['Age','Annual Income (k$)','Spending Score (1-100)'].mean()


# In[14]:


df.corr()


# In[15]:


sns.heatmap(df.corr(),annot=True,cmap='coolwarm')


# # Clustring Univariate, Bivariate and Multivariate.

# In[27]:


clustring1=KMeans(n_clusters=3)


# In[28]:


clustring1.fit(df[['Annual Income (k$)']])


# In[29]:


clustring1.labels_


# In[30]:


df['income cluster']=clustring1.labels_
df.head()


# In[31]:


df['income cluster'].value_counts


# In[32]:


clustring1.inertia_


# In[33]:


inertia_scores=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df[['Annual Income (k$)']])
    inertia_scores.append(kmeans.inertia_)


# In[34]:


inertia_scores


# In[26]:


plt.plot(range(1,11),inertia_scores)


# In[40]:


df.columns


# In[42]:


df.groupby('income cluster')['Age', 'Annual Income (k$)', 'Spending Score (1-100)'].mean()


# # Bivariate Clustering

# In[49]:


clustering2=KMeans(n_clusters=5)
clustering2.fit(df[['Annual Income (k$)', 'Spending Score (1-100)']])
df['Spending and Income Clustering']=clustering2.labels_
df.head()


# In[50]:


inertia_scores2=[]
for i in range(1,11):
    kmeans2=KMeans(n_clusters=i)
    kmeans2.fit(df[['Annual Income (k$)', 'Spending Score (1-100)']])
    inertia_scores2.append(kmeans2.inertia_)
plt.plot(range(1,11),inertia_scores2)


# In[60]:


centers=pd.DataFrame(clustering2.cluster_centers_)
centers.columns=['x','y']
centers


# In[61]:


plt.figure(figsize=(10,8))
plt.scatter(x=centers['x'],y=centers['y'],c='black',marker='*')
sns.scatterplot(data=df, x='Annual Income (k$)' ,y='Spending Score (1-100)', hue='Spending and Income Clustering',palette='tab10')


# In[63]:


pd.crosstab(df['Spending and Income Clustering'],df['Gender'],normalize='index')


# In[64]:


pd.crosstab(df['Spending and Income Clustering'],df['Gender'])


# In[65]:


df.groupby('Spending and Income Clustering')['Age', 'Annual Income (k$)', 'Spending Score (1-100)'].mean()


# # MultiVariate Clustering

# In[67]:


from sklearn.preprocessing import StandardScaler


# In[68]:


scale = StandardScaler()


# In[73]:


dff=pd.get_dummies(df,drop_first=True)
dff.head()


# In[74]:


dff=dff[['Age', 'Annual Income (k$)','Spending Score (1-100)','Gender_Male']]


# In[76]:


dff=pd.DataFrame(scale.fit_transform(dff))


# In[78]:


inertia_scores3=[]
for i in range(1,11):
    kmeans3=KMeans(n_clusters=i)
    kmeans3.fit(dff)
    inertia_scores3.append(kmeans3.inertia_)
plt.plot(range(1,11),inertia_scores3)


# In[ ]:




