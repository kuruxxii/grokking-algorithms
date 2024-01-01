def factorial(i):
    if i == 1:  # base case
        return 1
    else:  # recursive case
        return i * factorial(i-1)


print(factorial(5))
print(factorial(1))
