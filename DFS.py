from time import time
graph = {
  'Homepage' : ['Director','Movie'],
  'Director': ['Name','Description'],
  'Name': [],
  'Description': [],
  'Movie' : ['Categories'],
  'Categories' : ['SciFi','Comedy'],
  'SciFi' : ['Transformers','Iron Man'],
  'Comedy' : ['Dictator'],
  'Transformers':[],
  'Iron Man':[],
  'Dictator':[]
}
visited = set() 
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

t0 = time()
dfs(visited, graph, 'Homepage')
t1 = time() - t0
print('Time for DFS :', t1, 'seconds')

