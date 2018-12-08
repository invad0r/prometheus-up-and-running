import http.server
import random
from prometheus_client import start_http_server
from prometheus_client import Counter

PORT_WEB = 8001
PORT_PROM = 8000

REQUEST = Counter('hello_worlds_total', 'Hello Worlds requested.')

EXCEPTIONS = Counter('hello_world_exception_total','Exception serving Hello World')

SALES = Counter('hello_world_sales_euro_total','Euros made serving Hello World')

class MyHandler(http.server.BaseHTTPRequestHandler):
    @EXCEPTIONS.count_exceptions()  # as function decorator
    def do_GET(self):
        REQUEST.inc()
        euros =  random.random()
        SALES.inc()
#        with EXCEPTIONS.count_exceptions():
#          if random.random() < 0.2:
#            raise Exception
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello World for {} euros.".format(euros).encode())

if __name__ == "__main__":
    print("starting %d.." % PORT_PROM)
    start_http_server(PORT_PROM)
    print("starting %d.." % PORT_WEB)
    server = http.server.HTTPServer(('0.0.0.0', PORT_WEB), MyHandler)
    server.serve_forever()
