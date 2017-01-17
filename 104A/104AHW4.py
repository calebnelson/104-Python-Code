#Author: Caleb Nelson
#Math 104A HW4
import math
def f(x):
    x = x * 1.0 #force x to be a float
    return x #insert function here

def fp(x):
    x = x * 1.0 #force x to be a float
    return x #insert derivative here

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

def falsepos(p0, p1, tol, n):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    while (i <= n):
        p = p1 - ((q1*(p1 - p0))/(q1 - q0))
        if (abs(p - p0) < tol):
            print i
            return p
        i = i + 1
        q = f(p)
        if ((q * q1) < 0):
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    print p
    return "The method failed after " + str(n) + " iterations"

def muller(p0, p1, p2, tol, n):
    h1 = p1 - p0
    h2 = p2 - p1
    d1 = (f(p1) - f(p0))/h1
    d2 = (f(p2) - f(p1))/h2
    d = (d2 - d1)/(h1 + h2)
    i = 3
    while (i < n):
        b = d2 + h2*d
        dd = math.sqrt((b**2 - 4*f(p2)*d))
        if (abs(b - dd) < abs(b + dd)):
            E = b + dd
        else:
            E = b - dd
        h = -2*f(p2)/E
        p = p2 + h
        if (h < tol):
            return p
        p0 = p1
        p1 = p2
        p2 = p
        h1 = p1 - p0
        h2 = p2 - p1
        d1 = (f(p1) - f(p0))/h1
        d2 = (f(p2) - f(p1))/h2
        d = (d2 - d1)/(h1 + h2)
        i = i + 1
    print p
    return "The method failed after " + str(n) + " iterations"

#Only used in problem 34 of 2.3
def thirtyfour(x):
    if (x > 2 * math.pi):
        x = math.radians(x)
    l = 89
    h = 49
    D = 30
    b1 = 11.5
    A = l*math.sin(math.radians(b1))
    B = l*math.cos(math.radians(b1))
    C = (h + 0.5*D)*math.sin(math.radians(b1)) - 0.5*D*math.tan(math.radians(b1))
    E = (h + 0.5*D)*math.cos(math.radians(b1)) - 0.5*D
    return (A*math.sin(x)*math.cos(x) + B*math.sin(x)**2 - C*math.cos(x) - E*math.sin(x))

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
