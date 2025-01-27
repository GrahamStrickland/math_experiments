#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import scipy.special as special


def f(x):
    return special.fresnel(x)


x = np.linspace(0, 3.0)

y = f(x)

plt.plot(x, y)

plt.show()
