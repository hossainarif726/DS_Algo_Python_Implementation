#!/usr/bin/env python
# coding: utf-8

# In[2]:


def partition(lis, start, end):
    pivot = lis[start]
    low = start + 1
    high = end
    
    while True:
        
        while (low <= high) and (lis[low] <= pivot):
            low = low + 1
            
        while (low <= high) and (lis[high] >= pivot):
            high = high - 1
            
        if low <= high:
            lis[low], lis[high] = lis[high], lis[low]
            
        else:
            break
            
    lis[start], lis[high] = lis[high], lis[start]
    
    return high

def quicksort(lis, start, end):
    if start >= end:
        return
    
    p = partition(lis, start, end)
    quicksort(lis, start, p-1)
    quicksort(lis, p+1, end)
    
a = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
quicksort(a, 0, len(a)-1)
print(a)

