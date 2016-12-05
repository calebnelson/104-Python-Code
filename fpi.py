import math
def f(x):
    return 0.5*(math.sin(x) + math.cos(x)) #insert function here

def fixedpoint(p, tol, n):
    if (n > 900):
        print p
        return "Error: Calculation took too long"
    fp = f(p)
    if (abs(fp - p) < tol):
        print n
        return p
    else:
        return fixedpoint(fp, tol, n+1)
    return "Unknown Error"
