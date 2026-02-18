import matplotlib.pyplot as plt


#circle1 = plt.Circle((0.5, 0.5), 0.2, color='black', fill=False, linewidth=18)
#circle2 = plt.Circle((0.5, 0.5), 0.3, color='black', fill=False)
#circle3 = plt.Circle((0.5, 0.5), 0.4, color='black', clip_on=False, fill=False)


fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
ax = plt.gca()
# change default range so that new disks will work
ax.axis("equal")
ax.set_xlim((-15, 15))
ax.set_ylim((-15, 15))
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

for i in range(0,10,1):
    circle = plt.Circle((0.5, 0.5), 1*i, color='black', fill=False, linewidth=5)
    ax.add_patch(circle)

    
#ax.add_patch(circle2)
#ax.add_patch(circle3)


fig.show()
#fig.savefig('plotcircles.png')
