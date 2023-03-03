square = 3
board = [1,2,3,4,5,6,7,8,9,]
mode_h_vs_h = '1'
mode_h_vs_ai = '2'
def draw_board():
    print('_' * 4 * square)
    for i in range(square):

        print('', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)

def AI_step(human , ai):
    avialable_step = [i-1 for i in board if type(i) == int]
    win_step = (4,0,2,6,8,1,3,5,7,)
    for char in (ai, human):
        for pos in avialable_step:
            board_ai = board[:]
            board_ai[pos] = char
            if (check_win(board_ai) != False):
                return pos
    for pos in win_step:
        if (pos in avialable_step):
            return pos
    return False
def next_players(current_player):
    if (current_player == 'x'):
        return 'o'
    return 'x'

def game_step(index, char):
    if (index >9 or index < 1 or board[index-1] in ('x', 'o')):
        return False
    board[index - 1] = char
    return True
def check_win(board):
    win = False
    win_if = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    )
    for num in win_if:
        if (board[num[0]] == board[num[1]] and board[num[1]] == board[num[2]]):
            win = board[num[1]]


    return win
def start_game(mode):
    curent_player = 'x'
    ai_player = 'o'
    step = 1
    draw_board()

    while (step < 10) and (check_win(board) == False):
        index = input('Ходит игрок ' + curent_player + ' .Введите номер поля (0-конец игры):')
        if(index == '0'):
            break

        if(game_step(int(index), curent_player)):
            print('ход противника.')

            curent_player = next_players(curent_player)
            draw_board()
            step += 1
            if (mode == mode_h_vs_ai):
                ai_step = (AI_step('x', 'o'))
                if (ai_step  != False):
                    board[ai_step] = ai_player
                    curent_player = next_players(curent_player)

                    step += 1
                print('Режим: Человек против компютера')

                draw_board()
        else:
            print('неверный ход ещё раз. ')

    if (step == 10):
        print('Игра окончена, Ничья! ')

    elif (check_win(board) != False):
        print('Выиграл ' + check_win(board))

print("Начало игры")
mode = 0
while mode not in (mode_h_vs_h, mode_h_vs_ai):
    mode = input("Ружим игры: \n1 - Человек против человека \n2 - Человек против Коипютера\nВыберите режим игры. ")
start_game(mode)