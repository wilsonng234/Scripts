from http.server import HTTPServer, BaseHTTPRequestHandler
from ssl import SSLContext, PROTOCOL_TLS_SERVER

PORT = 8000
CERTIFICATE_PATH = "localhost.pem"
PRIVATE_KEY_PATH = "localhost-key.pem"


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        try:
            with open(self.path[1:], "rb") as file:
                content = file.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "File not found")


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ("", PORT)
    httpd = server_class(server_address, handler_class)

    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
