import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Define the two point sets
points_1 = np.array([
    (294,75), (317,108), (341,141), (364,174), (391,211), (416,246),
    (440,279), (399,308), (374,273), (350,239), (325,205), (300,170),
    (278,136), (253,101), (211,132), (169,161), (194,194), (269,296),
    (297,330), (357,336), (313,365), (275,398), (248,362), (227,328),
    (201,290), (177,260), (154,224), (130,190), (87,222), (112,253),
    (136,283), (160,318), (186,355), (212,393), (234,423)
])

points_2 = np.array([
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

def generate_blur(points, sigma=35):
    # Determine bounds with padding
    margin = 50
    min_x, min_y = points.min(axis=0) - margin
    max_x, max_y = points.max(axis=0) + margin

    # Create meshgrid
    res = 1
    x, y = np.meshgrid(np.arange(min_x, max_x, res), np.arange(min_y, max_y, res))

    # Generate Gaussian blur map
    blur = np.zeros_like(x, dtype=np.float64)
    for px, py in points:
        blur += 0.8 * np.exp(-((x - px)**2 + (y - py)**2) / (2 * sigma**2))

    blur -= blur.min()
    blur /= blur.max()

    # Flip vertically once to get origin at top-left
    blur = np.flipud(blur)

    # Plotting
    fig, ax = plt.subplots(figsize=(4, 4))
    levels = np.linspace(0, 1, 100)
    contour = ax.contourf(x, y, blur, levels=levels, cmap='gray_r')

    # Colorbar
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.2)
    cbar = fig.colorbar(contour, cax=cax)
    cbar.set_ticks([0, 0.3, 0.7, 1])
    cbar.ax.set_ylabel(r'$c_{ft}$', rotation=0)

    # Formatting
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)  # Normal y-limits (bottom to top)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(True)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.show()

# Generate blur maps with adjusted view bounds and different sigmas
generate_blur(points_1, sigma=17.5)
generate_blur(points_2, sigma=35)
