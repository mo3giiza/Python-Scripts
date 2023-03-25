import requests
import argparse

def parsing_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("-u", "--url", dest="url",help="Target URL")
	parser.add_argument("-w", "--wordlist", dest="wordlist",help="Wordlist file path")

	options = parser.parse_args()

	if not options.url:
		parser.error("\n[!] Enter Target URL, Use --help for more info.")
	if not options.wordlist:
		parser.error("\n[!] Enter File That Containing Directories, Use --help for more info.")

	return options

def response_status_codes():

	if response.status_code == 200:
		print(f"[+] {target_url}\t[{response.status_code} OK]")
	elif response.status_code == 301:
		print(f"[+] {target_url}\t[{response.status_code} Moved Permanently]")
	elif response.status_code == 302:
		print(f"[+] {target_url}\t[{response.status_code} Found]")	
	elif response.status_code == 401:
		print(f"[+] {target_url}\t[{response.status_code} Unauthorized]")
	elif response.status_code == 403:
		print(f"[+] {target_url}\t[{response.status_code} Forbidden]")
	elif response.status_code == 404:
		print(f"[-] {target_url}\t[{response.status_code} Not Found]")
	elif response.status_code == 429:
		print(f"[+] {target_url}\t[{response.status_code} Too Many Requests]")
	elif response.status_code == 500:
		print(f"[+] {target_url}\t[{response.status_code} Internal Server Error]")

options = parsing_args()

try:
	file = open(options.wordlist, 'r')
	for line in file:
		directory = line.strip()
		target_url = options.url + directory
		# Making a request
		response = requests.get(target_url)
		
		# Calling response_status_codes function
		response_status_codes()

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C .. Quitting\n")
    exit()

except PermissionError:
    print("\n[-] Operation not permitted, Run the script as superuser ..\n")
    exit()