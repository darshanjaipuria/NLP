#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[8]:


from nltk.book import brown


# In[4]:


nltk.download


# In[5]:


nltk.download()


# In[7]:


from nltk.book import *


# In[9]:


from nltk.corpus import brown


# In[10]:


brown.categories()


# In[11]:


brown.words(categories = 'news')[:10]


# In[12]:


from nltk.corpus import inaugural


# In[13]:


inaugural.fileids()


# In[17]:


inaugural.words(fileids='2017-Trump.txt')[:50]


# In[ ]:




