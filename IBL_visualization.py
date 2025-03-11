import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerTuple
import numpy as np
import math as m

delta_ibl_0 = 70
z_0hi = 0.68
z_h = 70
s_x = 7
D = 80
x_len = 10000/z_0hi
x = np.arange(0, x_len, x_len)
H_G  = 1300

def ibl_visualization(delta_ibl_0, z_0hi, z_h, s, D, x_len, H_G):
    def ibl(x):
        return delta_ibl_0 + z_0hi * (x / z_0hi) ** (4 / 5)

    ibl = ibl(x)
    ibl[ibl >= H_G] = H_G  # Limit IBL height

    
    # Define turbine positions
    p_bottom = [(i * s * D, 0) for i in range(0, m.ceil(x_len / (s * D)))]
    p_top = [(i * s * D, z_h) for i in range(0, m.ceil(x_len / (s * D)))]

    fig, ax = plt.subplots()

    # Store turbine plot handles
    turbine_plots = []

    # Plot turbines and store handles
    for (bx, by), (tx, ty) in zip(p_bottom, p_top):
        line, = ax.plot([bx, tx], [by, ty], color='Blue', linestyle='-')  
        turbine_plots.append(line)
    
    
    # Plot IBL height and store its handle
    ibl_plot, = ax.plot(x, ibl, label='IBL height [m]', color="Green")

    # Set labels and title
    ax.set_xlabel('Downstream distance [m]')
    ax.set_ylabel('Height [m]')
    ax.set_title('\nIBL height as a function of downstream distance\n', wrap=True)

    # Annotation
    plt.figtext(0.525, 0.825, "z = H*_G")

    # Single legend entry for turbines + IBL height
    ax.legend(
        [tuple(turbine_plots), ibl_plot],  # Handles
        ["Turbines", "IBL height [m]"],  # Labels
        handler_map={tuple: HandlerTuple()}
    )
    plt.grid(True)
    plt.show()

ibl_visualization(delta_ibl_0, z_0hi, z_h, s_x, D, x_len, H_G)
