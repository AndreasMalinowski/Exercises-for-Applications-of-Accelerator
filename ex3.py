import numpy  as np
import matplotlib.pyplot as plt


data = np.loadtxt('ex3.txt')
def maximum(data):
    np.fmax(data)
    
    return
plt.rcParams.update({
    "lines.color": "lightblue",
    "patch.edgecolor": "white",
    "text.color": "black",
    "axes.facecolor": "black",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "black",
    "figure.facecolor": "black",
    "figure.edgecolor": "blue",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})
print(maximum)

plt.plot(data)
plt.scatter(578,30.8193,c= 'red')
plt.savefig('testplot.png')
plt.show()