def sum(arr):
    # 编写涉及数组的递归函数时，基线条件通常是数组为空或只包含一个元素。
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])


arr = [1, 3, 5, 7, 9]
print(sum(arr))
