import requests
import re
import urllib.parse as urlparse
import argparse

def parsing_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("-u", "--url", dest="target", help="Target URL")

	options = parser.parse_args()

	if not options.target:
		parser.error("\n[!] Enter Target URL, Use --help for more info.")

	return options


def extract_urls(target_url):
	response = requests.get(target_url)
	return re.findall('(?:href=")(.*?)"', str(response.content))

target_urls = []

def crawl(target_url):
	urls = extract_urls(target_url)
	for url in urls:
		url = urlparse.urljoin(options.target, url)

		if "#" in url:
			url = url.split("#")[0]

		if options.target in url and url not in target_urls:
			target_urls.append(url)
			print(url)
			crawl(url)



options = parsing_args()
crawl(options.target)

'''
┌──(azab㉿kali)-[~/Python-Scripts]
└─$ python3 Simple-WebApp-Crawler.py -u http://testphp.vulnweb.com/ 
http://testphp.vulnweb.com/style.css
http://testphp.vulnweb.com/index.php
http://testphp.vulnweb.com/categories.php
http://testphp.vulnweb.com/artists.php
http://testphp.vulnweb.com/disclaimer.php
http://testphp.vulnweb.com/cart.php
http://testphp.vulnweb.com/guestbook.php
http://testphp.vulnweb.com/AJAX/index.php
http://testphp.vulnweb.com/styles.css
http://testphp.vulnweb.com/
http://testphp.vulnweb.com/login.php
http://testphp.vulnweb.com/signup.php
http://testphp.vulnweb.com/userinfo.php
http://testphp.vulnweb.com/privacy.php
http://testphp.vulnweb.com/Mod_Rewrite_Shop/
http://testphp.vulnweb.com/hpp/
http://testphp.vulnweb.com/?pp=12
'''
