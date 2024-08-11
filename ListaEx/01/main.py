import numpy as np
import matplotlib.pyplot as plt

Q = 20
g = 9.81

def f(y):
    Ac = 3*y + (y**2)/2
    B = 3 + y
    return (1 - (Q**2)/(g * (Ac**3))*B)

def plot_graphs():
    y = np.linspace(0.7, 3, 2000)
    f_y = f(y)

    plt.plot(y, f_y)
    # plt.plot(1, f(1), marker='x', markersize='30', color='y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

plot_graphs()
             
