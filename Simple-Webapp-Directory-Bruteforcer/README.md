# Simple WebApp Directory BruteForcer

**Web directory brute forcing is the process of trying to enumerate and access hidden directories or files within a web application by guessing possible directory and file names. This technique is commonly used by hackers to find vulnerabilities in web applications. I wrote simple tool to automate this attack using python, here is the usage of the tool:**

```bash
┌──(azab㉿kali)-[~/Python-Scripts/Simple-Webapp-Directory-Bruteforcer]
└─$ python WebApp-Directory-BruteForcer.py -u http://testphp.vulnweb.com/ -w ~/Python-Scripts/Simple-Webapp-Directory-Bruteforcer/common.txt 
[+] http://testphp.vulnweb.com/cart.php [200 OK]
[+] http://testphp.vulnweb.com/login.php        [200 OK]
[+] http://testphp.vulnweb.com/AJAX     [200 OK]
[+] http://testphp.vulnweb.com/AJAX/index.php   [200 OK]
[+] http://testphp.vulnweb.com/artists.php      [200 OK]
[-] http://testphp.vulnweb.com/.bash_history    [404 Not Found]
[-] http://testphp.vulnweb.com/.bashrc  [404 Not Found]
[-] http://testphp.vulnweb.com/.cache   [404 Not Found]
[-] http://testphp.vulnweb.com/.config  [404 Not Found]
[-] http://testphp.vulnweb.com/.cvs     [404 Not Found]
```