import random
from typing import List

from actions_2D import Actions2D
from environment_2D import Environment2D
from q_table import QTable


class Simulator2D:
    def __init__(self,
                 environment : tuple,
                 actions : List[str],
                 reward_position: tuple,
                 initial_position : tuple = (0,0)):
        self.environment = Environment2D(environment, reward_position, initial_position)
        self.actions = Actions2D(actions)
        self.Q_table : QTable = QTable(self.environment.matrix_size, self.actions.actions)

    def train(self, episodes: int):
        state = self.environment.initial_position
        for episode in range(episodes):
            print(f"Training episode {episode + 1}/{episodes}")
            action = self.__choose_action(state)
            print(f"Chosen action: {action}")
            new_state, reward, done = self.__step(state, action)
            self.Q_table.update(state, action, reward)
            state = new_state
            if done:
                print("Reached the reward position!")
                break


    def __choose_action(self, state):
        q_table_value = self.Q_table.value(state)
        action =  self.__map_action_to_int(random.choice(self.actions.actions))

    def __map_action_to_int(self, action):
        action_mapping = {
            'up': (0,-1),
            'down': (0,1),
            'left': (-1,0),
            'right': (1,0)
        }
        return action_mapping.get(action, -1)

    def __step(self, state, action):
        new_state = state[0] + action[0], state[1] + action[1] # move to new state
        reward = self.environment[new_state[0]][new_state[1]] # get reward for new state
        done = new_state == self.environment.reward_position # check if episode is done
        return new_state, reward, done