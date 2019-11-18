def choice_sort(left, right):
    ans =[]
    i,j =0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    # 字符串特性  越界之后不加
    ans += left[i:]
    ans += right[j:]
    return ans


def merge_sort(A):
    if len(A)  < 2:
        return A
    half = int((len(A))/2)
    left = merge_sort(A[:half])
    right = merge_sort(A[half:])
    return  choice_sort(left, right)


if __name__ == '__main__':
    A = [34, 8, 64, 51, 32, 21]
    A = merge_sort(A)
    print(A)
