

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

route=[(1,1), (1,2), (1,3), (1,4), (2,4), (3,4), (2,4), (1,4), (1,3), (1,2), (1,1)]

fig = plt.figure()
axes = fig.add_subplot(111, autoscale_on=False)
axes.set_xlim(0,6)
axes.set_ylim(0,6)
N = 2
points = []
for i in range(N):
    points.append(axes.plot([],[], 'go', ms = 6)[0])
    # points.append(axes.plot([],[], 'bo', ms = 15)[0])
# point, = axes.plot([],[], 'go', markersize = 6)


def animation(coords):   
    
    for i in range(N):
        points[i].set_data([coords[0]],[coords[1]])
    # point2.set_data([coords[1]],[coords[2]])
    return points,

def frames():
   for x,y in route:
      yield x,y 
#    for acc_11_pos, acc_12_pos in zip(Acc_11, Acc_12):
#        yield acc_11_pos, acc_12_pos

ani = FuncAnimation(fig, animation, frames=frames, interval=300, repeat=False)  # decreased interval

plt.show()
