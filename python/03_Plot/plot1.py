import matplotlib.pyplot as plt
import numpy
import math

PI = math.pi # für besonders Tippfaule ;-)
CNT = 1024
X = [ ... for i in range(int(PI*-1),int(PI)) ] # CNT Werte von -pi ... +pi
C = [ math.cos(x) for x in X ] # CNT cosinuswerte für x von -pi ... +pi
S = [ ... ]
#In X, C und S sollten jetzt je 1024 Werte stehen. Daraus machen wir jetzt eine Grafik.
plt.plot(X, C)
plt.plot(X, S)
plt.savefig("plot1_familienname.png",dpi=72)
plt.show() # Anzeigen: Danach kann man die Grafik nicht mehr ändern!
