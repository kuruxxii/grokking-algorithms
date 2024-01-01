def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


list = [4, 7, 9, 12, 16, 30, 100, 200]

print(binary_search(list, 4))
print(binary_search(list, 9))
print(binary_search(list, 100))
