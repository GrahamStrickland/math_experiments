import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0


def f(state, t):
    x, y, z = state  # Unpack the state vector
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z  # Derivatives


state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.01)

states = odeint(f, state0, t)

ax = plt.figure().add_subplot(projection="3d")
ax.plot(states[:, 0], states[:, 1], states[:, 2])
plt.show()
