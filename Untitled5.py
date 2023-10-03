#!/usr/bin/env python
# coding: utf-8

# In[13]:


l = [(2,5),(1,2),(4,4),(2,3),(2,1)]
l.sort(key = lambda item:item[1])
print("sorted based on second element",l)


# In[15]:


ascii_dict = {}
for letter in range(ord('a'),ord('z')+1):
    ascii_dict[chr(letter)]=letter
print(ascii_dict)    


# In[ ]:




