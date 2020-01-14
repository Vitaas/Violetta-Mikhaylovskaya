def my_func(a, b, c):
    if c >= b >= a:
        return b + c
    elif c >= a >= b:
        return a + c
    elif b >= a >= c:
        return a + b
    elif b >= c >= a:
        return c + b
    elif a >= b >= c:
        return b + a
    elif a >= c >= b:
        return c + a


print(my_func(1, 2, 5))
