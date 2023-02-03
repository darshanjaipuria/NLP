#!/usr/bin/env python
# coding: utf-8

# # Simple Text Classification

# In[1]:


def gender_features(word):
    return { 'last_letter':word[-1]}


# In[7]:


gender_features('Winston')


# In[9]:


import nltk
nltk.download('names')
from nltk.corpus import names


# In[12]:


labeled_names = ([(name, 'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])


# In[15]:


import random
random.shuffle(labeled_names)


# In[14]:


featuresets = [(gender_features(n),gender) for (n,gender) in labeled_names]


# In[16]:


train_set, test_test = featuresets[500:], featuresets[:500]


# In[17]:


import nltk
classifier = nltk.NaiveBayesClassifier.train(train_set)


# In[18]:


classifier.classify(gender_features('David'))


# In[19]:


classifier.classify(gender_features('Darshan'))


# In[20]:


print(nltk.classify.accuracy(classifier,test_test))


# In[21]:


classifier.classify(gender_features('Shreya'))


# In[22]:


classifier.classify(gender_features('Naruto'))


# # Tweet Tokenizer

# In[23]:


import nltk


# In[24]:


from nltk.tokenize import TweetTokenizer
text = 'The Party was soooo fun 😊 :D #superfun'


# In[25]:


twtkn = TweetTokenizer()


# In[26]:


twtkn.tokenize(text)


# # Explore Coca 

# In[28]:


#shorturl.at


# In[29]:


#https://www.bing.com/ck/a?!&&p=b17aa236a274be07JmltdHM9MTY3MzQ4MTYwMCZpZ3VpZD0xYzkyMjAyNC0zYjZkLTY5ODQtMjllZC0zMTEwM2E2YjY4MGMmaW5zaWQ9NTE5Ng&ptn=3&hsh=3&fclid=1c922024-3b6d-6984-29ed-31103a6b680c&psq=contemporary+corpus+of+english&u=a1aHR0cHM6Ly93d3cuZW5nbGlzaC1jb3Jwb3JhLm9yZy9jb2NhLw&ntb=1


# In[ ]:


#Searched for Michael Jordan and Barack Obama

