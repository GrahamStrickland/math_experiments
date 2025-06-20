using DynamicalSystems
using CairoMakie

function henon_rule(u, p, n) # here `n` is "time", but we don't use it.
    x, y = u # system state
    a, b = p # system parameters
    xn = 1.0 - a*x^2 + y
    yn = b*x
    return SVector(xn, yn)
end

u0 = [0.2, 0.3]
p0 = [1.4, 0.3]

henon = DeterministicIteratedMap(henon_rule, u0, p0)

total_time = 10_000
X, t = trajectory(henon, total_time)
scatter(X)
