#!/usr/bin/env python
# coding: utf-8

# In[1]:


def insertion_sort(lis, n):
    for i in range(1, n):
        item = lis[i]
        j = i -1
        while (j >= 0) and (lis[j] > item) :
            lis[j+1] = lis[j]
            j = j - 1
            
        lis[j+1] = item
    return lis

lis = [12, 11, 13, 5, 6]
print(insertion_sort(lis, len(lis)))

