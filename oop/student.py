import matplotlib.pyplot as plt 
import numpy as np


students = ["Arun","Alice","Akhil","Esha","Divya"]
marks = [75,85,90,70,95]

plt.plot(students,marks,marker='o')

plt.xlabel("X axis")
plt.ylabel("Y axis")


plt.grid()
plt.show()