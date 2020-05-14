import matplotlib.pyplot as plt
import time
import random
import pyshark
import numpy as np
 
xdata = []
ydata = []
 
plt.show()

x = 10
axes = plt.gca()
axes.set_xlim(0, x)
axes.set_ylim(0, 500)
line, = axes.plot(xdata, ydata, 'r-')
x_base = np.arange(100)
 
i = 0
while(1):
    packet = pyshark.LiveCapture(interface= "wlp1s0" )
    for cap in packet.sniff_continuously(packet_count=1):
        size = cap.length
        xdata.append(i)
        ydata.append(int(size))
        line.set_xdata(xdata)
        line.set_ydata(ydata)
        plt.draw()
        plt.pause(1e-17)
        time.sleep(0.1)
        if (i>x):
            x = x + 10
            axes.set_xlim(0, x)
    i = i + 1

plt.show()