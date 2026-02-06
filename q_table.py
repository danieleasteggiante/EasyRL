import random

class QTable:
    def __init__(self, size : tuple, actions: list):
        self.size = size
        self.actions = actions
        self.matrix = self.__initialize_Q_table()

    def __initialize_Q_table(self):
        row, col = self.size
        return [[0 for _ in range(len(self.actions))] for _ in range(row * col)]

    def render(self):
        column_names = self.__populate_column_names()
        row_names = self.__populate_row_names()
        table_str = "       " + "  ".join(column_names) + "   \n"
        for i, row in enumerate(self.matrix):
            table_str += f"{row_names[i]} ¦ " + " ¦ ".join(f" {value} " for value in row) + " ¦\n"
        return table_str

    def __populate_column_names(self):
        return [action for action in self.actions]

    def __populate_row_names(self):
        rows = []
        for i in range(self.size[0]):
            name = f"({i},"
            for j in range(self.size[1]):
                rows.append(f"{name}{j})")
        return rows

    def update(self, state: tuple, action: int, value: float):
        action_index = self.actions.index(action)
        self.matrix[self.__index_from_state(state)][action_index] = value

    def __value(self, state: tuple, action: int):
        return self.matrix[self.__index_from_state(state)][action]

    def best_action(self, state: tuple):
        state_row = self.matrix[self.__index_from_state(state)]
        if all(value == 0 for value in state_row):
            return random.choice(self.actions)
        best_action = max(state_row)
        return self.actions[state_row.index(best_action)]

    def __index_from_state(self, state: tuple):
        row, col = state
        return row * self.size[1] + col
