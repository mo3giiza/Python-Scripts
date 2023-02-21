import urllib.request

# Get URL, path to save file and file name
file_url = input(">> Enter the URL to file: ")
file_path = input(">> Enter the path that you want to save the file: ")

print("[+][+] Downloading File... ")

# Download file by urllib.request library
urllib.request.urlretrieve(file_url,file_path)

print("File has been downloaded successfully :)")

