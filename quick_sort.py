import sys
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

T = int (sys.stdin.readline().strip())

for j in range(0,T):
    minCal= math.inf
    studentsMIn = []
    print("Caso #" + str(j + 1) + ":")
    N = int(sys.stdin.readline().strip())
    for i in range(0,N):
        line = sys.stdin.readline().strip().split()
        cal=float(line[1])
        if cal<minCal:
            minCal=cal
            studentsMIn = []
            studentsMIn.append(line[0])
        elif cal==minCal:
            studentsMIn.append(line[0])
    quickSort(studentsMIn,0,(len(studentsMIn))-1)
    for k in range(0,len(studentsMIn)):
        print(str(studentsMIn[k]))
    print("\n")
