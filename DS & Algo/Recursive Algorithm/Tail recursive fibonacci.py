#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fibonacci(n, a, b):
    if n == 0: return a
    elif n == 1: return b
    else:
        return fibonacci((n-1), b, a+b)
fibonacci(4, 0 ,1)

