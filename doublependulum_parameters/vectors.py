import numpy as np
from undamped_demo import *
from changing_theta import update_system_undamped


new_omega_phi, new_phi, new_omega_h, new_theta_h =  update_system_undamped(theta_h, phi, omega_h, omega_phi, m_1, m_2, l_f, l_t, g, b_1, b_2, t)

print(new_theta_h)


# def r_1(l_f, theta_h): #calculates the position vector of knee given a theta
#     x = l_f * np.cos(theta_h)
#     y = -l_f * np.sin(theta_h) # y defined negative in order to hang leg down
#     return np.array([x, y])

# r_10 = r_1(l_f, theta_h)

# def r_2(r_1, l_t, theta_k, phi): #calculates the position vector of ankle given a theta    
#     x = r_1[0] + l_t * np.cos(phi)
#     y = r_1[1] - l_t * np.sin(phi) # y defined negative in order to hang leg down
#     return np.array([x, y])