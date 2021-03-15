#!/usr/bin/env python
# coding: utf-8

# In[9]:


def KnapSack(C, w, val, n):
    k = [[0 for x in range(C+1) for x in range(n+1)]]
    
    for i in range(n+1):
        for j in range(C+1):
            if i == 0 or j == 0:
                k[i][j] = 0
                
            if w[i-1] <= j:
                
                #filling the 2D array with maximum value
                k[i][j] = max(val[i-1] + k[i-1][j-C[i-1]], k[i-1][j])
                
            else:
                k[i][j] = k[i-1][j]
                
    return k[n][C]

val = [60, 100, 120] 
w = [10, 20, 30] 
C = 50
n = len(val) 
print(knapSack(C, w, val, n)) 

