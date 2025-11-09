import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dt = 0.03 # Zeitschritte
n_balls = 3 # Anzahl der kugeln

# Startposition und Geschw.
positions = np.random.uniform(1.1,9, (n_balls, 2)) # (a,b,(shape)) -> n_balls = Anzahl der Zeilen
print(positions)
velocities = np.array([
    [0.5, 2.0],
    [1.3, 1.0],
    [-1.0, 0.45]
])
"""
positions = np.array([
    [0.0, 0.0]
    [2.0, 1.0]
    [-1.0, 2.0]
])
"""


"""
array([
  [ 0.52, -0.73],  # Kugel 1 → [[ 0.74504408  0.63028008]
  [-0.12,  0.89],  # Kugel 2 →  [ 0.08057956 -0.7862975 ]]
  [ 0.34,  0.01]   # Kugel 3 →  [ 0.08057956 -0.7862975 ]]
])
"""
# Plot
fig, ax = plt.subplots()
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_aspect("equal")
scat = ax.scatter(positions[:,0], positions[:,1], s= 100)  # Alle x und y positionen

def update(frame):
    global positions,velocities
    
    # Bewegung
    positions += (velocities-[0,0.981]) * dt
    # Beschleunigung -> positions += (velocities + i)*dt

    # Reflexion an Wänden
    for i in range(n_balls):
        for dim in [0,1]:
            if positions[i, dim] < 0.5:  # positions[i, dim] === Kugel i entweder dim= 0 für x-koord oder dim = 1 für y-koord
                positions[i,dim] = 0.5
                velocities[i, dim] *= -1 # Richtung x und y gespiegelt
                print(velocities[i, dim])
            elif positions[i,dim] > 9.5:
                positions[i,dim] = 9.5
                velocities[i, dim] *= -1 # Richtung x und y gespiegelt
    scat.set_offsets(positions)
    return scat,
ani = FuncAnimation(fig, update, frames=200, interval=10, blit=True)
plt.show()