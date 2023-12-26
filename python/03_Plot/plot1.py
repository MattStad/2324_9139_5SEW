import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy
import math

PI = math.pi
CNT = 1024
X = numpy.linspace(-PI, PI, CNT)
C = [math.cos(x) for x in X]
S = [math.sin(x) for x in X]

#Version 1
#plt.plot(X, C)
#plt.plot(X, S)
#plt.savefig("plot1.1_Stadlinger.png",dpi=72)
#plt.show()

#Version 2
plt.figure(figsize=(10,6), dpi=80)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

#Version 3
plt.xlim(min(X)*1.1, max(X)*1.1)
plt.ylim(min(C)*1.1, max(C)*1.1)

#Version 4
#plt.xticks( [-PI, -PI/2, 0, PI/2, PI])
#plt.yticks([-1, 0, +1])

#Version 5
plt.xticks([-PI, -PI/2, 0, PI/2, PI],
[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
[r'$-1$', r'$0$', r'$+1$'])

#Version 6
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sine")
plt.legend(loc='upper left', frameon=False)

#Version 7
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

#Version 8
t = 2*PI/3
plt.plot([t,t],[0,math.cos(t)], color ='green', linewidth=2.5, linestyle="--")
plt.scatter([t,],[math.cos(t),], 50, color ='green')
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
xy=(t, math.sin(t)), xycoords='data',
xytext=(+10, +30), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot([t,t],[0,math.sin(t)], color ='yellow', linewidth=2.5, linestyle="--")
plt.scatter([t,],[math.sin(t),], 50, color ='yellow')
plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
xy=(t, math.cos(t)), xycoords='data',
xytext=(-90, -50), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#Version 9
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))
ax.set_axisbelow(True)

#Aufgaben
#Wähle eine anderen Linienstil bzw. eine andere Linienfarbe für deine Grafik.
plt.plot(X, C, color="green", linewidth=3, linestyle="--", label="cosine")
plt.plot(X, S, color="yellow", linewidth=1, linestyle=":", label="sine")
#Markiere (zusätzlich) die Werte bei -45°.
t=PI/-2
plt.scatter([t,],[math.cos(t),], 100, color ='blue')
plt.scatter([t,],[math.sin(t),], 100, color ='red')
#Eine Titelzeile fehlt auch noch.
ax.set_title("Plot von Matthias Stadlinger, HTL3R")
#Bonus: Pfeile bei den Achsen (geht nur mit Tricks – siehe plt.annotate).
plt.annotate(r'$\cos(\frac{-pi}{2})$',
xy=(t, math.cos(t)), xycoords='data',
xytext=(-90, -50), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate(r'$\sin(\frac{-pi}{2})$',
xy=(t, math.sin(t)), xycoords='data',
xytext=(-90, -50), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
#speichere die fertige Grafik als plot1_familienname.png (kommt in git).
plt.savefig("plot1.Final_Stadlinger.png")
plt.show()