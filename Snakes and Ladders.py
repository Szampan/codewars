class SnakesLadders():

    def __init__(self):
        self.positions = {1: 0, 2: 0}
        self.current_player = 1

    def play(self, die1, die2):
        if self.is_gameover():
            return "Game over!"
        self.set_position(self.current_player, die1, die2)
        if self.has_won(self.current_player):
            self.gameover()
        tmp_player = self.current_player
        self.current_player = self.next_player(die1, die2)
        return f"Player {tmp_player} is on square {self.positions[tmp_player]}"

    def set_position(self, player, die1, die2):
        self.positions[player] = self.move_to(player, die1, die2)

    def move_to(self, player, die1, die2):
        LADDERS = ((2, 38), (7,14), (8,31), (15,26), (21,42), (28, 84), (36, 44), (51, 67), (71, 91), (78,98), (87, 94))
        SNAKES = ((16, 6), (46, 25), (49, 11), (62, 19), (64, 60), (74, 53), (89, 68), (92, 88), (95, 75), (99, 80))
        
        square = self.positions[player] + die1 + die2
        if square > 100:
            square = 100 - square

        for i in LADDERS+SNAKES:
            if square == i[0]:
                square = i[1]
        return square       
       
    def has_won(self, player):
        if self.positions[player] == 100:
            return True
        
    def next_player(self, die1, die2):
        print(die1, die2)
        if die1 == die2:
            print("SAME PLAYER AGAIN")
            return self.current_player
        else:
            print("NEXT PLAYER")
            if self.current_player == 1:
                return 2
            return 1
        
    def gameover(self):
        self.current_player = 0
        return f"Player {self.current_player+1} Wins!"
        
    def is_gameover(self):
        if self.current_player == 0:
            return True
    
    
    