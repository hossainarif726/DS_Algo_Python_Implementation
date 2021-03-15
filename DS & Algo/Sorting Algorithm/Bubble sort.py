#!/usr/bin/env python
# coding: utf-8

# In[2]:


def bubble_sort(lis,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis

lis = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(lis, len(lis)-1))

