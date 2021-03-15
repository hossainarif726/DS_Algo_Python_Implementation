#!/usr/bin/env python
# coding: utf-8

# In[10]:


def bfs(visited, graph, first_node):
    visited.append(first_node)
    queue.append(first_node)
    
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        
        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

graph = {
  '1' : ['2','6'],
  '2' : ['1', '7', '3'],
  '3' : ['2', '4'],
  '4' : ['3', '7', '5'],
  '5' : ['4', '7', '6'],
  '6' : ['1', '5'],
  '7' : ['2', '4', '5']
}

visited = []
queue = []

bfs(visited, graph, '1')

