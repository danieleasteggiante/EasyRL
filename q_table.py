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
        """
            ¦ left ¦ right ¦ up ¦ down ¦
        0,0 ¦ 0    ¦ 0     ¦ 0 ¦ 0   ¦
        0,1 ¦ 0    ¦ 0     ¦ 0 ¦ 0   ¦
        0,2 ¦ 0    ¦ 0     ¦ 0 ¦ 0   ¦
        1,0 ¦ 0    ¦ 0     ¦ 0 ¦ 0   ¦
        1,1 ¦ 0    ¦ 0     ¦ 0 ¦ 0   ¦
        [...]
        """
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
        self.matrix[self.__index_from_state(state)][action] = value

    def __value(self, state: tuple, action: int):
        return self.matrix[self.__index_from_state(state)][action]

    def choose_action(self, state: tuple, epsilon: float):
        actions_values = [self.__value(state, action) for action in range(len(self.actions))]
        best_choice = max(actions_values)
        probability = random.random()
        if probability < epsilon:
            return random.choice(range(len(self.actions)))
        return actions_values.index(best_choice)

    def __index_from_state(self, state: tuple):
        row, col = state
        return row * self.size[1] + col
