import requests

url = "http://testphp.vulnweb.com/login.php"

data = {
	"uname":"test",
	"pass":"test",
	"submit":"login"
}

response = requests.post(url, data=data)
print(response)