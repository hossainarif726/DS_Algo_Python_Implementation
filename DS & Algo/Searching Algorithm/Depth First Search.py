#!/usr/bin/env python
# coding: utf-8

# In[8]:


def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(node)
        
        for i in graph[node]:
            dfs(visited, graph, i)
            
graph = {
  '1' : ['4','2'],
  '2' : ['8', '7', '5', '3', '1'],
  '3' : ['10', '9', '4', '2'],
  '4' : ['3', '1'],
  '5' : ['2', '7', '6', '8'],
  '6' : ['5'],
  '7' : ['2', '8', '5'],
  '8' : ['7', '5', '2'],
  '9' : ['3'],
  '10' : ['3']
}

visited = set()

dfs(visited, graph, '1')


# In[ ]:




