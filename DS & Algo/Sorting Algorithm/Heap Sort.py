#!/usr/bin/env python
# coding: utf-8

# In[23]:


def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def parent(i):
    return i // 2

def MaxHeapify(lis, heap_size, i):
    l = left(i)
    r = right(i)
    largest = 0
    temp = 0
    
    if (l <= heap_size) and lis[l] > lis[i]:
        largest = l
    else:
        largest = i
        
    if (r <= heap_size) and lis[r] > lis[largest]:
        largest = r
        
    if (largest != i):
        temp = lis[i]
        lis[i] = lis[largest]
        lis[largest] = temp
        MaxHeapify(lis, heap_size, largest)
    return lis
        
def build_max_heap(lis, heap_size):
    k = heap_size//2
    while k >= 1:
        MaxHeapify(lis, heap_size, k)
        k = k - 1
    return lis

def HeapSort(lis, n):
    for i in range(n, -1, -1):
        if i > 1:
            lis[1], lis[i] = lis[i], lis[1]
            i -= 1
            n -= 1
            MaxHeapify(lis, n, 1)
    return lis
            

lis = [0,12,7,13,5,10,17,1,2,3]
build_max_heap(lis, len(lis)-1)
print(HeapSort(lis, len(lis)-1))

