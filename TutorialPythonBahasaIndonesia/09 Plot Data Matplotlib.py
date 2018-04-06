#import package yang dibutuhkan
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y1 = np.array([1,2,3,4,5])
y2 = x**2

plt.plot(x, y1, label='data linear')
plt.scatter(x, y1, marker='*', s=100, c='red')
plt.plot(x, y2, c='green', label='data kuadrat')
plt.legend()
plt.title("Belajar plotting matplotlib")
plt.xlabel("nilai x")
plt.ylabel("nilai y")
plt.show()