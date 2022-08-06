def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))


# tail recursion
def factorial(n, a):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return a
    else:
        return factorial(n - 1, n * a)


print(factorial(5, 1))
