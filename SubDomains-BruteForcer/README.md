# DNS Bruteforcing

**What is DNS bruteforcing?**

It's a technique where the person takes a long list of common subdomain names and append their target to them and based on the response determines whether they are valid or not. This is similar to the dictionary attack.

Below we can what happens in bruteforcing:

- admin             ---->      admin.target.com
- internal.dev    ---->      internal.dev.target.com
- secret             ---->      secret.target.com
- backup      ---->      backp.target.com

I wrote simple tool to automate this attack using python, here is the usage of the tool:

```bash
┌──(azab㉿kali)-[~/Python-Scripts/SubDomains-BruteForcer]
└─$ python SubsBrute.py -d google.com -w words.txt 
accounts.google.com
admin.google.com
ads.google.com
apis.google.com
blog.google.com
calendar.google.com
chrome.google.com
cloud.google.com
code.google.com
developers.google.com
docs.google.com
drive.google.com
groups.google.com
```