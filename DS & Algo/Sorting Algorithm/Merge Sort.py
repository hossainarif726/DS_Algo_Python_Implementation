#!/usr/bin/env python
# coding: utf-8

# In[6]:


def Merge(left, right):
    lis = []
    i,j = 0,0
    
    
    # this loop will run until one of the loop is empty
    while i < len(left) and j < len(right):
        
        
        #comparing first element of both sorted list
        if left[i] < right[j]:
            lis.append(left[i])
            i += 1
            
        else:
            lis.append(right[j])
            j += 1
            
    
    #for appending remaning elements of the list which isn't empty
    while (i < len(left)):
        lis.append(left[i])
        i += 1
        
    while (j < len(right)):
        lis.append(right[j])
        j += 1
        
    return lis
        
        
def MergeSort(L):
    if len(L) < 2:
        return L[:]
    
    else:
        mid = len(L) // 2
        left = MergeSort(L[:mid])
        right = MergeSort(L[mid:])
        return Merge(left, right)
    
a = [29,99,27,41,66,28,44,78,87,19,31]
MergeSort(a)

