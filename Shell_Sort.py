import time


def get_sedgewick(le):
    sedgewick = []
    for i in range(0,le):
        sedgewick.append(9*4**i -9*2**i + 1)
    return sedgewick

def shell_sort(A):
    start = time.time()
    lis = [3,2,1]
    for gap in lis:
        for i in range(gap, len(A)):
            temp = A[i]
            j = i
            while j >= gap &  A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp

    end = time.time()
    print(A)
    print(end-start)
    print()


if __name__ == '__main__':
    A = [34, 8, 64, 51, 32, 21]
    shell_sort(A)
    print(A)