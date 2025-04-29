import numpy as np
import matplotlib.pyplot as plt


def CtDRV(n):
    r1 = np.random.uniform(0, 1, n)
    r2 = np.random.uniform(0, 1, n)

    x = -1 / 2 * np.log(1 - r1)
    y = -1 / 3 * np.log(1 - r2)

    return x, y


n = 10000
x, y = CtDRV(n)


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(x, bins=50, density=True, alpha=0.6, color='red')
plt.title('Гистограмма для X')
plt.xlabel('x')
plt.ylabel('Плотность')

plt.subplot(1, 2, 2)
plt.hist(y, bins=50, density=True, alpha=0.6, color='green')
plt.title('Гистограмма для Y')
plt.xlabel('y')
plt.ylabel('Плотность')

plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.1, color='magenta')
plt.title('Двумерное распределение (X, Y)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
