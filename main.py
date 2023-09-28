from bke import MLAgent, is_winner, opponent, RandomAgent, train, validate, plot_validation
import random

class MyAgent(MLAgent):
  def evaluate(self, board):
    if is_winner(board, self.symbol):
      reward = 1
    elif is_winner(board, opponent[self.symbol]):
      reward = -1
    else:
      reward = 0
    return reward

#my_agent = MyAgent(1, 0.1)
#train(my_agent, 10000)

random.seed(1)
random_agent = RandomAgent()

validation_agent = random_agent
#validation_result = validate(agent_x=my_agent, agent_o=validation_agent, iterations=1000)
#plot_validation(validation_result)

def NewAgent(name, alph, epsi):
  name = MyAgent(alpha=alph, epsilon=epsi)
  train(name, 100000)
  validation_result = validate(agent_x=name, agent_o=validation_agent, iterations=1000)
  plot_validation(validation_result)

NewAgent(1, 0.00001, 0.00001)