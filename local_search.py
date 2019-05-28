import itertools

def attacks(a, b):
    same_row_or_column = (a.x == b.x) or (a.y == b.y)
    if same_row_or_column:
        return True # return early to avoid division by zero

    same_diagonal = abs((a.y - b.y) / (a.x - b.x)) == 1
    return same_diagonal

def get_num_of_attacking_queens(board):
    count = 0
    for pair in itertools.combinations(board, 2):
        if attacks(pair[0], pair[1]):
            count += 1
    return count

# Note: he board will always have a single queen in each column.
def get_queen_idx_in_column(board, column):
    #print("column", column)
    for i, queen in enumerate(board):
        if queen.x == column:
            return i

def is_queen(board, x, y):
    for queen in board:
        if queen.x == x and queen.y == y:
            return True
    return False

class Queen:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

def get_attack_counts(board):
    grid = []
    for x in range(6):
        grid.append([0]*6)
        for y in range(6):
            queen_idx = get_queen_idx_in_column(board, x+1)

            # move it up by one, wrap around
            new_y_coord = (board[queen_idx].y % 6) + 1
            board[queen_idx].y = new_y_coord

            # calculate number of attacks in new position
            #print("board[queen_idx]", board[queen_idx])
            #print("attack count", get_num_of_attacking_queens(board))
            grid[x][new_y_coord-1] = get_num_of_attacking_queens(board)

    return grid

def print_grid(board):
    grid = get_attack_counts(board)

    for y in range(5, -1, -1):
        line = ""
        for x in range(6):
            if is_queen(board, x+1, (y%6)+1):
                line += "X "
            else:
                line += str(grid[x][y]) + " "
        print(line)

board = [
    Queen(1,4),
    Queen(2,1),
    Queen(3,5),
    Queen(4,2),
    Queen(5,6),
    Queen(6,4),
]

print_grid(board)
