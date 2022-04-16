graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  print(visited)
  queue.append(node)
  print(queue)
  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 
    # print(m)
    for neighbour in graph[m]:
      print(neighbour)
      if neighbour not in visited:
        visited.append(neighbour)
        print(visited)
        queue.append(neighbour)
        print(queue)
# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling