using DynamicalSystems
using CairoMakie

function lorenz96_rule!(du, u, p, t)
    F = p[1]; N = length(u)
    # 3 edge cases
    du[1] = (u[2] - u[N - 1] * u[N] - u[1]) + F
    du[2] = (u[3] - u[N]) * u[1] - u[2] + F
    du[N] = (u[1] - u[N - 2]) * u[N - 1] - u[N] + F
    # then the general case
    for n in 3:(N - 1)
        du[n] = (u[n + 1] - u[n - 2]) * u[n - 1] - u[n] + F
    end
    return nothing # always `return nothing` for in-place form!
end

N = 6
u0 = range(0.1, 1; length = N)
p0 = [8.0]
lorenz96 = CoupledODEs(lorenz96_rule!, u0, p0)

total_time = 12.5
sampling_time = 0.02
Y, t = trajectory(lorenz96, total_time; Ttr = 2.2, Δt = sampling_time)

fig = Figure()
ax = Axis(fig[1, 1]; xlabel = "time", ylabel = "variable")
for var in columns(Y)
    lines!(ax, t, var)
end
fig
