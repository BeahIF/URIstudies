
N,P = list(map(int,input().strip().split(' ')))
connections = [-1] * N


'''Basic way of storing connected components for quick find.'''
def connect_quick_find(connections, u, v):
    print(connections)
    print(u)
    print(v)
    if connections[u] > -1 and connections[v] == -1:
        print("entra nessa")
        connections[v] = connections[u]
        return
    if connections[v] > -1 and connections[u] == -1:
        connections[u] = connections[v]
        return
    if connections[u] > -1 and connections[v] > -1:
        connect_to = min(connections[u], connections[v])
        connect_it = connections[v]
        for i in range(len(connections)):
            if connections[i] == connect_it:
                connections[i] = connections[u]
        return 
    connections[u] = u
    connections[v] = u
    return


for a0 in range(P):
    u,v = input().strip().split(' ')
    u,v = [int(u),int(v)]
    connect_quick_find(connections,u,v)


'''Preparing a counts array of number of nodes in each connected component i.e number of persons in each country.'''
counts = [0] * N
print(connections)
for i in range(len(connections)):
    print("no for")
    print(connections[i])
    if connections[i] == -1:
        connections[i] = i
    counts[connections[i]] = counts[connections[i]] + 1
    print(counts[connections[i]])
combinations = 0
sum = 0


'''calculating combination'''
for i in range(len(counts)-1,-1,-1):
    combinations = combinations + abs(counts[i])*sum
    sum = sum + abs(counts[i])

print(combinations)