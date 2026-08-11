class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Board:
    vaild_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        self.board_array = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        lines=[]
        lines.append(f" {self.board_array[0][0]} | {self.board_array[0][1]} | {self.board_array[0][2]} ")
        lines.append(f"----------\n")
        lines.append(f" \n {self.board_array[1][0]} | {self.board_array[1][1]} | {self.board_array[1][2]} ")
        lines.append(f"----------\n")
        lines.append(f" \n {self.board_array[2][0]} | {self.board_array[2][1]} | {self.board_array[2][2]} ")
        return "".join(lines)

    def move(self, move_string):
        if not move_string in Board.vaild_moves:
            raise TictactoeException("That's not a vaild move.")
        move_index = Board.vaild_moves.index(move_string)
        row = move_index // 3 #row 
        column = move_index // 3 #column
        if self.board_array[row][column] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][column] = self.turn
        self.last_move = move_string

        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    def whats_next(self):
        cat = True
        for i in range(3):
            for j in range(3):
                if self.board_array[i][j] == " ":
                    cat = False
                else:
                    continue
                break
            else:
                continue
            break
        if (cat):
            return (True, "Cat's Game.")

        win = False
        for i in range(3):
            if self.board_array[i][0] != " ":
                if self.board_array[i][0] == self.board_array[i][1] and self.board_array[i][1] == self.board_array[i][2]: 
                    win = True
                    break
            if not win:
                for i in range(3):
                    if self.board_array[0][i] != " ":
                        if self.board_array[0][i] == self.board_array[1][i]and self.board_array[1][i] == self.board_array[2][i]:win = True
                        break
            if not win:
                if self.board_array[1][1] != " ":
                    if self.board_array[0][0] == self.board_array[1][1] and self.board_array[2][2] == self.board_array[1][1]:
                        win = True
                    if self.board_array[0][2] == self.board_array[1][1] and self.board_array[2][0] == self.board_array[1][1]:
                        win = True

            if not win:
                if self.turn == "X":
                    return (False, "X's turn.")
                else:
                    return (False, "O's turn")
            else:
                if self.turn == "0":
                    return (True, "X wins")
                else:
                    return (True, "O wins")
        
print("Welcome to Tic-Tac-Toe!")
board = Board()
game_over = False

while not game_over:
    print("\n" + str(board))

    status = board.whats_next()
    game_over = status[0]
    message = status[1]

    if game_over:
        print(message)
        break

    print(message)
    user_move = input("Enter your move (ex: 'center', 'upper right'): ")

    try:
        board.move(user_move)
    except TictactoeException as e:
        print(f"{e} Please try again.")
