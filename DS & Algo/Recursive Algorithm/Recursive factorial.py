#!/usr/bin/env python
# coding: utf-8

# In[13]:


def fac(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * fac(n-1)
    
print(fac(10))

