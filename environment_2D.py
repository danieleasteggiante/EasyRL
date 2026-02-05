
class Environment2D:
    def __init__(self, matrix_size: tuple, reward_position: tuple, initial_position : tuple):
        self.matrix_size = matrix_size
        self.initial_position = initial_position
        self.reward_position = reward_position
        if not self.__is_valid_position(reward_position) or not self.__is_valid_position(initial_position):
            raise ValueError("Invalid initial or reward position")
        self.env = self.__create_environment()

    def __create_environment(self):
        row, col = self.matrix_size
        return [[0 for _ in range(col)] for _ in range(row)]

    def __is_valid_position(self, reward_position):
        r_row, r_col = reward_position
        m_row, m_col = self.matrix_size
        return r_col < m_col and r_row < m_row