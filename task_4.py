import numpy as np
import matplotlib.pyplot as plt

plt.title("Graph y(x)=cos(x); y(x)=cos(3x).")
x = np.arange(-5, 5, 0.01)
plt.axis('equal')
plt.plot(x, np.cos(3 * x), "c")
plt.plot(x, np.cos(x), "r")
plt.grid(True)
plt.show()
