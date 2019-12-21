revenue = int(input('Выручка: '))
costs = int(input('Издержки: '))
profit = revenue - costs

if profit > 0:
    print('Финансовый результат: прибыль')
    profitability = profit / revenue
    print(f'Коэффициент рентабельности: {profitability}')
    employees = int(input('Численность сотрудников: '))
    profit_per_employee = profit / employees
    print(f'Прибыль на одного сотрудника составила {profit_per_employee}')
elif profit < 0:
    print('Финансовый результат: убыток')
else:
    print('Финансовый результат: 0')
