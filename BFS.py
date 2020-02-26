import math

def bfs(adjDict,s):
    visited=set()
    distance = dict.fromkeys(adjDict.keys(), math.inf)
    parent = dict.fromkeys(adjDict.keys(), None)
    distance [s]=0
    queue=[]
    queue.append(s)
    while queue:
        u=queue.pop(0)
        for i in range(0, len(adj[u])):
            v = adj[u][i]
            if v not in visited:
                visited.add(v)
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
        visited.add(u)
    return parent

def printPath(adj,parent,s,v):
    if s==v:
        print(str(s))
    else:
        if  parent[v]==None:
            print("there is no path beetween s and v")
        else:
            printPath(adj,parent,s,parent[v])
            print (str(v))



adj=dict([('r', ['s','v']), ('v', ['r']), ('s', ['r','w']), ('w', ['s','t','x']), ('t', ['w','x','u']),
          ('x', ['w','t','u','y']),('u', ['t','x','y']),('y', ['u','x'])])
parents=bfs(adj,'s')
printPath(adj,parents,'s','u')




