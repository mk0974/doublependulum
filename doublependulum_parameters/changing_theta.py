from undamped_demo import *

print(theta_h)
def update_system_undamped(theta_h, phi, omega_h, omega_phi, m_1, m_2, l_f, l_t, g, b_1, b_2, t): #including all relevant parameters in function parameters
    I_1 = m_1 * np.square(l_f) # moment of inertia of femur
    I_2 = m_2 * np.square(l_t) # moment of inertia of tibia
    T = (m_2 / l_t) * (np.square(l_f) * np.square(omega_h) + 2 * l_f * l_t * omega_h * omega_phi + np.square(l_t) * np.square(omega_phi)) # tension of the tibia swinging
    
    new_omega_phi = omega_phi - (b_2 / I_2 * omega_phi + (l_t * m_2 * g) / I_2 * np.cos(phi)) * t
    new_phi = phi + new_omega_phi * t

    new_omega_h = omega_h - (b_1 / I_1 * omega_h + (l_f * m_1 * g) / I_1 * np.cos(theta_h) - (l_f / I_1) * T) * t
    new_theta_h = theta_h + new_omega_h * t

    return new_omega_phi, new_phi, new_omega_h, new_theta_h

print(update_system_undamped)