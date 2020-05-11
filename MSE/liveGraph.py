import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from random import randint

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
a=[]
for i in range(100):
    a.append(randint(1,30))

def animate(i):
    del a[0]
    a.append(randint(1,30))
    
    ax1.clear()
    ax1.plot(a)

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()