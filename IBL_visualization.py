import matplotlib.pyplot as plt
import numpy as np
import math as m

delta_ibl_0 = 100
z_0hi = 0.92
z_h = 100
s_x = 7
D = 100
x_len = 10000
x = np.arange(0, x_len)
H_G  = 1300

def ibl_visualization(delta_ibl_0, z_0hi, z_h, s, D, x_len, H_G):

    def ibl(x):
        return delta_ibl_0 + z_0hi * (x/z_0hi)**(4/5)

    ibl = ibl(x)

    for i in range(0, x_len):
        if ibl[i] >= H_G:
            ibl[i] = H_G

    p_bottom = [(i*s*D, 0) for i in range(0, m.ceil(x_len/(s*D)))]
    p_top = [(i*s*D, z_h) for i in range(0, m.ceil(x_len/(s*D)))]

    bottom_x, bottom_y = zip(*p_bottom)
    top_x, top_y = zip(*p_top)

    for (bx, by), (tx, ty) in zip(p_bottom, p_top):
        plt.plot([bx, tx], [by, ty], color='Blue', linestyle='-')

    plt.plot(x, ibl, label='IBL Height [m]', color="Green")   
    plt.xlabel('x')
    plt.ylabel('IBL')
    plt.title('IBL vs x')
    plt.legend()
    plt.show()

ibl_visualization(delta_ibl_0, z_0hi, z_h, s_x, D, x_len, H_G)