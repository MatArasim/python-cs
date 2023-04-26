import math
import matplotlib.pyplot as plt
import numpy as np

def giveNumbers(x, y, mod):
  return (y*x) % mod


x = 1
m= 4056
a = 3
k = 100
k1 = k
xn = np.array([])
while (k1 > 0):
  x = giveNumbers(x, a, m)
  print(x/m)
  xn.append(x/m)
  k1 -= 1
print(len(xn))
# for x in points:
#   plt.plot(x, linewidth=0)

fig, ax = plt.subplots()
for x in xn:
    scale = 200.0
    ax.scatter(x, s=scale)
               

ax.legend()
ax.grid(True)

plt.show()
