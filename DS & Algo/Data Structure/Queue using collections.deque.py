#!/usr/bin/env python
# coding: utf-8

# In[4]:


from collections import deque

queue = deque()

queue.append(8)
queue.append(9)
queue.append(7)

print("Initial queue:\n", queue)

queue.popleft()
queue.popleft()
queue.popleft()

print("\nQueue after poped from rear:\n", queue)


# In[ ]:




