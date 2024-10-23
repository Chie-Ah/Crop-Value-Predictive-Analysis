#!/usr/bin/env python
# coding: utf-8

# In[70]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[71]:


#Exploration


# In[72]:


data = pd.read_csv("crop_production.csv")


# In[73]:


data.shape


# In[74]:


data.tail()


# In[75]:


data.columns


# In[76]:


data.describe()


# In[77]:


data.isnull().sum()


# In[78]:


#cleaning


# In[79]:


data = data.drop('Flag Codes', axis=1)
data


# In[80]:


#visualization


# In[81]:


#how crop yield evolved with time
sns.relplot(x='TIME', y='SUBJECT', data=data)


# In[82]:


#crop againts value 
sns.relplot(x='Value', y='SUBJECT', data=data)


# In[83]:


#crop value evolution over time  
sns.relplot(x='TIME', y='SUBJECT', hue='Value',data=data)


# In[84]:


#model
data.head()


# In[85]:


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[87]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['SUBJECT'] = le.fit_transform(data['SUBJECT'])


# In[88]:


data = pd.get_dummies(data, columns=['SUBJECT'])


# In[89]:


train = data.drop(['Value','index','INDICATOR','MEASURE','FREQUENCY','LOCATION'], axis=1)
test = data['Value']


# In[90]:


x_train, x_test, y_train, y_test = train_test_split(train, test, test_size=0.3, random_state=2)


# In[91]:


regr = LinearRegression()


# In[92]:


regr.fit(x_train, y_train)


# In[93]:


pred = regr.predict(x_test)


# In[94]:


pred


# In[95]:


#accuracy
regr.score(x_test, y_test)


# In[96]:


#my 1st try and accuracy too bad,will do better in the next.

