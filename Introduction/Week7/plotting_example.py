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
plotnames = ['lin', 'quad', 'log', 'nlog']
i = 0
for plot in plots:
    plt.figure(1)
    plt.plot(xvals, plot, label=str(plotnames[i]))
    plt.xlabel('x-Werte')
    plt.ylabel('y-Werte')
    plt.title('Test')
    plt.legend(loc='upper right')
    i += 1
    plt.ylim(0, 20)
plt.yscale('linear')
plt.show()
