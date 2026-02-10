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
                 initial_position : tuple = (0,0),
                 epsilon : float = 0.5):
        self.environment = Environment2D(environment, reward_position, initial_position)
        self.actions = Actions2D(actions)
        self.Q_table : QTable = QTable(self.environment.matrix_size, self.actions.actions)
        self.epsilon = epsilon
        self.out_of_bounds_penalty = -1

    def train(self, episodes: int, epchos: int = 100):
        for epoch in range(epchos):
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
        probability = random.random()
        if probability < self.epsilon:
            return random.choice(self.actions.actions)
        return self.Q_table.best_action(state)

    def __map_to_movement(self, action):
        action_mapping = {
            'up': (-1,0),
            'down': (1,0),
            'left': (0,-1),
            'right': (0,1)
        }
        return action_mapping.get(action, -1)

    def __step(self, state, action):
        movement = self.__map_to_movement(action)
        new_state = self.__get_new_state(state, movement)
        reward = self.__get_reward(state, new_state)
        done = self.__check_if_done(new_state)
        return new_state, reward, done

    def __get_reward(self, state, new_state):
        if new_state == state:
            # controlla se il nuovo stato == stato significa che è uscito dai confini e
            # gli è stato assegnato il vecchio stato, quindi assegna la penalità
            return self.out_of_bounds_penalty
        if new_state == self.environment.reward_position:
            return self.environment.value(self.environment.reward_position)
        if self.__is_out_of_bound(new_state):
            return self.out_of_bounds_penalty
        return 0

    def __is_out_of_bound(self, state):
        row, col = state
        m_row, m_col = self.environment.matrix_size
        return row < 0 or row >= m_row or col < 0 or col >= m_col

    def __check_if_done(self, state):
        return state == self.environment.reward_position

    def __get_new_state(self, state, movement):
        new_row = state[0] + movement[0]
        new_col = state[1] + movement[1]
        if self.__is_out_of_bound((new_row, new_col)):
            # se è out of bounds ritorna lo stato vecchio
            return state
        return new_row, new_col