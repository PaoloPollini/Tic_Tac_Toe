'''
    Крестики нолики v1.2

    (c)saigon 2022
    Written: Oct 16 2022.
    Last Updated: Oct 18 2022
    GitHub: https://github.com/PaoloPollini/Tic_Tac_Toe
    
'''
# массив карты игры
game_map = [[1,2,3],
            [4,5,6],
            [7,8,9]]

# набор выигрышных вариантов
win_opt = [[1,2,3],
           [4,5,6],
           [7,8,9],
           [1,4,7],
           [2,5,8],
           [3,6,9],
           [1,5,9],
           [3,5,7]]

# функция вывода карты на экран
def show_map():
    print('\n' + '+---'*3 + '+')
    for i in range(3):
        for j in range(3):
            print( '| ' + str(game_map[i][j]), end = ' ')
        print('|\n' + '+---'*3 + '+')


# функция делает ход в ячейку списка
# проверив, не занята ли ячейка
def next_step(step, znak):
    row = -1 * step //3 * -1 - 1                # вычисляем номер строки
    col = (step-1)%3                            # номер колонки
    if game_map[row][col] not in ('X', 'O'):    # если ячейка не занята
        game_map[row][col] = znak
        step_ok = True
    else:
        step_ok = False
    return step_ok

        
# функция проверяет текущий результат игры
def get_result():
    win = ''
    # собираем списки во множество и если в нем ХО - ничья
    draw = set.union(set(game_map[0]),set(game_map[1]),set(game_map[2]))
    if len(draw) == 2:
        win = 'N'
    # проверяем выигрышные комбинации
    for s0,s1,s2 in win_opt:
        if game_map[-1 * s0 //3 * -1 - 1][(s0-1)%3] ==\
           game_map[-1 * s1 //3 * -1 - 1][(s1-1)%3] ==\
           game_map[-1 * s2 //3 * -1 - 1][(s2-1)%3]:
            win = game_map[-1 * s0 //3 * -1 - 1][(s0-1)%3]
    return win

# поиск шага с подсчетом Х и О в линиях выигрышных вариантов
def find_step(num_X,num_O):
    step = ''
    for line in win_opt:
        x = 0
        o = 0
        for s in line:
            if game_map[-1 * s //3 * -1 - 1][(s-1)%3] == 'X':
                x = x + 1
            if game_map[-1 * s //3 * -1 - 1][(s-1)%3] == 'O':
                o = o + 1
        if x == num_X and o == num_O and step == '':
            for t in line:
                if game_map[-1 * t //3 * -1 - 1][(t-1)%3] not in ('X', 'O'):
                    step = game_map[-1 * t //3 * -1 - 1][(t-1)%3]

    return step


# выбор хода компьютером
def computer_step():
    step = ''

    # 1- если два нолика и пусто - делаем ход и выигрываем
    step = find_step(0,2)

    # 2- если два крестика и пусто - ставим нолик, блокируем противника
    if step == '':
        step = find_step(2,0)

    # 3- если один нолик и пусто - ставим нолик
    if step == '':
        step = find_step(0,1)

    # 4- если центр не занят - ставим нолик
    if step == '':
        if game_map[1][1] not in ('X', 'O'):
            step = 5

    # 5- если занят центр - занимаем первую ячейку 
    if step == '':
        if game_map[0][0] not in ('X', 'O'):
            step = 1

    # 6- если один крестик и пусто - ставим нолик (наметилась ничья)
    if step == '':
        step = find_step(1,0)

    return step


# основная функция программы
def main():
    game_over = False
    player1 = True
    win_dict = {'N':'Ничья!', 'X':'Выиграли крестики!', 'O':'Выиграли нолики!'}
    while game_over == False:
        show_map()
        try:
            if player1:
                znak = 'X'
                step = int(input('Игрок X, ваш ход: '))
            else:
                znak = 'O'
                #step = int(input('Игрок O, ваш ход: '))
                step = computer_step()
                print("Компьютер делает ход: " + str(step))
        
            if step >0 and step < 10:
                if next_step(step, znak):
                    player1 = not(player1)
                else:
                    print('Ячека занята, повторите ввод')
            else:
                print('Введенное число вне диапазона игрового поля')

        except ValueError:
            print('Введено не верное значение. Повторите ввод.')

        win = get_result() # проверяем победителя
        if win != '':
            game_over = True

    show_map()
    print('Игра окончена. ' + win_dict[win])
    input()


if __name__ == '__main__':
    main()
