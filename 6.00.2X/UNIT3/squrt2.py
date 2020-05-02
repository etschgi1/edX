import math
import random


def test2(num):
    """Estimates Squrt od 2 using num trails"""
    right = 0
    for t in range(num):
        x = random.random()
        if (1+x)**2 <= 2.0:
            right += 1
    return 1+(float(right)/num)


sol = test2(10000000)
print("The sqrt of 2 based on calculation is : %.5f, actual"
      "number is %.5f" % (sol, math.sqrt(2)))
