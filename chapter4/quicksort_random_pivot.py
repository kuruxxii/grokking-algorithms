import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # 将任何元素用作基准值都可行
        # 实现快速排序时，请随机地选择用作基准值的元素。快速排序的平均运行时间为O(nlogn)
        pivot_index = random.randint(0, len(arr)-1)
        pivot = arr[pivot_index]
        # partitioning
        less = [x for i, x in enumerate(
            arr) if i != pivot_index and x <= pivot]
        greater = [x for i, x in enumerate(
            arr) if i != pivot_index and x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


arr = [3, 5, 1, 5, 9, 11, 2, -1]


print(quicksort(arr))
print(arr)
