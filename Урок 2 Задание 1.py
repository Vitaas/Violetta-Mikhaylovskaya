# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно
# не запрашивать у пользователя, а указать явно, в программе.

my_list = ['super', 8, 3.14159, (1, 2, 3), ['a', 1], None, True]
# print(type(my_list[0]))
# print(type(my_list[1]))
# print(type(my_list[2]))
# print(type(my_list[3]))
# print(type(my_list[4]))
# print(type(my_list[5]))
# print(type(my_list[6]))

for i in my_list:
    print(type(i))
