sdk = [[5, 4, 0, 0, 2, 0, 8, 0, 6],
       [0, 1, 9, 0, 0, 7, 0, 0, 3],
       [0, 0, 0, 3, 0, 0, 2, 1, 0],
       [9, 0, 0, 4, 0, 5, 0, 2, 0],
       [0, 0, 1, 0, 0, 0, 6, 0, 4],
       [6, 0, 4, 0, 3, 2, 0, 8, 0],
       [0, 6, 0, 0, 0, 0, 1, 9, 0],
       [4, 0, 2, 0, 0, 9, 0, 0, 5],
       [0, 9, 0, 0, 7, 0, 4, 0, 2]]


def print_sudoku(s):
    for i in range(len(s)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - -  \n")
        for j in range(len(s[0])):
            if j % 3 == 0 and j != 0:
                print("|  ", end="")
            print(str(s[i][j])+"   ", end="")
        print("\n")


def empty(s):
    for i in range(9):
        for j in range(9):
            if s[i][j] == 0:
                return (i, j)
    return None


def valid(s, n, pos):
    for i in range(len(s[0])):
        if s[pos[0]][i] == n and pos[1] != i:
            return False
    for i in range(len(s)):
        if s[i][pos[1]] == n and pos[0] != i:
            return False
    bx = pos[1]//3
    by = pos[0]//3

    for i in range(by*3, by*3 + 3):
        for j in range(bx*3, bx*3+3):
            if s[i][j] == n and (i, j) != pos:
                return False

    return True


def solve(s):
    find = empty(s)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(s, i, (row, col)):
            s[row][col] = i

            if solve(s):
                return True

            s[row][col] = 0

    return False


solve(sdk)
print_sudoku(sdk)
