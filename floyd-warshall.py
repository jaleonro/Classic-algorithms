import math


INF = math.inf

def floydWarshall(graph,source,destiny):
    dist = graph
    V= len(graph[0])
    parents = [[-1] * V for i in range(V)]
    for i in range(V):
        for j in range(V):
            if i==j or graph[i][j] == INF:
                parents[i][j]=-1
            else:
                parents[i][j] = i

    for k in range(V):
        for i in range(V):
            for j in range(V):
               if dist[i][k]+dist[k][j] < dist[i][j]:
                   dist[i][j]=dist[i][k]+dist[k][j]
                   parents[i][j]= parents[k][j]

    return dist[source][destiny],parents




# Driver program to test the above program
# Let us create the following weighted graph
"""
            10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3           """
graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]

long,parents=floydWarshall(graph,0,2)
print(long)
print(parents)
#printPath(parents,2)


