import sys
import math

def parent(i):
    return (i - 1) // 2

def left(i):
    return (2 * i)+1

def right(i):
    return (2 * i) + 2

def minHeapify(a,i,heapSize):
    l = left(i)
    r = right(i)
    if l <= heapSize-1 and a[l] < a[i]:
        shortest = l
    else:
        shortest = i
    if r <= heapSize-1 and a[r] < a[shortest]:
        shortest = r
    if not shortest == i:
        a[i],a[shortest] = a[shortest],a[i]
        minHeapify(a,shortest,heapSize)

def builtMinHeap(a):
    for i in range((len(a) // 2)-1, -1, -1):
        minHeapify(a,i,len(a))
    return a

def heapExtractMin(a):
    min=a[0]
    print(a)
    a[0]=a[(len(a))-1]
    minHeapify(a,0,(len(a))-1)
    return min

def heapDecreaseKey(a,i,key):
    a[i]=key
    while i>0 and a[parent(i)]>a[i]:
        a[i],a[parent(i)]=a[parent(i)],a[i]
        i=parent(i)

def minHeapInsert(a,key):
    a.append(math.inf)
    heapDecreaseKey(a,(len(a))-1,key)

def heapSort(a):
    builtMinHeap(a)
    b=[]
    for i in range(0,len(a)):
        b.append(heapExtractMin(a))
    return b

a=[4,3,2,1,0]

b=heapSort(a)
print (b)