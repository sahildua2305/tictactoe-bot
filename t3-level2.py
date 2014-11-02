
import random

class Board(object):
    winning_combos = (
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6])
    winners = ("X", "Tied", "O")

    def __init__(self, squares=[]):
        if len(squares)==0:
            self.squares = [None for i in range(9)]
        else:
            self.sqaures = squares

    def show(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print element
    
    def available_moves(self):
        return [k for k, v in enumerate(self.squares) if v is None]
        """r = []
        for i in [v for v in self.squares]:
            if i is None:
                r.append(i)
        return r"""

    def available_combos(self, player):
        return self.available_moves() + self.get_squares(player)

    def complete(self):
        if None not in [v for v in self.squares]:
            return True
        if self.winner() != None:
            return True
        return False

    def X_won(self):
        return self.winner()=="X"

    def O_won(self):
        return self.winner()=="O"

    def tied(self):
        return self.complete()==True and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    
    def get_squares(self, player):
        return [k for k, v in enumerate(self.squares) if v == player]
        """r = []
        for i in [v for v in self.squares]:
            if i == player:
                r.append(i)
        return r"""

    def make_move(self, position, player):
        self.squares[position] = player

    def block(self, player):
        for move in self.available_moves():
            self.make_move(move, get_enemy(player))
            if self.X_won():
                self.make_move(move, None)
                return move
            else:
                self.make_move(move, None)
        return False

    def win(self, player):
        for move in self.available_moves():
            self.make_move(move, player)
            if self.O_won():
                self.make_move(move, None)
                return move
            else:
                self.make_move(move, None)
        return False
    
    
def get_enemy(player):
    if player=='X':
        return 'O'
    return 'X'

if __name__ == "__main__":
    board = Board()
    board.show()

    while not board.complete():
        player = 'X'
        player_move = int(raw_input("Next Move: ")) - 1
        if not player_move in board.available_moves():
            continue
        board.make_move(player_move, player)

        if board.complete():
            break
        comp_player = get_enemy(player)
        comp_win = board.win(comp_player)
        comp_block = board.block(comp_player)
        if comp_win:
            board.make_move(comp_win, comp_player)
        elif comp_block:
            board.make_move(comp_block, comp_player)
        else:
            board.make_move(random.choice(board.available_moves()), comp_player)
        board.show()
    if board.winner():
        print "Winner is: "+board.winner()
    else:
        print "Game Tied"
