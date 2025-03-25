import matplotlib.pyplot as plt
import numpy as np

def U_hT(ibl_x, z_0hi, k, z_0lo, u_star_lo, z_h, D, beta, H_G):
    
    
    x_len = 20000
    x = np.arange(0, x_len)
    
    """
    ibl_x = delta_ibl_0 + z_0hi * (x/z_0hi)**(4/5)

    for i in range(0, x_len):
        if ibl_x[i] >= H_G:
            ibl_x[i] = H_G
    """
    
    U_hT_x = (u_star_lo / k) * (np.log(ibl_x / z_0lo) / np.log(ibl_x / z_0hi)) * np.log((z_h / z_0hi) * (1 + D/(2 * z_h))**beta)

    plt.plot(x, U_hT_x)
    plt.xlabel('x')
    plt.ylabel('Hub height velocity [m/s]')
    plt.ylim(5, 11)
    plt.grid(True)
    plt.show()
    
    return U_hT_x