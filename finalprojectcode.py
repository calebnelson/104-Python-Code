import math
def f(x):
    x = x * 1.0 #force x to be a float
    return x #insert function here

def fp(x):
    x = x * 1.0 #force x to be a float
    return x #insert derivative here

#Function returns estimation of f'(x) where y1 = f(x)
def tpef(y1, y2, y3, h):
    #y1 is f(x)
    #y2 is f(x+h)
    #y3 is f(x+2h)
    return (1/(2*h)*(-3*y1+4*y2-y3))

#Function returns estimation of f'(x)
def tpmf(y1, y2, h):
    #y1 is f(x-h)
    #y2 is f(x+h)
    return (1/(2*h)*(y1-y2))

#Function returns estimation of f'(x) where y1 = f(x)
def fpef(y1, y2, y3, y4, y5, h):
    #y1 is f(x)
    #y2 is f(x+h)
    #y3 is f(x+2h)
    #y4 is f(x+3h)
    #y5 is f(x+4h)
    return (1/(12*h)*(-25*y1+48*y2-36*y3+16*y4-3*y5))

#Function returns estimation of f'(x)
def fpmf(y1, y2, y3, y4, h):
    #y1 is f(x-2h)
    #y2 is f(x-h)
    #y3 is f(x+h)
    #y4 is f(x+2h)
    return (1/(12*h)*(y1-8*y2+8*y3-y4))

#Remember to set f(x) before you use this function
#Function returns root of f(x)
def bisection(a, b, tol, n):
    if (n > 900):
        return "Error: Calculation took too long"
    if (a > b):
        c = b
        b = a
        a = c
    p = (a + b) / 2.0
    fp = f(p)
    if (abs(fp) < tol):
        return p
    else:
        if ((f(a) * fp) < 0):
            return (bisection(a, p, tol, n+1))
        else:
            return (bisection(p, b, tol, n+1))
    return "Unknown Error"

#Remember to set f(x) AND fp(x) before you use this function
#Function returns root of f(x)
def newton(p0, tol, n):
    i = 1
    while (i <= n):
        p = p0 - (f(p0)/fp(p0))
        if (abs(p - p0) < tol):
            return p
        i = i + 1
        p0 = p
    print p
    return "The method failed after " + str(n) + " iterations"

#Remember to set f(x) before you use this function
#Function returns root of f(x)
def secant(p0, p1, tol, n):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while (i <= n):
        p = p1 - ((q1*(p1 - p0))/(q1 - q0))
        if (abs(p - p0) < tol):
            print i
            return p
        i = i + 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    print p
    return "The method failed after " + str(n) + " iterations"

#Returns interpolating forumla estimation of f(x)
#The function returns the entire two dimensional polynomial,
#but the coefficients of the interpolating polynomial are the
#diagonals of f, or f[0,0], f[1,1], and so on.
def divdiff(x, y):
    n = len(x) - 1
    f = [[0.0 for i in range(len(y))] for j in range(len(y))]
    for i in range(len(y)):
        f[i][0] = y[i]
    for i in range(1, n+1):
        for j in range(1, i+1):
            f[i][j] = ((f[i][j-1] - f[i-1][j-1])/(x[i] - x[i-j]))
    return f
