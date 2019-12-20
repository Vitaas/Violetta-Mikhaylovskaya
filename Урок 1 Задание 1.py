name = input('Как вас зовут? ')
dollar_course = int(input('Введите курс доллара: '))
rubles = int(input('Сколько рублей у вас есть: '))
dollars = rubles / dollar_course

print(f'{name}, вы можете купить {dollars} долларов.')
