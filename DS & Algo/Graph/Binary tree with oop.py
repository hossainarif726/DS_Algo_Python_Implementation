#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
root = Node(5)
root.left = Node(3)
root.right = Node(6)

