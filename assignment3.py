import pandas as pd
import numpy as np
class td_qlearning:
  def __init__(self, path):
    #setup
    self.learning_rate = 0.1
    self.discount_factor = 0.5
    self.reward = -1
    self.trajectory = pd.read_csv(path, header=None)
    
  
  def qvalue(self, state, action):
    #setup
    pass

  def policy(self, state):
    #setup
    pass

#testing
def main():
  blah = td_qlearning("C:\\Users\\Matthew Talbot\\OneDrive\\Documents\\AI\\QLearning\\Example1\\Example1\\trajectory.csv")
  print(blah.trajectory[0])

if __name__ == "__main__":
  main()
