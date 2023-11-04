#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


import pandas as pd


# In[5]:


df = pd.read_csv("C:\\Users\\Sachi\\Downloads\\merged_data.csv")


# In[6]:


df


# In[8]:


df.drop('Unnamed: 0',axis = 1, inplace = True)


# In[9]:


df


# In[10]:


st.sidebar.title('Oil Prediction')

