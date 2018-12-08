import http.server
from prometheus_client import start_http_server
from prometheus_client import Counter

PORT_WEB = 8001
PORT_PROM = 8000

REQUEST = Counter('hello_worlds_total', 'Hello Worlds requested.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUEST.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello World\n")

if __name__ == "__main__":
    print("starting %d.." % PORT_PROM)
    start_http_server(PORT_PROM)
    print("starting %d.." % PORT_WEB)
    server = http.server.HTTPServer(('0.0.0.0', PORT_WEB), MyHandler)
    server.serve_forever()
