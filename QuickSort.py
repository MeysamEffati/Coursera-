from turtle import right
import numpy as np

with open('QuickSort.txt') as f:
    a = [int(x) for x in f]
def FindMedian(A):
    minvalue = min(A)
    maxvalue = max(A)
    for i in range(3):
        if A[i] != minvalue and A[i] != maxvalue:
            return A[i]
def ChoosePivot(A, flag):
    n = len(A)
    first = A[0]
    final = A[n-1]
    if n % 2 == 1:
        middle = A[int(np.ceil(n/2))]
    else:
        middle = A[int(n/2)]

    if flag == 1:
        pivot = first 
    elif flag == 2:
        pivot = middle
    elif flag == 3:
        pivot = final

    return (pivot)


def Swap(A,first,second):
    second_value = A[second]
    first_value = A[first]
    A[first] = second_value
    A[second] = first_value
    return A

def Partition(A):
    pivot = A[0] #the first element is the pivot
    r = len(A)
    i = 1
    for j in range(1,r):
        if A[j]<pivot:
            A = Swap(A, i, j)
            i += 1
    A = Swap(A,0,i-1)
    return A,i-1

def QuickSort(A,flag):
    n = len(A)
    if n > 1:
        p = ChoosePivot(A, flag)
        A = Swap(A, 0, A.index(p))
        A, PositionPivot = Partition(A)
        A [:PositionPivot], left = QuickSort(A[:PositionPivot], flag)
        A [PositionPivot+1:], right = QuickSort(A[PositionPivot+1:], flag)
        return A, left+right+n-1
    else:
        return A,0


SortedMatrix, N = QuickSort(a, 1)

print('SortedMatrix', SortedMatrix)



