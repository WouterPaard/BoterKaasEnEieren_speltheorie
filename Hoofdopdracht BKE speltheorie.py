import random
from bke import *

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

class MySmartAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        return getal
    
my_random_agent = MyRandomAgent()
my_smart_agent = MySmartAgent()

start(player_o=my_smart_agent, player_x=my_random_agent)