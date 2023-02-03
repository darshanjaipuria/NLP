#!/usr/bin/env python
# coding: utf-8

# In[20]:


from urllib import request


# In[21]:


url = "https://www.gutenberg.org/files/98/98-0.txt"


# In[22]:


response = request.urlopen(url)


# In[23]:


raw = response.read().decode('utf8')


# In[27]:


import nltk
from nltk.tokenize import word_tokenize
tokens = word_tokenize(raw)


# In[28]:


print(tokens[:200])


# In[ ]:





# In[30]:


import nltk
from nltk.stem import PorterStemmer
porter = PorterStemmer()
porter.stem('joyous')


# In[31]:


porter.stem('happiness')


# In[32]:


porter.stem('cacti')


# In[37]:


import nltk
from nltk.stem import LancasterStemmer
lancaster = LancasterStemmer()
lancaster.stem('joyous')


# In[39]:


lancaster.stem('happiness')


# In[42]:


lancaster.stem('cacti')


# In[43]:


lancaster.stem('singing')


# In[41]:


import nltk
from nltk.stem import RegexpStemmer
regex = RegexpStemmer('ing')
regex.stem('singing')


# In[44]:


regex.stem('bring')


# In[45]:


import nltk
from nltk.stem import RegexpStemmer
regex = RegexpStemmer('ing$')
regex.stem('singing')


# In[47]:


import nltk
from nltk.stem import SnowballStemmer
snowball = SnowballStemmer('french')
snowball.stem('manger')


# In[50]:


porter=PorterStemmer()
text="It is the time of 1775, and Mr. Jarvis Lorry is going to Dover to meet the girl Lucie Manette. He tells her that she is not an orphan in the world, as this was told to her from a young age. Lorry says to her that he will travel with her to Paris, where she can meet her father. He also tells that her father Doctor Manette has recently been released from the Bastille, Paris, where he was kept for 18 years. Doctor Manette is presently at the house of Defarges’ family, where they are running a wine-shop. Her father has lost his memory due to some reason. But, he starts regaining it when he meets his daughter and then they went back to London."
stemmed = [porter.stem(token) for token in text.split(" ")]


# In[51]:


print(stemmed[:50])


# In[52]:


lancaster=LancasterStemmer()
text="It is the time of 1775, and Mr. Jarvis Lorry is going to Dover to meet the girl Lucie Manette. He tells her that she is not an orphan in the world, as this was told to her from a young age. Lorry says to her that he will travel with her to Paris, where she can meet her father. He also tells that her father Doctor Manette has recently been released from the Bastille, Paris, where he was kept for 18 years. Doctor Manette is presently at the house of Defarges’ family, where they are running a wine-shop. Her father has lost his memory due to some reason. But, he starts regaining it when he meets his daughter and then they went back to London."
stemmed = [lancaster.stem(token) for token in text.split(" ")]


# In[53]:


print(stemmed[:50])


# In[59]:


nltk.download('wordnet')
nltk.download('omw-1.4')


# In[60]:


from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
print(lemma.lemmatize("am"))


# In[61]:


print(lemma.lemmatize("mice"))


# In[63]:


print(lemma.lemmatize("am", pos='v'))


# In[ ]:




