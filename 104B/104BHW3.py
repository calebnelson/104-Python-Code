# Author: Caleb Nelson
# Math 104B HW #3
import math
def f(t, y):
    return y - t**2 + 1 #insert y' here

def runge_kutta_4(a, b, N, alpha):
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    k = [0.0 for i in range(4)]
    t[0] = a
    w[0] = alpha
    for i in range(1, N):
        ttemp = t[i-1]
        wtemp = w[i-1]
        k0 = h*f(ttemp, wtemp)
        k1 = h*f(ttemp + (h/2), wtemp + (k0/2))
        k2 = h*f(ttemp + (h/2), wtemp + (k1/2))
        k3 = h*f(ttemp + h, wtemp + k2)
        w[i] = wtemp + ((k0 + 2*k1 + 2*k2 + k3)/6)
        t[i] = a + i*h
    return [t, w]

def adams_bashforth_4(a, b, N, alpha):
    if (N <= 4):
        return runge_kutta_4(a, b, N, alpha)
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    x = runge_kutta_4(a, a + (3*h), 4, alpha)
    t[0] = a
    w[0] = alpha
    for i in range(1, 4):
        t[i] = a + i*h
        w[i] = x[1][i]
    for i in range(4, N):
        t[i] = a + i*h
        w[i] = w[i-1] + h*(55*f(t[i-1], w[i-1]) - 59*f(t[i-2], w[i-2]) + 37*f(t[i-3], w[i-3]) - 9*f(t[i-4], w[i-4]))/24
        
    return [t, w]

def adams_moulton_4(a, b, N, alpha):
    if (N <= 4):
        return runge_kutta_4(a, b, N, alpha)
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    x = runge_kutta_4(a, b, N, alpha)
    t[0] = a
    w[0] = alpha
    for i in range(1, N):
        t[i] = a + i*h
        w[i] = x[1][i]
    for i in range(4, N):
        w[i] = w[i-1] + h*(9*f(t[i], w[i]) + 19*f(t[i-1], w[i-1]) - 5*f(t[i-2], w[i-2]) + f(t[i-3], w[i-3]))/24
    return [t, w]

def adams_pc_4(a, b, N, alpha):
    if (N <= 4):
        return runge_kutta_4(a, b, N, alpha)
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    x = runge_kutta_4(a, a + (3*h), 4, alpha)
    t[0] = a
    w[0] = alpha
    for i in range(1, 4):
        t[i] = a + i*h
        w[i] = x[1][i]
    for i in range(4, N):
        t[i] = a + i*h
        w[i] = w[i-1] + h*(55*f(t[i-1], w[i-1]) - 59*f(t[i-2], w[i-2]) + 37*f(t[i-3], w[i-3]) - 9*f(t[i-4], w[i-4]))/24
        w[i] = w[i-1] + h*(9*f(t[i], w[i]) + 19*f(t[i-1], w[i-1]) - 5*f(t[i-2], w[i-2]) + f(t[i-3], w[i-3]))/24
    return [t, w]
