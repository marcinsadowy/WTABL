import numpy as np
import matplotlib.pyplot as plt

# Create a grid of (x, y) values
x = np.linspace(-3, 3, 1000)
y = np.linspace(-3, 3, 1000)
x, y = np.meshgrid(x, y)

# Define a 2D Gaussian function
sigma = 1.0
mu = 0.0
gaussian = np.exp(-((x - mu)**2 + (y - mu)**2) / (2 * sigma**2))
gaussian /= 2 * np.pi * sigma**2  # Normalized Gaussian

# Normalize to [0, 1]
gaussian -= gaussian.min()
gaussian /= gaussian.max()

# Define contour levels from 0 to 1 with many steps for smoothness
levels = np.linspace(0, 1, 100)

# Plot the Gaussian kernel
fig, ax = plt.subplots(figsize=(6, 5))
contour = ax.contourf(x, y, gaussian, levels=levels, cmap='Grays')

cbar = fig.colorbar(contour, ax=ax)
cbar.set_ticks([0, 0.3, 0.7, 1])
cbar.ax.set_ylabel(r'$c_{ft}$', rotation=0)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.tight_layout()
plt.show()
