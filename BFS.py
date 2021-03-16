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
visited = [] 
queue = []     #Initialise

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0) 
    print (s, end = "\n") 
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

t0 = time()
bfs(visited, graph, 'Homepage')
t1 = time() - t0
print('Time for BFS :', t1, 'seconds')
