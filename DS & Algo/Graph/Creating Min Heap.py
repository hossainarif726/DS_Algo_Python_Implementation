#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def parent(i):
    return i // 2

def MinHeapify(lis, heap_size, i):
    l = left(i)
    r = right(i)
    smallest = 0
    temp = 0
    
    if (l <= heap_size) and lis[l] < lis[i]:
        smallest = l
    else:
        smallest = i
        
    if (r <= heap_size) and lis[r] < lis[smallest]:
        smallest = r
        
    if (smallest != i):
        temp = lis[i]
        lis[i] = lis[smallest]
        lis[smallest] = temp
        
        MinHeapify(lis, heap_size, smallest)
        
def build_min_heap(lis, heap_size):
    k = heap_size//2
    while k >= 1:
        MinHeapify(lis, heap_size, k)
        k = k - 1
    return lis

lis = [0,12,7,13,5,10,17,1,2,3]
print(build_min_heap(lis, len(lis)-1))

