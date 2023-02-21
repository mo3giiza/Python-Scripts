import http.server
import socketserver

port = 9000

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",port),handler)

URL = f"http://127.0.0.1:{port}"
print(f"The server is up on {URL}")
httpd.serve_forever()