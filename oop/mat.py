import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10,20,70,200])
ypoints = np.array([20,30,150,200])

plt.plot(xpoints,ypoints,marker='0')

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("simple line plot")

plt.grid()
plt.show()