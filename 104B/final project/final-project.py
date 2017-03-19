import math
import matplotlib.pyplot as plt

startingwater=11e9 #in gallons
startingfood=1600.0*(200000) #in pounds
startingpopA=5 #people
startingpopB=15 #people
foodAccessA = .6 #percentange of total food given to city A
foodAccessB = .4 #percentage of total food given to city B
waterAccessA = .7 #percentange of total water given to city A
waterAccessB = .3 #percentange of total water given to city B
r=.021 #human growth rate
r2=.70 #cow growth rate
W = 1.14e9 #rainfall per year (in gallons)

#PA returns the rate of population increase/decrease
def PA(Pa,Pb,Cd,Ce,t):
    return((Pa+alphaA(Pa,Pb,Cd,Ce,t))*r*math.e**(r))

#PAtw returns the PA function compatable with the Runge-Kutta systems of equations function
def PAtw(t, w):
    return PA(w[0], w[1], w[2], w[3], t)

#PB returns the rate of population increase/decrease
def PB(Pa,Pb,Cd,Ce,t):
    return((Pb-alphaA(Pa,Pb,Cd,Ce,t))*r*math.e**(r))

#PBtw returns the PB function compatable with the Runge-Kutta systems of equations function
def PBtw(t, w):
    return PB(w[0], w[1], w[2], w[3], t)

#CD returns the rate of water intake/consumption
def CD(Pa,Pb,Cd,Ce,t):
    return( W-(365.0*20.0*(Pa+Pb)+Ce*(15.0*365.0/1600.0)))

#CDtw returns the CD function compatable with the Runge-Kutta systems of equations function
def CDtw(t, w):
    return CD(w[0], w[1], w[2], w[3], t)

#Ce returns the rate of food production/consumption
def CE(Pa,Pb,Cd,Ce,t):
    return( (r2*Ce/1600.0*math.e**(r2))-(5.0*365.0*(Pa+Pb)))
    
#CEtw returns the CE function compatable with the Runge-Kutta systems of equations function
def CEtw(t, w):
    return CE(w[0], w[1], w[2], w[3], t)

#alphaA returns the amount of people migrating from city B to city A. If alphaA<0 then people are migrating from city A to city B.
def alphaA(Pa,Pb,Cd,Ce,t):
    aCd = waterAccessA
    aCe = foodAccessA
    bCd = waterAccessB
    bCe = foodAccessB    
    return(((aCd+aCe)*(Pb)-(bCd+bCe)*(Pa))/2.0)
         
def runge_kutta(a, b, m, N, alpha, f):
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [[0.0 for i in range(m)] for i in range(N)]
    k = [[0.0 for i in range(4)] for i in range(m)]
    t[0] = a
    w[0] = alpha
    flag=0
    PopA=[]
    PopB=[]
    water=[]
    food=[]
    for i in range(1, N):
        for j in range(m):
            k[j][0] = h*f[j](t[i-1], w[i])
            k[j][1] = h*f[j]((t[i-1] + h/2.0), [(w[i-1][x]+(.5*k[x][0])) for x in range(m)])
            k[j][2] = h*f[j]((t[i-1] + h/2.0), [(w[i-1][x]+(.5*k[x][1])) for x in range(m)])
            k[j][3] = h*f[j]((t[i-1] + h), [(w[i-1][x]+(k[x][2])) for x in range(m)])
            w[i][j] = w[i-1][j] + (k[j][0] + 2*k[j][1] + 2*k[j][2] + k[j][3])/6.0
            if (w[i][j] < 0):
                flag+=1
                if(j == 0 or j== 3):
                    print("End of Simulation: Cows extinct")
                    break
                if(j == 1 or j==2):
                    print("End of Simulation: All water consumed")
                    break
            t[i] = a + i*h
            var=i-1
        if flag!=0:
            break
        print('t: '+str(t[i]) + ' Pop A : '+str(w[i][0])+ ' Pop B: '+str(w[i][1])+ ' Water is: '+str(w[i][2])+' Food is '+str(w[i][3]/1600.0))
    for x in range(1,var+1):
        PopA.append(w[x][0])
        PopB.append(w[x][1])
        water.append(w[x][2])
        food.append(w[x][3])
    plt.figure('Population vs Time')
    plt.title('Population vs Time')
    plt.plot(t[0:var],PopA)
    plt.plot(t[0:var],PopB)
    plt.xlabel('Time (years)')
    plt.ylabel('Population')
    plt.figure('Water vs Time')
    plt.title('Water vs Time')
    plt.plot(t[0:var],water)
    plt.xlabel('Time (years)')
    plt.ylabel('Water (gallons)')
    plt.figure('Food vs Time')
    plt.title('Food vs Time')
    plt.plot(t[0:var],food)
    plt.xlabel('Time (years)')
    plt.ylabel('Food (pounds)')        
    plt.show()
            
f = [PAtw, PBtw, CDtw, CEtw]
alpha = [startingpopA, startingpopB, startingwater, startingfood] #initial conditions
runge_kutta(0.0, 1000.0, 4, 1001, alpha, f)
