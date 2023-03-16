def show_board(b):
    num = '  0 1 2'
    print(num)
    for row, i in zip(b, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")


def users_input(b, user):
    global x, y
    while True:
        place = input(f"Ходит {user}. Введите координаты: ").split()
        if len(place) != 2:
            print("Введите две координаты ")
            show_board(board)
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print("Введите числа ")
            show_board(board)
            continue
        x, y = map(int, place)
        if not (0 <= x < 3 and 0 <= y < 3):
            print("Вышли из диапазона ")
            show_board(board)
            continue
        if b[x][y] != '*':
            print("Клетка занята ")
            show_board(board)
            continue
        break
    return x, y


def win_position(b, user):
    b_list = []
    for r in b:
        b_list += r

    positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    indices = set([i for i, x in enumerate(b_list) if x == user])
    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False


def start(board):
    count = 0
    while True:
        show_board(board)
        if count % 2 == 0:
            user = 'X'
        else:
            user = '0'
        if count < 9:
            x, y = users_input(board, user)
            board[x][y] = user

        elif count == 9:
            print('Ничья')
            break
        if win_position(board, user):
            print('-' * 11)
            print(f"Выйграл '{user}'")
            print('-' * 11)
            show_board(board)
            break
        count += 1


board = [['*'] * 3 for _ in range(3)]

start(board)
