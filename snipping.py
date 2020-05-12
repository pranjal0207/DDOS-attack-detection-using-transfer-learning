import pyshark 
import datetime

i = 0
while (1):
    packet = pyshark.LiveCapture(interface= "wlp1s0" )
    for cap in packet.sniff_continuously(packet_count=1):
        if (i == 0) :
            pack_time = 0
            time = float(cap.sniff_timestamp)
            i = 1
        pack_time = float(cap.sniff_timestamp) - time
        time = float(cap.sniff_timestamp)
        size = cap.length
        packet = 1
        prot = cap.transport_layer
        
        if hasattr(cap, 'tcp'):
            port = cap.tcp.dstport
        if hasattr(cap, 'udp'):
            port = cap.udp.dstport
        print (pack_time, "\t", size, "\t", packet, "\t", prot, "\t", port)