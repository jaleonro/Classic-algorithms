import heapq
import sys
from Queue import PriorityQueue
T = int(sys.stdin.readline().strip())
#priorityQueue=queue.PriorityQueue()
#queue.put((-priority, item))


for i in range(T):
    line = list(map(int, sys.stdin.readline().strip().split()))
    N,X=line[0],line[1]
    capacities = list(map(int, sys.stdin.readline().strip().split()))
    heapq.heapify(capacities)
    numberOfBottles=0
    currentCapacityReached=0
    while currentCapacityReached <= X and capacities:
        currentBottleCapacity=heapq.heappop(capacities)
        if currentCapacityReached+currentBottleCapacity <= X:
            numberOfBottles=numberOfBottles+1
            currentCapacityReached=currentCapacityReached+currentBottleCapacity
    print(numberOfBottles)
