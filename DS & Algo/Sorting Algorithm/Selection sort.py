#!/usr/bin/env python
# coding: utf-8

# In[4]:


def selection_sort(lis, n):
    for i in range(n):
        minimum_index = i
        for j in range(i+1, n):
            if lis[minimum_index] > lis[j]:
                minimum_index = j
                
        lis[i], lis[minimum_index] = lis[minimum_index], lis[i]
    return lis

lis = [64, 25, 12, 22, 11]
print(selection_sort(lis, len(lis)))

