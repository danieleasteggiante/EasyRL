from q_table import QTable
from simulator_2D import Simulator2D

if __name__ == '__main__':
    #simulator_2D = Simulator2D((1,3), ['left','right'], (0,2))
    #simulator_2D.train(10)
    q_table = QTable((1,3), ['left','right'])
    q_table.update((0,2), 1, 1.0)
    print(q_table.render())


