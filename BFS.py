from time import time  #to display time in seconds
graph = {
  'Homepage' : ['Director','Movie'], #level 0- Homepage, level 1- Director and Movie (child nodes)
  'Director': ['Name','Description'],  #level 2- Name and Description
  'Name': [], 
  'Description': [],
  'Movie' : ['Categories'], #level 2
  'Categories' : ['SciFi','Comedy'], #level 3- Scifi and Comedy
  'SciFi' : ['Transformers','Iron Man'], #level 4- Transformers and Iron Man (Child node for Scifi)
  'Comedy' : ['Dictator'],
  'Transformers':[],
  'Iron Man':[],
  'Dictator':[]
}
#Elements on same level are neighbours
visited = []  #To track the list of visited nodes
queue = []     #Initialising a queue
               #BFS uses queue 

def bfs(visited, graph, node):
  visited.append(node) #Tracking each visited node
  queue.append(node) #Tracking BFS for the graph
  while queue:
    s = queue.pop(0) 
    print (s, end = "\n") 
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

t0 = time()
bfs(visited, graph, 'Homepage') #Can change the 'node' value to check the time for that node
t1 = time() - t0
print('Time for BFS :', t1, 'seconds')
