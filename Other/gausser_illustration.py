import numpy as np
import matplotlib.pyplot as plt

# Define the x-axis
x = np.linspace(-5, 5, 500)

# Define super-Gaussian function
def supergaussian(x, a, b, c, P):
    return a * np.exp(- ((x - b)**2 / 2*c**2)**P)

# Generate and plot for P = 1, 2, 3
P_values = [0.5, 1, 3]
colors = ['blue', 'green', 'red']

plt.figure(figsize=(7, 4))
for P, color in zip(P_values, colors):
    y = supergaussian(x, 1, 0, 1, P)
    plt.plot(x, y, label=f'P={P}', color=color)

plt.xlabel(r'$x$')
plt.ylabel(r'$\exp(-x^{2P})$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
