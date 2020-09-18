

def board_setup():
    board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
            ]
    return board


def print_board(board):
    print("         SODOKU          ")
    print("-------------------------")
    for i in board:
        z = 0
        if board.index(i) % 3 == 0 and board.index(i) != 0:
            print("|", end="")
            print("------------------------")
            print("| ", end = "")
        else:
            print("|", end=" ")
        for j in i:
            if (z % 3 == 0) and z != 0:
                print("|", end = " ")
            print(j, end = " ")
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


def validate_cell(row, col, pick, board):
    for l in board[row]:
        if l == pick:
            return False
    for m in board:
        if m[col] == pick:
            return False
    x = row//3
    y = col//3
    for s in range(x * 3,x * 3 + 3):
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


def main():
    board = board_setup()
    print_board(board)
    solve(board)
    print(" ")
    print("Here is the solved board:")
    print_board(board)



main()