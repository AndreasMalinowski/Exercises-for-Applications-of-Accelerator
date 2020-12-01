
import numpy as np
import matplotlib.pyplot as plt
T = np.arange(0.0, 3.1, 0.1)
#gamma=((T*1000)/mo)+1
#delta_E=88.5*T^4 / rho
rho=561.6
mo=0.511
X=[]
Y=[]
for x in T:
    gamma=((x*1000)/mo)+1
    delta_E=88.5*x**4 / rho
    X.append(gamma)
    Y.append(delta_E)


plt.xlabel("Energy of particle in MeV")
plt.ylabel("Synchrotron-Radiation in MeV")
plt.title("Loss of Energy due to Synchrotron Radiation")
plt.grid(color='k')
plt.plot(X,Y)

plt.savefig('synchrotron-radiation.png')
plt.show()