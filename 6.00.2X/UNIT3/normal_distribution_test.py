import random
import matplotlib.pyplot as plt
dist = []
for i in range(1000000):
    dist.append(random.gauss(0, 30))

plt.hist(dist, 200)
plt.show()
