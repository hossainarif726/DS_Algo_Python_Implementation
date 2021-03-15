#!/usr/bin/env python
# coding: utf-8

# In[2]:


def tail_rec_fac(n, a):
    if (n == 0) or (n == 1): return a
    else: return tail_rec_fac((n-1),a=(n*a))
    
tail_rec_fac(10, 1)


# In[ ]:




