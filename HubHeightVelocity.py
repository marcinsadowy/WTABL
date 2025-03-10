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

def U_cT(x, x_len, delta_ibl_0, z_0hi, u_star, k, z_0lo, beta, H_G):
    x = np.arange(0, x_len)
    ibl_x = delta_ibl_0 + z_0hi * (x/z_0hi)**(4/5)

    for i in range(0, x_len):
        if ibl_x[i] >= H_G:
            ibl_x[i] = H_G

    p_bottom = [(i*s_x*D, 0) for i in range(0, m.ceil(x_len/(s_x*D)))]
    p_top = [(i*s_x*D, 6) for i in range(0, m.ceil(x_len/(s_x*D)))]

    bottom_x, bottom_y = zip(*p_bottom)
    top_x, top_y = zip(*p_top)

    for (bx, by), (tx, ty) in zip(p_bottom, p_top):
        plt.plot([bx, tx], [by, ty], color='Blue', linestyle='-')

    U_hT_x = (u_star / k) * (np.log(ibl_x / z_0lo) / np.log(ibl_x / z_0hi)) * np.log((z_h / z_0hi) * (1 + D/(2 * z_h))**beta)

    plt.plot(x, U_hT_x)
    plt.xlabel('x [m]')
    plt.ylabel('U_hT_x [m/s]')
    plt.ylim(5, 11)
    plt.title('Hub Height Velocity')
    plt.grid(True)
    plt.show()