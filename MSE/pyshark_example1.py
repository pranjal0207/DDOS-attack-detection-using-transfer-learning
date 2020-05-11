""" import pyshark


# Sniff from interface
capture = pyshark.LiveCapture(interface='enp2s0',output_file = 'abc.pcap')
capture.set_debug()
capture.sniff(timeout=10)
print(capture) """

import pyshark


# Sniff from interface

i=0
#while (1):
capture = pyshark.LiveCapture(interface='wlp3s0')
capture.set_debug()
capture.sniff(timeout=5)
""" for i in capture:
    print("Timestamp",i.sniff_time, i.length)
    print("Destination:",i.ip.dst,"\nSource:",i.ip.src)
    print("--------------------------------------------") """
print("Timestamp",capture[1].sniff_time, capture[1].length)
print("Destination:",capture[1].ip.flags)
print(dir(capture[0].transport_layer.__hash__))