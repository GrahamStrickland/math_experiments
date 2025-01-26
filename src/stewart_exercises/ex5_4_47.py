import matplotlib
import numpy as np

matplotlib.rcParams["text.usetex"] = True
import matplotlib.pyplot as plt


def f(x):
    return 1 - 2 * x - 5 * x**4


x = np.linspace(-1, 1)

y = f(x)

fig, ax = plt.subplots()

l1 = ax.plot(x, y, label="$y = 1 - 2x - 5x^4$")

ax.axis([-1, 1, -6, 2])
ax.set_title("Stewart Ex. 5.4.47")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
ax.grid()

plt.show()
