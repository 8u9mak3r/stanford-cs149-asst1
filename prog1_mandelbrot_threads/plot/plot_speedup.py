import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y1 = np.array([1.00, 1.97, 1.60, 2.39, 2.42, 3.10, 3.22, 3.46])
y2 = np.array([1.01, 1.67, 2.17, 2.54, 2.86, 3.26, 3.56, 3.58])

plt.plot(x, y1,
         color="red",
         linestyle="-",
         linewidth=2,
         marker="o",
         markersize=6,
         alpha=0.7,
         label="View 1"
         )

plt.plot(x, y2,
         color="blue",
         linestyle="-",
         linewidth=2,
         marker="*",
         markersize=6,
         alpha=0.7,
         label="View 2"
         )

plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.legend()
plt.savefig(fname="image/1.png")
plt.show()