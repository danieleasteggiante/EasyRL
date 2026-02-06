from simulator_2D import Simulator2D

if __name__ == '__main__':
    simulator_2D = Simulator2D((3,3), ['left','right','up','down'], (2,2))
    simulator_2D.train(60)
    print(simulator_2D.Q_table.render())


