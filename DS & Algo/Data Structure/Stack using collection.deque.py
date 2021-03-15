#!/usr/bin/env python
# coding: utf-8

# In[8]:


#similar to a list operation
from collections import deque

stack = deque()

stack.append(50)
stack.append(60)
stack.append(70)

print("Initial Stack:\n",stack)

stack.pop()
stack.pop()
stack.pop()

print("\nStack after poped:\n",stack)


# In[ ]:




