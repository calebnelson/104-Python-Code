import math
def f(t, y):
    return (math.e**(-0.06*math.pi*t) * ((-1.29238)*math.cos(2*t) + (0.735745*math.sin(2*t)))) #insert y' function here

def euler(a, b, N, alpha):
    h = (b - a)/(N - 1)
    t = [0.0 for i in range(N)]
    w = [0.0 for i in range(N)]
    t[0] = a
    w[0] = alpha
    for i in range(1, N):
        w[i] = w[i-1] + h * f(t[i-1], w[i-1])
        t[i] = a + i*h
    return [t, w]

# [0.0, -0.12923800000000002, -0.23919063269544477, -0.3262314550650922, -0.3877725470218083, -0.42232823685050164, -0.4295329620274547, -0.4101142573042067, -0.36582359641794976, -0.2993293764856133, -0.21407766972467523, -0.1141274313056723, -0.003967612917711777, 0.1116759297851951, 0.22803573668377075, 0.34049245930349015, 0.44475171180361983, 0.5370015523190248, 0.6140450953198231, 0.6734039407206416, 0.7133894169824551, 0.7331400169608799, 0.7326247996458012, 0.7126138826936714, 0.6746184079977933, 0.6208034793376548, 0.5538785085146987, 0.47697013395830434, 0.3934833726156913, 0.3069569209494916, 0.22091853293806718, 0.13874618061787458, 0.06354026337411967, -0.0019884987558710793, -0.055611643059722084, -0.09565308176451359, -0.12103482264375202, -0.13129739059908233, -0.126595080151426, -0.10766715742046956, -0.07578703808692491, -0.0326922621690694, 0.01950125994750549, 0.07839676350222237, 0.14142162314764814, 0.2059354036553907, 0.26933658956260337, 0.329163829899133, 0.383187904682872, 0.4294911264353073, 0.4665315075236835, 0.4931897241987312, 0.5087976600827409, 0.51314808397681, 0.506485777973778, 0.4894811523493878, 0.46318803662345676, 0.4289878982636734, 0.3885231929218828, 0.34362287904625016, 0.29622332678617314, 0.24828791340075093, 0.20172852742369346, 0.15833200928204538, 0.11969424920211161, 0.08716426033086824, 0.06180006551130447, 0.04433770183497797, 0.035174081072979764, 0.03436386987207299, 0.04162999416395723, 0.05638684910742372, 0.07777482837064294, 0.10470439105956973, 0.13590757405509823, 0.16999464105041812, 0.20551344224495094, 0.24100904141584686, 0.27508124692917896, 0.3064378534276907, 0.33394165138114695, 0.356649579553567, 0.3738427656879451, 0.38504660678161506, 0.3900404648705882, 0.38885697981828493, 0.38177141037692786, 0.3692817931689899, 0.3520810424479538, 0.3310223900610637, 0.3070797761313202, 0.28130494069172995, 0.2547830319678587, 0.22858853837831128, 0.2037432716884816, 0.1811779838811315, 0.16169899832993662, 0.14596098686410078, 0.13444673986135308, 0.12745446914234693, 0.12509286614141427]
