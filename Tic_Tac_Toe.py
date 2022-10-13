'''
Крестики нолики v1.0

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
    print()
    print('+---'*3 + '+')

    for i in range(3):
        for j in range(3):
            print( '| ' + str(game_map[i][j]), end = ' ')
        print('|\n' + '+---'*3 + '+')


# функция делает ход в ячейку массива
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
    for s0,s1,s2 in win_opt:
        if game_map[-1 * s0 //3 * -1 - 1][(s0-1)%3] ==\
           game_map[-1 * s1 //3 * -1 - 1][(s1-1)%3] ==\
           game_map[-1 * s2 //3 * -1 - 1][(s2-1)%3]:
            win = game_map[-1 * s0 //3 * -1 - 1][(s0-1)%3]
    return win



def main():
    game_over = False
    player1 = True
    
    while game_over == False:
        show_map()
        try:
            if player1:
                znak = 'X'
                step = int(input('Игрок X, ваш ход: '))
            else:
                znak = 'O'
                step = int(input('Игрок O, ваш ход: '))
        
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
    print('Игра оконена. Выиграл игрок ' + win)





        
for i in range(3):
    for j in range(3):
        n = game_map[i][j]
        print(int(-1 * n //3 * -1 - 1), end = ' ')
        print((n-1)%3)
        
if __name__ == '__main__':
    main()
