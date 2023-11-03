import socket
from flask import Flask
from flask_api import status

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8000
CERTIFICATE_PATH = "cert.pem"
PRIVATE_KEY_PATH = "key.pem"

application = Flask(__name__)


@application.route("/")
def index():
    try:
        with open("index.html", "rb") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found", status.HTTP_400_BAD_REQUEST


if __name__ == "__main__":
    application.run(
        host=HOST, port=PORT, ssl_context=(CERTIFICATE_PATH, PRIVATE_KEY_PATH)
    )
