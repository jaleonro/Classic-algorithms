import math


def quickSort(array, p, r):
    if p<r:
        q=partition(array,p,r)
        quickSort(array,p,q-1)
        quickSort(array,q+1,r)

def partition(array,p,r):
    x=array[r]
    i=p-1
    for j in range(p,r):
        if array[j]>=x:
            i=i+1
            temp=array[i]
            array[i]=array[j]
            array[j]=temp
    temp2=array[i+1]
    array[i+1]=array[r]
    array[r]=temp2
    return i+1


def bucketSort(A):
    C=[]
    n=len(A)
    B=[[] for _ in range(n)]
    for i in range(0,n):
        B[(math.floor((A[i])*n))].append(A[i])
    for i in range(0, n):
        quickSort(B[i],0,(len(B[i]))-1)
    for i in range(0, n):
         C+=B[i]
    return C




