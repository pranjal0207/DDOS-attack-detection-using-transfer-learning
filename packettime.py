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
axes.set_ylim(0, 5)
line, = axes.plot(xdata, ydata, 'r-')
x_base = np.arange(100)
 
i = 0
while(1):
    packet = pyshark.LiveCapture(interface= "wlp1s0" )
    for cap in packet.sniff_continuously(packet_count=1):
        if (i == 0) :
            pack_time = 0
            time1 = float(cap.sniff_timestamp)
            i = 1
        pack_time = float(cap.sniff_timestamp) - time1
        time1 = float(cap.sniff_timestamp)
        size = cap.length
        print (pack_time, i)
        xdata.append(i)
        ydata.append(pack_time)
        line.set_xdata(xdata)
        line.set_ydata(ydata)
        plt.draw()
        plt.pause(1e-17)
        time.sleep(1)
        if (i>x):
            x = x + 10
            axes.set_xlim(0, x)
    i = i + 1

plt.show()