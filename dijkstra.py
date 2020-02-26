import sys
import math
import heapq

def dijkstra(adjDict,weights,a,b):
    distance = dict.fromkeys(adjDict.keys(), math.inf)
    parents =  dict.fromkeys(adjDict.keys(), None)
    distance[a] = 0 #min distances
    known=set()
    distances=[]#candidates
    adjKeys=list(adjDict.keys())
    for i in range(0,len(adjKeys)):
        if not adjKeys[i]==a:
            item=[math.inf,adjKeys[i]]
        else:
            item = [0, adjKeys[i]]
        heapq.heappush(distances, item)

    while distances:
        item=heapq.heappop(distances)
        u=item[1]
        if u not in known:
            known.add(u)
            for i in range(0, len(adj[u])):
                v = adj[u][i]
                if distance[v]>distance[u]+weights["("+u+","+v+")"]:
                    distance[v] = distance[u] + weights["(" + u + "," + v + ")"]
                    parents[v]=u

    return distance[b],parents

def printPath(parents,j):
    if parents[j]==-1:
        print(j)
        return;
    printPath(parents, parents[j])
    print(j)

T = int(sys.stdin.readline().strip())
for i in range(T):
    adj = {}
    weights = {}
    line = sys.stdin.readline().strip().split()
    N = int(line[0])
    E = int(line[1])
    Q = int(line[2])

    for j in range(E):
        line = sys.stdin.readline().strip().split()
        if adj.get(line[0]) is None:
            adj[line[0]] = []
            adj[line[0]].append(line[1])
        else:
            adj[line[0]].append(line[1])

        weights["(" + line[0] + "," + line[1] + ")"] = int(line[2])




    for k in range(Q):
        line = sys.stdin.readline().strip().split()
        response=dijkstra(adj,weights,line[0],line[1])
        if response==math.inf:
            print(-1)
        else:
            print(response)
