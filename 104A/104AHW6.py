import math

def hermite(x, y, d):
    n = len(x)
    z = [val for val in x for _ in (0, 1)]
    q = [[0.0 for i in 2*range(len(y))] for j in 2*range(len(y))]
    for i in range(n):
        z[2*i] = x[i]
        z[(2*i)+1] = x[i]
        q[2*i][0] = y[i]
        q[(2*i)+1][0] = y[i]
        q[(2*i)+1][1] = d[i]
        if (i > 0):
            q[2*i][1] = (q[2*i][0] - q[(2*1)-1][0])/(z[2*i] - z[(2*i)-1])
    for i in range(2, 2*n):
        for j in range(2, i+1):
            q[i][j] = (q[i][j-1] - q[i-1][j-1])/(z[i] - z[i-j])
    return q
        
def nspline(n, x, a):
    h = [0.0 for i in range(len(x))]
    alpha = [0.0 for i in range(len(a))]
    for i in range(n):
        h[i] = x[i+1] - x[i]
    for i in range(1, n):
        alpha[i] = 3/h[i] * (a[i+1] - a[i]) - 3/h[i-1] * (a[i] - a[i-1])
    l = [0.0 for i in range(len(x))]
    l[0] = 1
    m = [0.0 for i in range(len(x))]
    z = [0.0 for i in range(len(x))]
    for i in range(1, n):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*m[i-1]
        m[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]
    l[n] = 1
    z[n] = 0
    c = [0.0 for i in range(len(x))]
    b = [0.0 for i in range(len(x))]
    d = [0.0 for i in range(len(x))]
    for j in reversed(range(n)):
        c[j] = z[j] - m[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/h[j] - (h[j]*(c[j+1] + 2*c[j]))/3
        d[j] = (c[j+1] - c[j])/(3*h[j])
    output = [a, b, c, d]
    return output

def cspline(n, x, a, FPO, FPN):
    h = [0.0 for i in range(len(x))]
    alpha = [0.0 for i in range(len(a))]
    for i in range(n):
        h[i] = x[i+1] - x[i]
    alpha[0] = 3*(a[1] - a[0])/(h[0] - 3*FPO)
    alpha[n] = 3*FPN - 3*(a[n] - a[n-1])/h[n-1]
    for i in range(1, n):
        alpha[i] = 3/h[i] * (a[i+1] - a[i]) - 3/h[i-1] * (a[i] - a[i-1])
    l = [0.0 for i in range(len(x))]
    l[0] = 2*h[0]
    m = [0.0 for i in range(len(x))]
    m[0] = 0.5
    z = [0.0 for i in range(len(x))]
    z[0] = alpha[0]/l[0]
    for i in range(1, n):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*m[i-1]
        m[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]
    l[n] = h[n-1]*(2 - m[n-1])
    z[n] = (alpha[n] - h[n-1]*z[n-1])/l[n]
    c = [0.0 for i in range(len(x))]
    b = [0.0 for i in range(len(x))]
    d = [0.0 for i in range(len(x))]
    c[n] = z[n]
    for j in reversed(range(n)):
        c[j] = z[j] - m[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/h[j] - (h[j]*(c[j+1] + 2*c[j]))/3
        d[j] = (c[j+1] - c[j])/(3*h[j])
    output = [a, b, c, d]
    return output

def bezier(n, x, y, xpos, ypos, xneg, yneg):
    a0 = [0.0 for i in range(n)]
    a1 = [0.0 for i in range(n)]
    a2 = [0.0 for i in range(n)]
    a3 = [0.0 for i in range(n)]
    b0 = [0.0 for i in range(n)]
    b1 = [0.0 for i in range(n)]
    b2 = [0.0 for i in range(n)]
    b3 = [0.0 for i in range(n)]
    for i in range(n):
        a0[i] = x[i]
        b0[i] = y[i]
        a1[i] = 3*(xpos[i] - x[i])
        b1[i] = 3*(ypos[i] - y[i])
        a2[i] = 3*(x[i] + xneg[i+1] - 2xpos[i])
        b2[i] = 3*(y[i] + yneg[i+1] - 2ypos[i])
        a3[i] = x[i+1] - x[i] + 3*xpos[i] - 3*xneg[i+1]
        b3[i] = y[i+1] - y[i] + 3*ypos[i] - 3*yneg[i+1]
    print "a0 = " + str(a0)
    print "a1 = " + str(a1)
    print "a2 = " + str(a2)
    print "a3 = " + str(a3)
    print "b0 = " + str(b0)
    print "b1 = " + str(b1)
    print "b2 = " + str(b2)
    print "b3 = " + str(b3)
    return [a0, a1, a2, a3, b0, b1, b2, b3]
