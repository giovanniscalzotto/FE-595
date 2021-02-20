
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.xlim(0, 10)
plt.ylim(-1.1, 1.1)
plt.xlabel('x from 0 to 2*pi', fontsize = 12)
plt.ylabel('Sin and Cos', fontsize = 12)
plt.legend(['Sin', 'Cos'], loc = "upper right", frameon = False, fontsize = 10)
plt.title('Assignment 1', loc='left', fontsize = 20)
plt.show()