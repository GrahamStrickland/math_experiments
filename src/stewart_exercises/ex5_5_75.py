import matplotlib
import numpy as np

matplotlib.rcParams["text.usetex"] = True
import matplotlib.pyplot as plt


def f(x):
    return np.sqrt(2 * x + 1)


x = np.linspace(0, 1, 100)

y = f(x)

fig, ax = plt.subplots()

l1 = ax.plot(x, y, "b", label="$y = \\sqrt{{2x + 1}}$")

ax.axis([0, 1, 0, 2])
ax.set_title("Stewart Ex. 5.5.75")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend()
ax.grid()

plt.show()
