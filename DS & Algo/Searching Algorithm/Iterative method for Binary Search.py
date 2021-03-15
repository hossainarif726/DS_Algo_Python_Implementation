#!/usr/bin/env python
# coding: utf-8

# In[12]:


#iterative method of binary search
def bin_search(lis,x):
    low = 0
    high = len(lis)-1
    mid = 0
    
    while low <= high:
        
        mid = (low + high) // 2
        
        if lis[mid] < x:
            low = mid + 1
            
        elif lis[mid] > x:
            high = mid - 1
            
        else:
            return mid
        
    return -1

#test
lis = [68,89,90,198]
x = 54
result = bin_search(lis,x)

if result != -1:
    print('Element is present at index:',result)
else:
    print('Element is not present')

