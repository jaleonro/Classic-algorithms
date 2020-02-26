import sys

def countingSort(A,k):
    C=[0 for _ in range(k+1)]
    B=[0 for _ in range(len(A))]
    for i in range(0,len(A)):
        C[A[i]]=(C[A[i]])+1
    for i in range (1,k+1):
        C[i]=C[i]+C[i-1]
    C[:] = [x - 1 for x in C]
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]]=A[i]
        C[A[i]]=(C[A[i]])-1
    return B

N = int(sys.stdin.readline().strip())
array=[]
for i in range(N):
    x = int ((float(sys.stdin.readline().strip()))*100)
    array.append(x)
G = int(sys.stdin.readline().strip())

print(format(((countingSort(array,100)[G])/100),'.2f'))





