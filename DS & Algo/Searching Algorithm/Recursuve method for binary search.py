#!/usr/bin/env python
# coding: utf-8

# In[5]:


def bin_search(lis, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        
        if lis[mid] == x:
            return mid
        
        
        elif lis[mid] < x:
            return bin_search(lis, mid+1, high, x)
            
        else:
            return bin_search(lis, low, mid+1, x)
            
    else:
        return -1
    
#test
lis = [12,52,69,104,106]
x = 502
result = bin_search(lis, 0, len(lis)-1, x)

if result != -1:
    print('Element is present at index:',str(result))
    
else:
    print('Element is not present')


# In[ ]:




