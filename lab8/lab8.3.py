# Пользователь вводит два набора чисел. Выведите на экран числа, которые встречаются в обоих наборах.
def check(number):
    while True:
        try:
            if number == 'конец':
                return 'конец'
            return int(number)
        except ValueError:
            number = input('Введено некорректное значение ಥ_ಥ повторите попытку ')

set_1 = set()
set_1 = set()
set_2 = set()
while True:
    var = (input('Введите элемент 1 множества, если ввод элементов закончен, введите "конец": '))
    var = check(var)
    if var != 'конец':
        set_1.add(var)
    else:
        break

while True:
    var = (input('Введите элемент 2 множества, если ввод элементов закончен, введите "конец": '))
    var = check(var)
    if var != 'конец':
        set_2.add(var)
    else:
        break
same_var = set_1.intersection(set_2)
if same_var == set():
    print('Нет элементов пренадлежащих обоим множествам')
else:
    print(same_var)

print('hello world')