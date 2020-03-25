import pylab as plt
import math
xvals = []
ylin = []
yquad = []
ylog = []
ynlog = []
yexp = []

for i in range(1, 15):
    xvals.append(i)
    ylin.append(2*i)
    yquad.append(i**2)
    ylog.append(math.log(i, 10))
    ynlog.append(i*(math.log(i, 10)))
    yexp.append((math.e)**i)

plots = [ylin, yquad, ylog, ynlog]
for plot in plots:
    plt.figure("Vergleich lin,quad,log,nlog")
    plt.plot(xvals, plot)
    plt.xlabel('x-Werte')
    plt.ylabel('y-Werte')
    plt.title('Testtitle')
plt.yscale('linear')
plt.show()
