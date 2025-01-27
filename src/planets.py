#!/usr/bin/env python3

# Code from Nora's Guide to the Galaxy video at: https://www.youtube.com/watch?v=xEAhkUX7nVI

import time

import matplotlib.pyplot as plt
import numpy as np
import rebound
from astropy import units as u


def get_sim() -> rebound.Simulation:
    sim = rebound.Simulation()

    sim.add(m=0.957)
    sim.add(
        m=0.342,
        a=0.08143,
        e=0.0288,
        inc=np.deg2rad(90 - 89.613),
        omega=np.deg2rad(226.3),
    )
    sim.add(
        m=(2.07 * u.Mearth).to_value(u.Msun),
        a=0.2877,
        e=0.021,
        inc=np.deg2rad(90 - 89.752),
        omega=np.deg2rad(48.6),
    )
    sim.add(
        m=(19.02 * u.Mearth).to_value(u.Msun),
        a=0.6992,
        e=0.041,
        inc=np.deg2rad(90 - 90.395),
        omega=np.deg2rad(352),
    )
    sim.add(
        m=(3.17 * u.Mearth).to_value(u.Msun),
        a=0.9638,
        e=0.044,
        inc=np.deg2rad(90 - 90.1925),
        omega=np.deg2rad(306),
    )
    sim.add(
        primary=sim.particles[4],
        P=(5.877 * u.day).to_value(u.yr),
        e=0.01,
        inc=np.deg2rad(4),
        omega=4.77,
        Omega=0.83,
    )

    sim.move_to_com()

    return sim


def plot_sim(sim: rebound.Simulation) -> None:
    rebound.OrbitPlot(sim)
    rebound.OrbitPlot(sim, color=True, particles=[1, 2, 3, 4])
    rebound.OrbitPlot(sim, color=True, particles=[5], primary=4)

    plt.show()


def plot_progress(times: np.ndarray, smas: np.ndarray, ds: np.ndarray) -> None:
    plt.figure()
    plt.plot(times, smas.T)

    plt.figure()
    plt.plot(times, ds.T)
    plt.show()


def calc_progress(sim: rebound.Simulation) -> tuple[np.ndarray]:
    p = sim.particles
    times = np.linspace(0, 12 / 365, 1000)
    smas = np.full((len(p) - 1, len(times)), np.nan)
    ds = np.full((len(p) - 1, len(times)), np.nan)

    time0 = time.time()
    for i, t in enumerate(times):
        star_loc = [p[0].x, p[0].y, p[0].z]
        plt.plot(p[0].x, p[0].y, ".", color="C0", alpha=i / len(times))

        for j in range(1, len(p)):
            plt.plot(p[j].x, p[j].y, ".", color="C" + str(j), alpha=i / len(times))
            ds[j - 1, i] = np.sqrt(
                (p[j].x - star_loc[0]) ** 2
                + (p[j].y - star_loc[0]) ** 2
                + (p[j].z - star_loc[0]) ** 2
            )

            if j <= 4:
                smas[j - 1, i] = p[j].a
            else:
                orb = p[j].orbit(primary=p[1])
                smas[j - 1, i] = orb.a

        sim.integrate(t)

    lim = 1.1
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    plt.show()

    print(time.time() - time0)

    return times, smas, ds


def main() -> None:
    sim = get_sim()
    plot_sim(sim)

    times, smas, ds = calc_progress(sim)
    plot_progress(times, smas, ds)


if __name__ == "__main__":
    main()
