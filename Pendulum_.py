import numpy as np
import matplotlib.pyplot as plt

def fo(time,theta,theta_dot):
    return theta_dot

def f1(time,theta,theta_dot):
    return -np.sin(theta)

def rk4(theta_o,theta_dot_o,dt,tf,to=0):
    n = int((tf-to)/dt) + 1
    theta_dot = []
    time = []
    theta = []
    for i in range(n):
        time.append(to)
        theta.append(theta_o)
        theta_dot.append(theta_dot_o)
        k1 = dt*fo(to, theta_o, theta_dot_o)
        k2 = dt*fo(to+(dt/2), theta_o+k1/2, theta_dot_o)
        k3 = dt*fo(to+(dt/2), theta_o+k2/2, theta_dot_o)
        k4 = dt*fo(to+dt, theta_o+k3, theta_dot_o)

        l1 = dt*f1(to, theta_o, theta_dot_o)
        l2 = dt*f1(to+(dt/2), theta_o, theta_dot_o+l1/2)
        l3 = dt*f1(to+(dt/2), theta_o, theta_dot_o+l2/2)
        l4 = dt*f1(to+dt, theta_o, theta_dot_o+l3)

        theta_o += (k1 + 2*k2 + 2*k3 + k4)/6
        theta_dot_o += (l1 + 2*l2 + 2*l3 + l4)/6

        to += dt
    return time,theta,theta_dot

theta = np.linspace(-np.pi, np.pi, 10000)
thetas = np.deg2rad([10,20,45,90,120,160,180])
# print(thetas)

for i in thetas:
    t,theta,theta_dot = rk4(i,0,0.0001,50)
    plt.plot(theta,theta_dot)

plt.gca().set_aspect(10/10)
plt.xlabel(r"Angle ($\theta$) [rad]")
plt.ylabel(r"Radial velocity ($\dot{\theta}$) [rad/s]")
plt.title("")
# plt.savefig("Phase_space_given.svg")
plt.show()
