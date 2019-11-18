import time

A = [34, 8, 64, 51, 32, 21]

def choice_sort(A):
    start = time.time()
    for i in range(0,len(A)):
        t = i
        for j in range(i,len(A)):
            if A[i] > A[j] & A[t] > A[j]:
                t = j
            j += 1

        A[t],A[i] = A[i],A[t]

    end = time.time()
    print(A)
    print(end - start)
    print()