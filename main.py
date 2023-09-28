import random
from bke import *

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

my_random_agent = MyRandomAgent()

class MijnSpeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[4] == my_symbol:
            getal = getal + 5
        print(getal)
        return getal
 
mijn_speler = MijnSpeler()

class MijnSpeleres(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if can_win(board, my_symbol):
            getal = getal + 1000
        if can_win(board, opponent_symbol):
            getal = getal - 1000
        print(getal)
        return getal

mijn_speleres = MijnSpeleres()

class SlimmeSpeler(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
      getal = 1
      if 
    

slimme_speler = SlimmeSpeler()

while True:
    A = input("continue? 1(y)/2(n)")
    if A == "1":
        start(player_x=slimme_speler, player_o=my_random_agent)
    else:
        break