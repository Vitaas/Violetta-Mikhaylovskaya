while True:
    list_sum = list(map(int, input('Введите числа через пробел: ').split()))
    a = 0
    while a < len(list_sum):
        try:
            list_sum[a] = int(list_sum[a])
        except ValueError:
            print(sum(list_sum))
            break
        a += 1
    sum_num = 0
    for i in list_sum:
        sum_num += i
    print(sum_num)
