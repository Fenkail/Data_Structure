import time
import sys
sys.setrecursionlimit(10000)

def partition(A, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = A[high]
    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[high] = A[high], A[i + 1]
    return (i + 1)


def quick_sorting(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        # 确定了pi元素的位置是正确的
        quick_sorting(A, low, pi - 1)
        quick_sorting(A, pi + 1, high)

def quick_sort(A):
    start = time.time()
    low = 0
    high = len(A) - 1
    quick_sorting(A, low, high)
    end = time.time()
    print(A)
    print(end-start)
    print()


if __name__ == '__main__':
    A = [34, 8, 64, 51, 32, 21]
    quick_sort(A)
    print(A)
