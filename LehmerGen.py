import math
import matplotlib.pyplot as plt


def giveNumbers(x, y, mod):
  x= (x*y) % mod
  return x


x = 1
m= 4096
a = 3
k = 100
k1 = k
xn = []

while (k1 > 0):
  x = giveNumbers(x, a, m)
  print(x/m)
  xn.append(x/m)
  k1 -= 1


y =0
fig, ax = plt.subplots()
for x in xn:
    scale = 200.0
    ax.scatter(y, x)
    y = y + 1
               
ax.set_xlabel('Quantity', fontsize=15)
ax.set_ylabel('Generated number', fontsize=15)
plt.show()
