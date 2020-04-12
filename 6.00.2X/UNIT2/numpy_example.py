import numpy as np

a = np.zeros(10, dtype=int)
a.shape = (2, 5)
a[1, 3] = 1


unique, counts = np.unique(a, return_counts=True)

print(unique, counts)
if 0 in unique:
    print("return 1 1")
else:
    print("0 0")
