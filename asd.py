import sys
import math
N = int (sys.stdin.readline().strip())
array = sys.stdin.readline().strip().split()
def insertionSort(array):
    j=0
    while j < len(array):
        i = j-1
        key=array[j]
        while array[i]>key and i>-1:
            array[i+1]=array[i]
            i=i-1
        array[i+1]=key
        j=j+1
    return array
