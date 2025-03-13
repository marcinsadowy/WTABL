import matplotlib.pyplot as plt
import numpy as np

delta_ibl_0 = 70
z_0hi = 0.68
z_0lo = 0.0001
z_h = 70
s_x = 7
D = 80
k = 0.4
f = 10**(-4)
U_G = 10
C_star = 4.5

x_len = 10000
x = np.arange(0, x_len)

u_star_hi = (k * U_G) / (np.log(U_G / (f * z_0hi)) - C_star)
u_star_lo = (k * U_G) / (np.log(U_G / (f * z_0lo)) - C_star)

x_H_G = (((z_0hi/z_0lo)**(-u_star_hi/(u_star_lo - u_star_hi)) * z_0lo - z_h)/z_0hi)**(5/4) * z_0hi
H_G = z_h + z_0hi * (x_H_G / z_0hi) ** (4 / 5)
print(H_G)

def U_cT(x, delta_ibl_0, z_0hi, k, z_0lo, beta, H_G):
    x = np.arange(0, x_len)
    ibl_x = delta_ibl_0 + z_0hi * (x/z_0hi)**(4/5)

    for i in range(0, x_len):
        if ibl_x[i] >= H_G:
            ibl_x[i] = H_G

    U_hT_x = (u_star_lo / k) * (np.log(ibl_x / z_0lo) / np.log(ibl_x / z_0hi)) * np.log((z_h / z_0hi) * (1 + D/(2 * z_h))**beta)

    plt.plot(x, U_hT_x)
    plt.xlabel('Downstream distance [m]')
    plt.ylabel('Hub height velocity [m/s]')
    plt.ylim(5, 11)
    plt.title('\nHub height velocity as a function of downstream distance\n', wrap=True)
    plt.grid(True)
    plt.show()

    return U_hT_x

u = U_cT(x, delta_ibl_0, z_0hi, k, z_0lo, 0.68, H_G)
print(u[0])

#U_cT(x, x_len, delta_ibl_0, z_0hi, u_star, k, z_0lo, beta, H_G)
