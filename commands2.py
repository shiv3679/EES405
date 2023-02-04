import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0,10,1000)

y = np.sin(x)

plt.plot(x,y,'r.')
plt.xlabel('Data Points')
plt.ylabel('Sin(x)')
plt.show()
