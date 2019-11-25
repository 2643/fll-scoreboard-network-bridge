from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import threading
import time

a = open('scores.xml', 'r')
b = a.readlines()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("".join(b), "utf-8"))


httpd = HTTPServer(('10.42.0.1', 81), SimpleHTTPRequestHandler)

while True:
    try:
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
        x = threading.Thread(target=httpd.serve_forever(), args=(0))
        x.start()
    except KeyboardInterrupt:
        x.kill()
