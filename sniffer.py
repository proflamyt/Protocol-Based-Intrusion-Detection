import pyshark

# initialize a capture object
capture = pyshark.LiveCapture(interface='eth0')

# start capturing packets
capture.sniff(timeout=50)

# convert the captured packets to a list
packets = list(capture)
