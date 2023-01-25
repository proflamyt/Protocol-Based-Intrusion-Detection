import pyshark

# initialize a capture object
def capture() -> list:

    capture = pyshark.LiveCapture(interface='eth0', bpf_filter='tcp port 80 or tcp port 443')

    capture.sniff(timeout=50)

    return list(capture)

