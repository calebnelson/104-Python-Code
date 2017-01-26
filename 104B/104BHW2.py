# Author: Caleb Nelson
# Math 104B HW #2
import math
def f(t, y):
    return 1 + y/t #insert y' here

def midpoint(a, b, N, alpha):
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    t[0] = a
    w[0] = alpha
    for i in range(1, N):
        w[i] = w[i-1] + h*f(t[i-1] + (h/2), w[i-1] + (h/2)*f(t[i-1],w[i-1]))
        t[i] = a + i*h
    return [t, w]

def mod_euler(a, b, N, alpha):
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    t[0] = a
    w[0] = alpha
    for i in range(1, N):
        t[i] = a + i*h
        w[i] = w[i-1] + h/2*(f(t[i-1], w[i-1]) + f(t[i], w[i-1]+h*f(t[i-1],w[i-1])))
    return [t, w]

def heun(a, b, N, alpha):
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    t[0] = a
    w[0] = alpha
    for i in range(1, N):
        tt = t[i-1]
        wt = w[i-1]
        t[i] = a + i*h
        w[i] = wt + (h/4)*(f(tt,wt) + 3*f(tt+((2*h)/3), wt+((2*h)/3)*f(tt+(h/3), wt+(h/3)*f(tt,wt))))
    return [t, w]

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
