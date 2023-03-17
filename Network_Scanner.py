# pip install scpay
# pip install argparse

# The scapy.all library is imported as scapy for convenience.
import scapy.all as scapy
# argparse is Python's standard library parse command-line arguments
# We can use optparse but it become deprecated 
import argparse

# function to take arguments from user
def parsing_args():

	# Object to handle user input using argument
	parser = argparse.ArgumentParser()

	# Adding options to parser object
	parser.add_argument("-t", "--target", help="Traget IP / IP Range")

	# Method to allow object what user input and handle it
	options = parser.parse_args()

	# Error Handling
	if not options.target:
		print("Please enter Traget IP / IP Range to scan, use -h for help")
	return options


'''
1- The function creates an ARP request packet for the specified IP address or MAC address.
2- It creates an Ethernet broadcast packet to send the ARP request to all devices on the network.
3- It combines the ARP request and the broadcast packets into a single packet.
4- It sends the packet using scapy.srp, which sends the packet at the link layer and waits for responses.
5- It waits for 1 second for responses, and sets verbose to False to suppress output.
6- It extracts the IP and MAC addresses from the responses and adds them to a list of clients.
7- It returns the list of clients.
'''
def scan(ip):
	arp_req = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_req_broadcast = broadcast/arp_req
	ans = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
	
	clients_list = []
	for element in ans:
		clients_dict = {"ip":element[1].psrc, "mac":element[1].hwsrc}
		clients_list.append(clients_dict)
	return clients_list

# function to print the final results and handle the output
def print_result(results_list):
	print("==========================================")
	print("IP\t\t\tMAC Address\n==========================================")
	for client in results_list:
		print(client["ip"] + "\t\t" + client["mac"])

# Create options object to take the output from parsing_args() function
options = parsing_args()
result_scan = scan(options.target)
print_result(result_scan)


# Note the script run in python and python3