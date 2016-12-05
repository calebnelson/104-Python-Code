def f(x):
    return x #insert function here

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
