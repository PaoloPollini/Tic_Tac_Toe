# массив карты игры
map = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
]

# функция вывода карты на экран
def show_map():
    print('+---'*3 + '+')

    for i in range(3):
        for j in range(3):
            print( '| ' + str(map[i][j]), end = ' ')
        print('|\n' + '+---'*3 + '+'
              )

# функция запроса хода игрока
def next_step():
    s = int(input('Ваш ход: '))
    map[-1 * s //3 * -1 - 1][(s-1)%3] = 0

















def main():
    while True:
        show_map()
        next_step()
        
for i in range(3):
    for j in range(3):
        n = map[i][j]
        print(int(-1 * n //3 * -1 - 1), end = ' ')
        print((n-1)%3)
        
if __name__ == '__main__':
    main()
