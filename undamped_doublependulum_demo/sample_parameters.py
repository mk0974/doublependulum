import numpy as np

m1 = 2 # mass one at knee joint
m2 = 1 # mass two at ankle joint
l_f = 2 # length of femur
l_t = 1.5 # length of tibia

## INITIAL CONDITIONS
theta_h = np.pi/8 # angle of hip from parallel
theta_k = np.pi/3 # angle between femur and knee (NOT USED IN CALCULATIONS)
phi = np.pi - (theta_k - theta_h) # angle of knee measured fro parallel (USED IN CALCULATIONS)
omega_h = 0 # starting angular velocity at hip
omega_phi = 0 # starting angular velocity at knee