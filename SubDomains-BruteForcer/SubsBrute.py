import requests
import argparse

def parsing_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("-d", "--domain", dest="domain",help="Domain, like example.com")
	parser.add_argument("-w", "--wordlist", dest="wordlist",help="Wordlist file path")

	options = parser.parse_args()

	if not options.domain:
		parser.error("\n[!] Enter Target URL, Use --help for more info.")
	if not options.wordlist:
		parser.error("\n[!] Enter File That Containing Words, Use --help for more info.")

	return options

def request(domain):
	try:
		return requests.get(f"http://{domain}")
	except requests.exceptions.ConnectionError:
		#print("[-] URL dosen't exist..")
		pass

options = parsing_args()

try:
	with open(options.wordlist, 'r') as wordlist_file:
		for line in wordlist_file:
			word = line.strip()
			full_url = f"{word}.{options.domain}"
			response = request(full_url)
			if response:
				print(full_url)

except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C .. Quitting\n")
    exit()

except PermissionError:
    print("\n[-] Operation not permitted, Run the script as superuser ..\n")
    exit()
    