# Вариант 1
# def my_func(x, y):
#     return x**y
#
#
# print(my_func(2, -2))

# Вариант 2
def my_func():
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    i = 1
    while y > 0:
        i *= x
        y -= 1
    return i


print(my_func())
