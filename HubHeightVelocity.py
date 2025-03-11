import matplotlib.pyplot as plt
import numpy as np

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

    U_hT_x = (u_star / k) * (np.log(ibl_x / z_0lo) / np.log(ibl_x / z_0hi)) * np.log((z_h / z_0hi) * (1 + D/(2 * z_h))**beta)

    plt.plot(x, U_hT_x)
    plt.xlabel('Downstream distance [m]')
    plt.ylabel('Hub height velocity [m/s]')
    plt.ylim(5, 11)
    plt.title('\nHub height velocity as a function of downstream distance\n', wrap=True)
    plt.grid(True)
    plt.show()

#U_cT(x, x_len, delta_ibl_0, z_0hi, u_star, k, z_0lo, beta, H_G)
