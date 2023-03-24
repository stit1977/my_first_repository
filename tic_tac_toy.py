game = [(' 123')]  # Создаем список для поля игры
for i in range(1, 5):
    game.append(list(map(int, range(1, 5))))  # Делаем матрицу для поля игры
game.pop()  # Удаляем последний элемент из списка списков (он лишний)

game[2][0] = 2  # Меняем значения в манрице для корректного отображения поля игры
game[3][0] = 3
game[1][1] = game[2][1] = game[2][2] = game[2][3] = game[1][2] = game[1][3] = game[3][1] = game[3][2] = game[3][3] = '-'

for i in game:  # выводим готовое поле на экран
    print(*i)

row_and_column = '1 2 3'  # Переменная для прохождения по ней циклом и проверки вхождений
tic_tac = '0 x'  # Переменная для прохождения по ней циклом и проверки вхождений

total = None  # Переменная для аргумента функции
a = None


def enter_position(position):  # вводим номер строки и столбца.
    while True:  # Проверка корректрости ввода номера строки и столбца
        total = input('Введите номер строки, столбца:')
        if total in row_and_column:
            return int(total)
        else:
            print('Неправильно, друг, попробуйте ещё раз!')


def enter_data(x, y):  # ввод кркстика или нолика
    if game[x][y] != '-':
        print('Ничья! Сыграем ещё раз?')
    else:
        if game[x][y] == '-':
            while True:  # Проверка корректрости ввода "0" или "х"
                a = input('Введите "0" или "х":')
                if a in tic_tac:
                    game[x][y] = a
                    break
                else:
                    print('Неправильно, друг, попробуйте ещё раз!')
        else:
            print('Клетка занята, сделайте другой выбор: ')
        for i in game:
            print(*i)

        if (
                ((game[3][3] == '0') and (game[2][2] == '0') and (game[1][1] == '0')) or
                ((game[1][3] == '0') and (game[2][2] == '0') and (game[3][1] == '0')) or
                ((game[1][3] == '0') and (game[2][3] == '0') and (game[3][3] == '0')) or
                ((game[1][2] == '0') and (game[2][2] == '0') and (game[3][2] == '0')) or
                ((game[1][1] == '0') and (game[2][1] == '0') and (game[3][1] == '0')) or
                ((game[3][1] == '0') and (game[3][2] == '0') and (game[3][3] == '0')) or
                ((game[2][1] == '0') and (game[2][2] == '0') and (game[2][3] == '0')) or
                ((game[1][1] == '0') and (game[1][2] == '0') and (game[1][3] == '0'))
        ):
            print('Нолики победили!')  # Проверка выйгрышных вариантов для ноликов
        elif (
                ((game[3][3] == 'x') and (game[2][2] == 'x') and (game[1][1] == 'x')) or
                ((game[1][3] == 'x') and (game[2][2] == 'x') and (game[3][1] == 'x')) or
                ((game[1][3] == 'x') and (game[2][3] == 'x') and (game[3][3] == 'x')) or
                ((game[1][2] == 'x') and (game[2][2] == 'x') and (game[3][2] == 'x')) or
                ((game[1][1] == 'x') and (game[2][1] == 'x') and (game[3][1] == 'x')) or
                ((game[3][1] == 'x') and (game[3][2] == 'x') and (game[3][3] == 'x')) or
                ((game[2][1] == 'x') and (game[2][2] == 'x') and (game[2][3] == 'x')) or
                ((game[1][1] == 'x') and (game[1][2] == 'x') and (game[1][3] == 'x'))
        ):
            print('Крестики победили!')  # Проверка выйгрышных вариантов для крестиков
        else:
            return enter_data(enter_position(x), enter_position(
                x))  # Если выйгрышных вариантов нет, то возвращаем функцию для ее перезапуска


x, y = enter_position(total), enter_position(total)  # задаем координаты для ввода "0" или "х"

enter_data(x, y)  # Вызываем функцию для начала игры.
