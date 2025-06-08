import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Define the list of points (x, y)
points = np.array([
    (526,127), (578,115), (580,182), (586,238), (603,293), (635,353),
    (628,99), (657,128), (679,165), (697,195), (720,229), (739,265),
    (763,298), (763,340), (761,379), (761,415), (762,456), (727,484),
    (686,505), (648,519), (643,458), (673,408), (587,461), (522,336),
    (522,336), (545,389), (503,272), (484,186), (459,218), (434,252),
    (410,285), (448,338), (490,426), (537,489), (374,336), (350,366),
    (324,399), (390,418), (427,487), (472,545), (302,430), (278,459),
    (263,493), (246,531), (339,498), (377,577), (311,568), (233,569),
    (438,595), (504,590), (556,558), (490,689), (562,699), (548,759),
    (505,757), (455,763), (406,766), (420,679), (359,725), (280,765),
    (228,785), (185,790), (344,669), (344,669), (273,663), (272,710),
    (198,648), (180,686), (166,725), (151,761), (140,791)
])

# Create a grid covering the full area of points
x_range = (0, 900)
y_range = (0, 900)
res = 1  # resolution in pixels

x = np.arange(x_range[0], x_range[1], res)
y = np.arange(y_range[0], y_range[1], res)
x, y = np.meshgrid(x, y)

# Parameters for the Gaussian blur
sigma = 35  # standard deviation in pixels
blur = np.zeros_like(x, dtype=np.float64)

# Add a Gaussian at each point
for px, py in points:
    blur += np.exp(-((x - px)**2 + (y - py)**2) / (2 * sigma**2))

# Normalize and optionally flip
blur -= blur.min()
blur /= blur.max()
blur = np.flipud(blur)

# Plot with matched colorbar height
fig, ax = plt.subplots(figsize=(6, 6))
levels = np.linspace(0, 1, 100)
contour = ax.contourf(x, y, blur, levels=levels, cmap='gray_r')

# Match colorbar height using make_axes_locatable
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.2)  # Adjust size and padding here
cbar = fig.colorbar(contour, cax=cax)
cbar.set_ticks([0, 0.3, 0.7, 1])
cbar.ax.set_ylabel(r'$c_{ft}$', rotation=0)

# Hide tick labels and ticks, but keep the box
ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])
for spine in ax.spines.values():
    spine.set_visible(True)

ax.set_aspect('equal')
plt.tight_layout()
plt.show()