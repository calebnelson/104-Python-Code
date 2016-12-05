import math

def neville(x, xlist, y):
    n = len(xlist) - 1
    q = [[0.0 for i in range(len(y))] for j in range(len(y))]
    for i in range(len(y)):
        q[i][0] = y[i]
    for i in range(1, n+1):
        for j in range(1, i+1):
            q[i][j] = ((((x - xlist[i-j])*q[i][j-1]) - (x - xlist[i])*q[i-1][j-1]) / (xlist[i] - xlist[i-j]))
    return q

def divdiff(x, y):
    n = len(x) - 1
    f = [[0.0 for i in range(len(y))] for j in range(len(y))]
    for i in range(len(y)):
        f[i][0] = y[i]
    for i in range(1, n+1):
        for j in range(1, i+1):
            f[i][j] = ((f[i][j-1] - f[i-1][j-1])/(x[i] - x[i-j]))
    return f
