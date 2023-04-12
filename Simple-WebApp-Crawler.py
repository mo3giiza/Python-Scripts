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

