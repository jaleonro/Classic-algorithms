import sys
T = int (sys.stdin.readline().strip())

for j in range(0,T):
    array = list(map(int, sys.stdin.readline().strip().split()))
    k=len(array)
    suma = 0

    for i in range(k):
        suma = suma + array[i]
    array.append(suma)

    while suma<10**100:
        suma=(suma-(array[len(array)-k]))+suma
        array.append(suma)

    print(len(array-1))
