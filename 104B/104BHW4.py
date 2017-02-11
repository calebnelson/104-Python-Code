# Author: Caleb Nelson
# Math 104B HW #4
import math

def runge_kutta(a, b, m, N, alpha, f):
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [[0.0 for i in range(m)] for i in range(N)]
    k = [[0.0 for i in range(4)] for i in range(m)]
    t[0] = a
    w[0] = alpha
    for i in range(1, N):
        for j in range(m):
            k[j][0] = h*f[j](t[i-1], w[i])
            k[j][1] = h*f[j]((t[i-1] + h/2.0), [(w[i-1][x]+(.5*k[x][0])) for x in range(m)])
            k[j][2] = h*f[j]((t[i-1] + h/2.0), [(w[i-1][x]+(.5*k[x][1])) for x in range(m)])
            k[j][3] = h*f[j]((t[i-1] + h), [(w[i-1][x]+(k[x][2])) for x in range(m)])
            w[i][j] = w[i-1][j] + (k[j][0] + 2*k[j][1] + 2*k[j][2] + k[j][3])/6.0
            t[i] = a + i*h
    print "t = " + str(t)
    print "w = " + str(w)

def trapezoidal(a, b, N, alpha, tol, M, f, fy):
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    t[0] = a
    w[0] = alpha
    for i in range(1, N):
        k = w[i-1] + (h/2.0)*f(t[i-1], w[i-1])
        w0 = k
        j = 1
        FLAG = 0
        while(FLAG == 0):
            w[i] = w0 - ((w0 - (h/2.0)*f(t[i-1]+h, w0) - k) / (1 - (h/2.0)*fy(t[i-1]+h, w0)))
            if (math.fabs(w[i] - w0) < tol):
                FLAG = 1
            else:
                j = j + 1
                w0 = w[i]
                if (j > M):
                    return "Max iterations reached"
        t[i] = a + i*h
    print "t = " + str(t)
    print "w = " + str(w)
