import time
from functools import wraps
import bubble_sort
import Choice_Sort
import Heap_sort
import Shell_Sort
import Quick_sort
import Merge_Sort
import Insertion_Sort
import numpy as np

def func_timer(function):
    '''
    用装饰器实现函数计时
    :param function: 需要计时的函数
    :return: None
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        print ('[Function: {name} start...]'.format(name = function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print ('[Function: {name} finished, spent time: {time:.2f}s]'.format(name = function.__name__,time = t1 - t0))
        return result





if __name__ == '__main__':
    A = np.random.randint(1,10000,[5000]).tolist()
    bubble_sort.bubble(A)
    Insertion_Sort.insertion_sort(A)
    Choice_Sort.choice_sort(A)

    start = time.time()
    Merge_Sort.merge_sort(A)
    end = time.time()
    print(A)
    print(end-start)
    print()


    Shell_Sort.shell_sort(A)
    # Heap_sort.heap_sort(A)

    Quick_sort.quick_sort(A)