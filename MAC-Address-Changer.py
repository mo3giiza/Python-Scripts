# pip install subprocess
# pip install optparse
# pip install re
import subprocess, optparse, re

def parsing_args():
	# Object to handle user input using argument
	parser = optparse.OptionParser()

	# Adding options to parser object
	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="new_macaddr", help="New MAC address you want to set")

	# Method to allow object what user input and handle it
	(options, arguments) = parser.parse_args()

	# Handling errors
	if not options.interface:
		parser.error("[-][-] Please enter an interface, use -h for more information")

	if not options.new_macaddr:
		parser.error("[-][-] Please enter a new MAC address, use -h for more information")

	return options

def changing_mac(interface, new_macaddr):
	print(f">> Changing MAC Address For {interface} To {new_macaddr}\n")

	#subprocess.call(["ifconfig", show_interfaces])
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_macaddr])
	subprocess.call(["ifconfig", interface, "up"])
	#subprocess.call(["ifconfig", interface])

def getting_current_mac(interface):
	ifconfig_result = subprocess.check_output(["ifconfig", interface])
	#print(ifconfig_result)
	regex_result = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

	if regex_result:
		return regex_result.group(0)
	else:
		print("[!][!] Could not read the MAC address!!")

options = parsing_args()

current_mac = getting_current_mac(options.interface)
print(f"[+] Current MAC Addr = {str(current_mac)}")

changing_mac(options.interface, options.new_macaddr)

current_mac = getting_current_mac(options.interface)
if current_mac != options.new_macaddr:
	print(f"[+][+] MAC address was succesfully changed to {current_mac}")
else:
	print("[!][!] MAC address didn't changed.")


''' Output

└─$ sudo python3 MAC-Changer.py -i eth0 -m 00:55:63:44:55:66
[+] Current MAC Addr = b'76:22:43:94:73:44'
>> Changing MAC Address For eth0 To 00:55:63:44:55:66

[+][+] MAC address was succesfully changed to b'00:55:63:44:55:66'

'''
