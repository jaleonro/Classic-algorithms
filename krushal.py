import heapq
def krushal (V,A):
    #A=a list of {w,u,v}
    N=len(V)
    heapq.heapify(A)
    T=[]
    for i in range(len(E)):
        conexComponent = set()
        T.append(conexComponent)

    for i in range(len(T)-1):
        currentEdge=heapq.heappop(A)
        u = currentEdge[1]
        v = currentEdge[2]
        set1=T[i]
        if u in set1:
            if v not in set1:
                for j in range(i+1,(len(T))):
                    set2==T[j]
                    if v in set2:
                        union=set1.union(set2)



            len(T) == N - 1:




