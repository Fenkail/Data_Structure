import random
import time

A = [34, 8, 64, 51, 32, 21]

def insertion_sort(A):
    start = time.time()
    for i in range(0,len(A)):
        j = i
        while j > 0:
            if A[j] < A[j-1]:
                tem = A[j-1]
                A[j-1] = A[j]
                A[j] = tem
                j -= 1
            else:
                break

    end = time.time()
    print(A)
    print(end - start)
    print()

if __name__ == '__main__':
    B = []
    for i in range(1000):
        xx = random.randrange(1,10000,1)
        B.append(xx)
    insertion_sort(B)