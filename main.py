from bke import MLAgent, is_winner, opponent, RandomAgent, train, validate, plot_validation
import random

#creeert de class MyAgent met als basis MLAgent van de BKE library
class MyAgent(MLAgent):
  def evaluate(self, board):
    #checkt of de Agent heeft gewonnen of heeft verloren en voegt een reward toe aan de boardstate
    if is_winner(board, self.symbol):
      reward = 1
    elif is_winner(board, opponent[self.symbol]):
      reward = -1
    else:
      reward = 0
    #stuurt een reward terug naar de MLAgent functie
    return reward

#my_agent = MyAgent(1, 0.1)
#train(my_agent, 10000)

#creeert de random agent
random.seed(1)
random_agent = RandomAgent()

#zorgt ervoor dat de validation_agent gelijk is aan de random_agent
validation_agent = random_agent
#validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=1000)
#plot_validation(validation_result)

#functie om makkelijk te testen met verschillende parameters voor MyAgent
def NewAgent(name, alph, epsi): 
  name = MyAgent(alpha=alph, epsilon=epsi)
  train(name, 100000)
  validation_result = validate(agent_x=name, agent_o=validation_agent, iterations=1000)
  plot_validation(validation_result)

#creert een nieuwe agent via de NewAgent functie
NewAgent(1, 0.00001, 0.00001)