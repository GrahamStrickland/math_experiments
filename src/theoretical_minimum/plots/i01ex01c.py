import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0.5, 5.5, 0.1)


def theta(alpha):
    return np.exp(alpha) + alpha * np.log(alpha)


fig, ax = plt.subplots()
ax.plot(a, theta(a))
ax.set_title(
    "Theoretical Minimum: Interlude 1 - Exercise 1\nGraph of $\\theta(\\alpha) = e^\\alpha + \\alpha ln(\\alpha) $",
    usetex=True,
)
ax.set_xlabel("$\\alpha$", usetex=True)
ax.set_ylabel("$\\theta(\\alpha)$", usetex=True)

fig.savefig("i01ex01c.png", dpi=300)
