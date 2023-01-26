maps_size = 3   # сторона поля
maps = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # игровое поле

def draw_maps():
    '''Выводим поле для игры'''
    print('_' * 4 * maps_size)
    for i in range(maps_size):
        print(('|' + ' ' * 3) * 4)
        print('|', maps[i*3], '|', maps[1+i*3], '|', maps[2+i*3], '|')
        print((('|' + '_' * 3) * 3) + '|')

def game_step(index, char):
    ''' Выполняем ход '''
    if (index > 9 or index < 1 or maps[index-1] in ('X', 'O')):
        return False

    maps[index-1] = char
    return True

def chek_win():
    ''' Проверяем победу играка '''
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # вертикальные линии
        (0, 4, 8), (2, 4, 6)                # диагональные линии
    )

    for pos in win_combination:
        if (maps[pos[0]] == maps[pos[1]] and maps[pos[1]] == maps[pos[2]]):
            win = maps[pos[0]]

    return win

def start_game():
    player = 'X'
    step = 1
    draw_maps()

    while (step < 10) and (chek_win() == False):
        index = input('Ходит игрок ' + player + '. Введите номер поля (0 - выход):')

        if (index == '0'):
            break

        if (game_step(int(index), player)):
            print('Ход выполнен !')

            if (player == 'X'):
                player = 'O'
            else:
                player = 'X'

            draw_maps()

            step += 1   # увеличим номер хода

        else:
            print('Неверный ход! Повторите!')



    if (step == 10):
        print('Игра окончена. Ничья!')
    else:
        print('Конец игры. Выиграл ' + chek_win())

print('Добро пожаловать в Крестики-нолики!')
start_game()