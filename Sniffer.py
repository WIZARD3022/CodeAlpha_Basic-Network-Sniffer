from scapy.all import sniff
def packet_callback(packet):
    print(packet.summary())
    print(packet.show())

    
def start_sniffing(interface):
    print(f"Starting to Sniff on {interface}")
    sniff(iface = interface, prn = packet_callback, store = 0)

    
if __name__ == "__main__":
    network_interface = "Wi-Fi"
    # use the your network such as if using Wifi use "Wi-Fi"
    # otherwise if using ethernet use "eth0" or "eth1"
    start_sniffing(network_interface)
