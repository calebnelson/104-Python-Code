# Author: Caleb Nelson
# Math 104B HW #5
# Code is currently set up to do problems 9 - 29 of section 6.2
import math

def gaussian_elim(n, A, dc):
    swap_count = 0
    for i in range(n):
        p = i
        while(A[p][i] == 0):
            if (p == n-1):
                return "no unique solutions exist"
            else:
                p += 1
        if (p != i):
            swap_count += 1
            print str(i) + " <-> " + str(p)
            temp = A[p]
            A[p] = A[i]
            A[i] = temp
        for j in range(i+1, n):
            m = ndc(A[j][i]/A[i][i], dc)
            A[j] = [ndc(a, dc) for a in [A[j][k] - [m*a for a in A[i]][k] for k in range(len(A[j]))]]
    if (A[n-1][n-1] == 0):
        return "no unique solutions exist"
    x = [0.0 for i in range(n)]
    x[n-1] = ndc(A[n-1][n]/A[n-1][n-1], dc)
    for i in reversed(range(n-1)):
        x[i] = ndc((A[i][n] - sum([A[i][j]*x[j] for j in range(i+1, n)])) / A[i][i], dc)
    print str(swap_count) + " row interchanges performed"
    return x

def gauss_jordan(n, A, dc):
    swap_count = 0
    for i in range(n):
        p = i
        while(A[p][i] == 0):
            if (p == n-1):
                return "no unique solutions exist"
            else:
                p += 1
        if (p != i):
            swap_count += 1
            print str(i) + " <-> " + str(p)
            temp = A[p]
            A[p] = A[i]
            A[i] = temp
        for j in range(n):
            if(j != i):
                m = ndc(A[j][i]/A[i][i], dc)
                A[j] = [ndc(a, dc) for a in [A[j][k] - m*A[i][k] for k in range(len(A[j]))]]
    if (A[n-1][n-1] == 0):
        return "no unique solutions exist"
    x = [0.0 for i in range(n)]
    for i in range(n):
        x[i] = ndc(A[i][n]/A[i][i], dc)
    print str(swap_count) + " row interchanges performed"
    return x

def gaussian_ppivot(n, A, dc):
    swap_count = 0
    nrow = range(n)
    for i in range(n):
        p = i
        for j in range(i, n):
            if (A[nrow[j]][i] > A[nrow[p]][i]):
                p = j
        if (A[nrow[p]][i] == 0):
            return "no unique solutions exist"
        if(nrow[p] != nrow[i]):
            swap_count += 1
            print str(nrow[i]) + " <-> " + str(nrow[p])
            temp = nrow[p]
            nrow[p] = nrow[i]
            nrow[i] = temp
        for j in range(i+1, n):
            m = ndc(A[nrow[j]][i]/A[nrow[i]][i], dc)
            A[nrow[j]] = [ndc(a, dc) for a in [A[nrow[j]][k] - m*A[nrow[i]][k] for k in range(len(A[j]))]]
    if (A[nrow[n-1]][n-1] == 0):
        return "no unique solutions exist"
    x = [0.0 for i in range(n)]
    x[n-1] = ndc(A[nrow[n-1]][n]/A[nrow[n-1]][n-1], dc)
    for i in reversed(range(n)):
        x[i] = ndc((A[nrow[i]][n] - sum([A[nrow[i]][j]*x[j] for j in range(i+1, n)])) / A[nrow[i]][i], dc)
    print str(swap_count) + " row interchanges performed"
    return x

def gaussian_sppivot(n, A, dc):
    swap_count = 0
    nrow = range(n)
    s = [None for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (A[i][j] > s[i]):
                s[i] = A[i][j]
        if (s[i] == 0):
            return "no unique solutions exist"
    for i in range(n):
        p = i
        for j in range(i, n):
            if (A[nrow[j]][i]/s[nrow[j]] > A[nrow[p]][i]/s[nrow[j]]):
                p = j
        if (A[nrow[p]][i] == 0):
            return "no unique solutions exist"
        if(nrow[p] != nrow[i]):
            swap_count += 1
            print str(nrow[i]) + " <-> " + str(nrow[p])
            temp = nrow[p]
            nrow[p] = nrow[i]
            nrow[i] = temp
        for j in range(i+1, n):
            m = ndr(A[nrow[j]][i]/A[nrow[i]][i], dc)
            A[nrow[j]] = [ndr(a, dc) for a in [A[nrow[j]][k] - m*A[nrow[i]][k] for k in range(len(A[j]))]]
    if (A[nrow[n-1]][n-1] == 0):
        return "no unique solutions exist"
    x = [0.0 for i in range(n)]
    x[n-1] = ndr(A[nrow[n-1]][n]/A[nrow[n-1]][n-1], dc)
    for i in reversed(range(n)):
        x[i] = ndr((A[nrow[i]][n] - sum([A[nrow[i]][j]*x[j] for j in range(i+1, n)])) / A[nrow[i]][i], dc)
    print str(swap_count) + " row interchanges performed"
    return x

def gaussian_cpivot(n, A, dc):
    swap_count_r = 0
    swap_count_c = 0
    nrow = range(n)
    ncol = range(n+1)
    for i in range(n):
        s = None
        srow = None
        scol = None
        for j in range(i, n):
            for k in range(i, n):
                if (A[j][k] > s):
                    s = A[j][k]
                    srow = j
                    scol = k
        if (s == 0):
            return "no unique solutions exist"
        if(nrow[srow] != nrow[i]):
            swap_count_r += 1
            print "row swap: " + str(nrow[i]) + " <-> " + str(nrow[srow])
            temp = nrow[srow]
            nrow[srow] = nrow[i]
            nrow[i] = temp
        if(ncol[scol] != ncol[i]):
            swap_count_c += 1
            print "col swap: " + str(ncol[i]) + " <-> " + str(nrow[scol])
            temp = nrow[scol]
            nrow[scol] = nrow[i]
            nrow[i] = temp
        for j in range(i+1, n):
            m = ndr(A[nrow[j]][ncol[i]]/A[nrow[i]][ncol[i]], dc)
            A[nrow[j]] = [ndr(a, dc) for a in [A[nrow[j]][ncol[k]] - m*A[nrow[i]][ncol[k]] for k in range(len(A[j]))]]
    if (A[nrow[n-1]][ncol[n-1]] == 0):
        return "no unique solutions exist"
    x = [0.0 for i in range(n)]
    x[n-1] = ndr(A[nrow[n-1]][ncol[n]]/A[nrow[n-1]][ncol[n-1]], dc)
    for i in reversed(range(n)):
        x[i] = ndr((A[nrow[i]][ncol[n]] - sum([A[nrow[i]][ncol[j]]*x[j] for j in range(i+1, n)])) / A[nrow[i]][i], dc)
    print str(swap_count_r) + " row interchanges performed"
    print str(swap_count_c) + " col interchanges performed"
    return x

#n-digit chopping
def ndc(x, n):
    if (n == 0):
        return x
    neg = (x < 0)
    if (neg):
        x *= -1
    x = float(str("%.3e" % x)[:n+1] + str("%.3e" % x)[n+2:]) #evil evil code
    if (neg):
        x *= -1
    return x

#n-digit rounding
def ndr(x, n):
    if (n == 0):
        return x
    return float(("%." + str(n-1) + "e") % x)
