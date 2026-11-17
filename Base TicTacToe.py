import numpy as np

ROW = 3
COL = 3

def new_board():
    board = np.array([[None for j in range(COL)] for i in range(ROW)])
    return board

test_new_board = new_board()


def render(board):
    rows = []
    for i in range(ROW):
        row = []
        for j in range(COL):
            row.append(board[i][j])
        rows.append(row)
        
    row_num = 0
    print('  0 1 2')
    print('  ------')
    for row in rows:
        output_row = ''
        for square in row:
            if square is None:
                output_row += ' '
            else:
                output_row += square
        print("%d|%s |" % (row_num, ' '.join(output_row)))
        row_num += 1
    print('  ------')
    
def make_move(player, board, move_coords):
    if board[move_coords[0]][move_coords[1]] is not None:
        print("Invalid Move")
        return
    
    board[move_coords[0]][move_coords[1]] = player
    
def is_board_full(board):
    for row in board:
        for square in row:
            if square is None:
                return False
    
    return True

def get_all_line_coords():
    #   [((0,0),(0,1),(0,2)), ((1,0),(1,1),(1,2)), ((2,0),(2,1),(2,2))]
    rows = []
    for x in range(ROW):
        row = []
        for y in range(COL):
            row.append((x,y))
        rows.append(row)
    
    #   [((0,0),(1,0),(2,0)), ((0,1),(1,1),(2,1)), ((0,2),(1,2),(2,2))]
    cols = []
    for x in range(COL):
        col = []
        for y in range(ROW):
            col.append((y,x))
        cols.append(col)
    
    
    diagonals =  [((0,0), (1,1), (2,2)),((0,2), (1,1), (2,0))]
    
    return rows + cols + diagonals

def get_winner(board):
    all_line_coords = get_all_line_coords()
    
    for line in all_line_coords:
        line_values = []
        
        for (x,y) in line:
            value = board[x][y]
            line_values.append(value)
        #print(line_values)

        if len(set(line_values)) == 1 and line_values[0] is not None:  
                return line_values[0]
            
    return None

def get_move():
    user_input = input("Enter Move Coords separated by spaces: ")
    coords = list(map(int, user_input.split()))
    
    return coords

def play():
    players = [
        ('X'),
        ('O')
    ]
    
    turn_count = 0
    board = new_board()
    
    while True:
        current_player_value = players[turn_count % 2]
        render(board)
        
        move_coords = get_move()
        make_move(current_player_value, board, move_coords)
        
        winner = get_winner(board)
        if winner is not None:
            render(board)
            print(f"Winner: {winner}")
            break
        
        if is_board_full(board):
            render(board)
            print("DRAW !!")
            break
            
        turn_count += 1

play()

