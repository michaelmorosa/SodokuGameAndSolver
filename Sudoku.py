
def board_setup():
    Board = [
            [0,4,0,0,2,7,0,0,0],
            [8,0,0,6,4,0,0,0,0],
            [0,7,0,0,3,0,9,0,8],
            [4,1,0,9,0,0,0,0,0],
            [0,0,3,0,0,5,0,0,2],
            [0,0,8,0,0,0,0,1,6],
            [0,8,4,0,0,0,0,0,0],
            [0,9,6,0,0,0,7,0,0],
            [1,5,0,4,9,0,8,2,0]
            ]
    return Board


def print_board1(board1):
    print("         Sudoku Game        ")
    print("    0 1 2   3 4 5   6 7 8  ")
    print("  -------------------------")
    k = 0
    for i in board1:
        z = 0
        if board1.index(i) % 3 == 0 and board1.index(i) != 0:
            print("  |", end="")
            print("-----------------------", end = "")
            print("|")
            print(str(k) + " |", end=" ")
            k = k + 1
        else:
            print(str(k) + " |", end=" ")
            k = k + 1
        for j in i:
            if (z % 3 == 0) and z != 0:
                print("|", end=" ")
            print(j, end=" ")
            z = z + 1
        print("|")
    print("  -------------------------")


def choose_move(board1, move_list, wrong):
    print(" ")
    print_board1(board1)
    print("The number of wrong answers is " + str(len(wrong)))
    move_list.clear()
    while True:
        try:
            placement_move = input("Enter the row and column of your move with a space in between them:")
            if (len(placement_move) != 3) and (placement_move[0] != 9) and (placement_move[1] != 9) and (placement_move[1] != " "):
                print("Invalid Input. Try Again.")
                continue
            colrow = placement_move.split(" ",1)
            if board1[int(colrow[0])][int(colrow[1])] == 0:
                move = input("Enter your move:")
                if (len(move) != 1) or (int(move) == 0):
                    print("Invalid Input. Try Again.")
                    continue
                move_list.append(int(colrow[0]))
                move_list.append(int(colrow[1]))
                move_list.append(int(move))
                return move_list
            else:
                print("Invalid Input. Try Again.")
                continue
        except:
            print("Invalid Input. Try Again.")
            continue


def valid_move(a, board):
    r = board[a[0]][a[1]]
    b = a[2]
    if r == b:
        return True
    else:
        return False


def make_move(a, board1):
    board1[a[0]][a[1]] = a[2]


def print_board(board):
    print("         SODOKU          ")
    print("-------------------------")
    for i in board:
        z = 0
        if board.index(i) % 3 == 0 and board.index(i) != 0:
            print("|", end="")
            print("------------------------")
            print("| ", end="")
        else:
            print("|", end=" ")
        for j in i:
            if (z % 3 == 0) and z != 0:
                print("|", end=" ")
            print(j, end=" ")
            z = z + 1
        print("|")
    print("-------------------------")


def find_empty(board):
    w = 0
    for o in board:
        q = 0
        for p in o:
            if p == 0:
                lis = [True, w, q]
                return lis
            else:
                q = q + 1
                continue
        w = w + 1
    lis = [False]
    return lis


def find_empty1(board1):
    for o in board1:
        for p in o:
            if p == 0:
                return True
            else:
                continue
    return False


def validate_cell(row, col, pick, board):
    for l in board[row]:
        if l == pick:
            return False
    for m in board:
        if m[col] == pick:
            return False
    x = row // 3
    y = col // 3
    for s in range(x * 3, x * 3 + 3):
        for t in range(y * 3, y * 3 + 3):
            if board[s][t] == pick:
                return False
            else:
                continue
    return True


def solve(board):
    if not find_empty(board)[0]:
        last = [True, board]
        return last
    else:
        care = find_empty(board)
        row, col = care[1], care[2]
        for pick in range(1, 10):
            if validate_cell(row, col, pick, board):
                board[row][col] = pick
                if solve(board):
                    last = [True, board]
                    return last
                board[row][col] = 0
        return False


def win(board):
    print(" ")
    print("Well done! You've solved the board and won.")
    print("Here is the solved board:")
    print_board(board)


def lose(board):
    print(" ")
    print("You lost. Better luck next time.")
    print("Here is the solved board:")
    print_board(board)


def main():
    print("       The Game of Sudoku")
    print("You lose if you get 5 moves wrong")
    wrong = []
    move_list = []
    board = board_setup()
    board1 = board_setup()
    solve(board)
    while True:
        if not find_empty1(board1):
            win(board)
            exit()
        else:
            a = choose_move(board1, move_list, wrong)
            b = valid_move(a, board)
            if b:
                make_move(a, board1)
            else:
                wrong.append('x')
                if len(wrong) > 4:
                    lose(board)
                    exit()
                else:
                    continue


main()
