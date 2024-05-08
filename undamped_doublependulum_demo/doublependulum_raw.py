import numpy as np

# NO DAMPING OR DRIVING

class doublependulum_raw:
    # CONSTANTS
    GRAVITY = -9.8 # [m/s]

    def __init__(self, m1, m2, l_f, l_t, theta_h_i, theta_k_i, omega_h_i, omega_phi_i):
        # UNIQUE CONSTANTS
        self.m1 = m1 #[kg]
        self.m2 = m2 #[kg]
        self.l_f = l_f #[m]
        self.l_t = l_t #

        # INTIAL CONDITIONS
        self.theta_h = theta_h_i
        self.phi = np.pi - (theta_k_i - theta_h_i)
        self.omega_h = omega_h_i
        self.omega_phi = omega_phi_i

        # COORDINATES (to be populated)
        self._x_knee = list()
        self._y_knee = list()
        self._x_ankle = list()
        self._y_ankle = list()

    # POSITION VECTORS (used for getting coordinates of joints for each time step)
    def r_1(self):
        x = self.l_f * np.cos(self.theta_h)
        y = -self.l_f * np.sin(self.theta_h)
        return [x, y]
    
    def r_2(self):
        r1 = self.r_1()
        x = r1[0] + self.l_t * np.cos(self.phi)
        y = r1[1] - self.l_t * np.sin(self.phi)
        return [x, y]
    
    # MOMENT OF INERTIAS (derived from masses and lengths)
    def moment_of_inertia_femur(self):
        I1 = self.m1 * np.square(self.l_f)
        return I1
    
    def moment_of_inertia_tibia(self):
        I2 = self.m2 * np.square(self.l_t)
        return I2
    
    # TENSION OF TIBIA ON FEMUR (contributes to torque of femur)
    def T(self):
        v2 = (self.l_f * self.omega_h * (np.sin(self.theta_h) + np.cos(self.theta_h))) * (self.l_t * self.omega_phi * (np.sin(self.phi) + np.cos(self.phi)))
        T = -(self.m2 / self.l_t) * v2 # tension is a vector and is negative
        return T
    
    # EULER'S METHOD (given a time step defined by situation)
    def update_pendulum(self, time_step):
        t = time_step
        tension = self.T()

        # UPDATE phi
        self.omega_phi += - ((self.l_t * self.m2 * self.GRAVITY) / self.moment_of_inertia_tibia()) * np.cos(self.phi) * t
        self.phi += self.omega_phi * t

        # UPDATE theta_h

        self.omega_h += - ((self.l_f * self.m1 * self.GRAVITY) / self.moment_of_inertia_femur() * np.cos(self.theta_h) + tension * self.l_f / self.moment_of_inertia_femur() * np.cos(self.theta_h - self.phi)) * t # theta_h - phi = theta_k - pi
        self.theta_h += self.omega_h * t

        # UPDATE theta_k (in case)
        self.theta_k = np.pi + self.theta_h - self.phi

    # POPULATE COORDINATE ARRAYS
    def populateFrames(self, time_step, frames):
        t = time_step
        f = frames

        for x in range(f):
            r1 = self.r_1()
            r2 = self.r_2()

            self._x_knee.append(r1[0])
            self._y_knee.append(r1[1])
            self._x_ankle.append(r2[0])
            self._y_ankle.append(r2[1])

            self.update_pendulum(t)
    
    # GETTERS FOR ARRAYS (with index)

    def get_x_knee(self, index):
        return self._x_knee[index]
    
    def get_y_knee(self, index):
        return self._y_knee[index]
    
    def get_x_ankle(self, index):
        return self._x_ankle[index]
    
    def get_y_ankle(self, index):
        return self._y_ankle[index]

    # CLEAR COORDINATE DATA
    def clearData(self):
        self._x_knee.clear()
        self._y_knee.clear()
        self._x_ankle.clear()
        self._y_ankle.clear()

# WITH RANGE RESTRICTIONS FOR JOINTS

# class doublependulum_restricted(doublependulum_raw):





        