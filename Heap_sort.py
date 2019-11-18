import time


def heapify(A,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    # 判断左右子节点，是否大于根节点
    if left < n and A[i] < A[left]:
        largest = left
    if right < n and A[largest] < A[right]:
        largest = right
    # 需要完成的交换步骤
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        # 对‘上层’的堆进行重建
        heapify(A, n, largest)

# 中序遍历
def heap_sort(A):
    start = time.time()
    n = len(A)
    # 建立堆阶段
    for i in range(n-1,-1,-1):
        heapify(A, n, i)

    # 排序阶段
    for i in range(n-1, 0, -1): 
        A[i], A[0] = A[0], A[i]   # 交换
        # 去除最大点后，重建堆
        heapify(A, i, 0)
    end = time.time()
    print(A)
    print(end - start)
    print()

if __name__ == '__main__':
    A = [34, 8, 64, 51, 32, 21]
    heap_sort(A)
