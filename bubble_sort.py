import time
A = [34, 8, 64, 51, 32, 21]

def bubble(A):
    start = time.time()
    for i in range(0,len(A)):
        j = 0
        while j+i  < len(A) -1  :
            if A[j] > A[j+1]:
                tem = A[j + 1]
                A[j + 1] = A[j]
                A[j] = tem
            j += 1
    end = time.time()
    print(A)
    print(end-start)
    print()
