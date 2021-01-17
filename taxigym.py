'''"There are 4 locations (labeled by different letters), and our job is to pick up the passenger at one location 
and drop him off at another. We receive +20 points for a successful drop-off and lose 1 point for 
every time-step it takes. There is also a 10 point penalty for illegal pick-up and drop-off actions."

The filled square represents the taxi, which is yellow without a passenger and green with a passenger.
The pipe ("|") represents a wall which the taxi cannot cross.
R, G, Y, B are the possible pickup and destination locations. 
The blue letter represents the current passenger pick-up location, and the purple letter is the current destination.

Reinforcement Learning will learn a mapping of states to the optimal action to perform in that state by exploration, 
i.e. the agent explores the environment and takes actions based off rewards defined in the environment.'''

import gym
import numpy as np


env = gym.make("Taxi-v3")

q_table = np.zeros([env.observation_space.n, env.action_space.n65])
state = env.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
print("State:", state)

env.s = state
env.render()

print(env.P[328])
