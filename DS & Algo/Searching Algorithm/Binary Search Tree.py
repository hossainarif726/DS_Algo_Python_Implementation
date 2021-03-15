#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BST(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    def insert_node(self, value):
        if value == self.data:
            return
        
        if value < self.data:
            if self.left_child:
                self.left_child.insert_node(data)
                
            else:
                self.left_child = BST(data)
                
        else:
            if self.right_child:
                self.right_child.insert_node(data)
                
            else:
                self.right_child = BST(data)
                
                
    def search_node(self, data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left_child:
                return self.left_child.search_node(data)
            
            else:
                return False
            
        else:
            if self.right_child:
                return self.right_child.search_node(data)
            
            else:
                return False

